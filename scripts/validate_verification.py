#!/usr/bin/env python3
"""validate_verification.py — ScreenshotSkill result validator.

Validates:
  1. JSON results against schemas/visual-verification.schema.json
     (self-contained mini validator for the JSON-Schema subset this skill uses —
     no third-party dependencies).
  2. Cross-field consistency rules that a schema cannot express (SCORING.md):
       - weights keys == categories keys and sum to 1.00 (+/- 0.011)
       - score == round1(sum(category*weight) - sum(penalty.points))   (+/- 0.15)
       - status "pass"  <=> score >= threshold AND no unresolved critical problem
       - iteration <= max_iterations (default 5)
       - total penalty <= 3.0
       - score_delta == score - previous_score                          (+/- 0.15)
  3. Markdown reports against the template (headings, status/score/threshold/
     iteration lines, category-table math, blocking CRITICALs); an embedded
     ```json block, if present, is validated as a full JSON result.

Usage:
  validate_verification.py result.json [more.json ...]
  validate_verification.py --report report.md [more.md ...]
  validate_verification.py --self-test

Exit code: 0 = everything passed, 1 = validation failures, 2 = usage/IO error.
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schemas" / "visual-verification.schema.json"

DEFAULT_WEIGHTS = {
    "silhouette": 0.20,
    "proportions": 0.15,
    "structure": 0.15,
    "geometry": 0.10,
    "materials": 0.10,
    "reference_similarity": 0.15,
    "style": 0.10,
    "composition": 0.05,
}
DEFAULT_THRESHOLD = 7.0
DEFAULT_MAX_ITERATIONS = 5
PENALTY_CAP = 3.0
MATH_TOL = 0.15


# --------------------------------------------------------------------------
# Mini JSON-Schema validator (subset used by this skill's schema)
# --------------------------------------------------------------------------

class MiniSchemaValidator:
    def __init__(self, schema):
        self.root = schema
        self.errors = []

    def validate(self, instance):
        self._check(instance, self.root, "$", self.root)
        return self.errors

    def _err(self, path, msg):
        self.errors.append("%s: %s" % (path, msg))

    def _resolve(self, ref):
        if not ref.startswith("#/"):
            self._err("$", "unsupported non-local $ref %r" % ref)
            return {}
        node = self.root
        for part in ref[2:].split("/"):
            node = node.get(part, {})
        return node

    def _type_ok(self, inst, t):
        if t == "object":
            return isinstance(inst, dict)
        if t == "array":
            return isinstance(inst, list)
        if t == "string":
            return isinstance(inst, str)
        if t == "number":
            return isinstance(inst, (int, float)) and not isinstance(inst, bool)
        if t == "integer":
            return isinstance(inst, int) and not isinstance(inst, bool)
        if t == "boolean":
            return isinstance(inst, bool)
        if t == "null":
            return inst is None
        return True

    def _check(self, inst, schema, path, root):
        if not isinstance(schema, dict):
            return
        if "$ref" in schema:
            schema = dict(self._resolve(schema["$ref"]),
                          **{k: v for k, v in schema.items() if k != "$ref"})

        if "type" in schema:
            types = schema["type"]
            if isinstance(types, str):
                types = [types]
            if not any(self._type_ok(inst, t) for t in types):
                self._err(path, "expected type %s, got %s"
                          % ("/".join(types), type(inst).__name__))
                return

        if "enum" in schema and inst not in schema["enum"]:
            self._err(path, "value %r not in enum %r" % (inst, schema["enum"]))
        if "const" in schema and inst != schema["const"]:
            self._err(path, "expected const %r, got %r" % (schema["const"], inst))

        if isinstance(inst, (int, float)) and not isinstance(inst, bool):
            if "minimum" in schema and inst < schema["minimum"]:
                self._err(path, "%r < minimum %r" % (inst, schema["minimum"]))
            if "maximum" in schema and inst > schema["maximum"]:
                self._err(path, "%r > maximum %r" % (inst, schema["maximum"]))
            if "exclusiveMinimum" in schema and inst <= schema["exclusiveMinimum"]:
                self._err(path, "%r <= exclusiveMinimum %r"
                          % (inst, schema["exclusiveMinimum"]))
            if "exclusiveMaximum" in schema and inst >= schema["exclusiveMaximum"]:
                self._err(path, "%r >= exclusiveMaximum %r"
                          % (inst, schema["exclusiveMaximum"]))

        if isinstance(inst, str):
            if "minLength" in schema and len(inst) < schema["minLength"]:
                self._err(path, "string shorter than minLength %d"
                          % schema["minLength"])
            if "maxLength" in schema and len(inst) > schema["maxLength"]:
                self._err(path, "string longer than maxLength %d"
                          % schema["maxLength"])
            if "pattern" in schema and not re.search(schema["pattern"], inst):
                self._err(path, "string does not match pattern %r"
                          % schema["pattern"])

        if isinstance(inst, list):
            if "minItems" in schema and len(inst) < schema["minItems"]:
                self._err(path, "fewer than minItems %d" % schema["minItems"])
            if "maxItems" in schema and len(inst) > schema["maxItems"]:
                self._err(path, "more than maxItems %d" % schema["maxItems"])
            if schema.get("uniqueItems"):
                seen = set()
                for item in inst:
                    key = json.dumps(item, sort_keys=True, default=str)
                    if key in seen:
                        self._err(path, "duplicate item violates uniqueItems")
                        break
                    seen.add(key)
            if "items" in schema:
                for i, item in enumerate(inst):
                    self._check(item, schema["items"], "%s[%d]" % (path, i), root)

        if isinstance(inst, dict):
            for key in schema.get("required", []):
                if key not in inst:
                    self._err(path, "missing required property %r" % key)
            props = schema.get("properties", {})
            ap = schema.get("additionalProperties", True)
            name_pat = schema.get("propertyNames", {}).get("pattern")
            for key, val in inst.items():
                cpath = "%s.%s" % (path, key)
                if name_pat and not re.search(name_pat, key):
                    self._err(cpath, "property name does not match pattern %r"
                              % name_pat)
                if key in props:
                    self._check(val, props[key], cpath, root)
                elif ap is False:
                    self._err(cpath, "additional property not allowed")
                elif isinstance(ap, dict):
                    self._check(val, ap, cpath, root)
            if "minProperties" in schema and len(inst) < schema["minProperties"]:
                self._err(path, "fewer than minProperties %d"
                          % schema["minProperties"])
            if "maxProperties" in schema and len(inst) > schema["maxProperties"]:
                self._err(path, "more than maxProperties %d"
                          % schema["maxProperties"])

        for clause in schema.get("allOf", []):
            self._check(inst, clause, path, root)
        for kw in ("anyOf", "oneOf"):
            if kw in schema:
                sub = MiniSchemaValidator(root)
                matches = 0
                for clause in schema[kw]:
                    sub.errors = []
                    sub._check(inst, clause, path, root)
                    if not sub.errors:
                        matches += 1
                if kw == "anyOf" and matches == 0:
                    self._err(path, "matches none of anyOf")
                if kw == "oneOf" and matches != 1:
                    self._err(path, "matches %d of oneOf (expected exactly 1)"
                              % matches)


# --------------------------------------------------------------------------
# Consistency rules (scripts enforce what the schema cannot express)
# --------------------------------------------------------------------------

def effective_weights(doc):
    """Return {category: weight} actually used for scoring, or raise ValueError."""
    cats = doc.get("categories", {})
    weights = doc.get("weights")
    if weights is None:
        known = {k: DEFAULT_WEIGHTS[k] for k in cats if k in DEFAULT_WEIGHTS}
        unknown = [k for k in cats if k not in DEFAULT_WEIGHTS]
        if unknown:
            raise ValueError("categories %s have no default weight; "
                             "explicit 'weights' required" % unknown)
        total = sum(known.values())
        return {k: v / total for k, v in known.items()}
    return weights


def check_consistency(doc):
    errors, warnings = [], []
    path = "$"

    cats = doc.get("categories", {})
    if cats:
        try:
            weights = effective_weights(doc)
        except ValueError as exc:
            errors.append("$: %s" % exc)
            weights = None
        if weights is not None:
            wk, ck = set(weights), set(cats)
            if wk != ck:
                errors.append("$: weights keys %s do not match categories keys %s"
                              % (sorted(wk), sorted(ck)))
            total_w = sum(weights.get(k, 0.0) for k in ck)
            if abs(total_w - 1.0) > 0.011:
                errors.append("$: weights over categories sum to %.4f, expected 1.00"
                              % total_w)

            expected = sum(cats[k] * weights.get(k, 0.0) for k in ck)
            penalty = sum(p.get("points", 0.0) for p in doc.get("penalties", []))
            if penalty > PENALTY_CAP + 1e-9:
                errors.append("$: total penalty %.2f exceeds cap %.2f"
                              % (penalty, PENALTY_CAP))
            final = max(0.0, min(10.0, expected - penalty))
            score = doc.get("score")
            if isinstance(score, (int, float)):
                if abs(score - final) > MATH_TOL:
                    errors.append(
                        "$: score %.2f != weighted total %.2f - penalties %.2f "
                        "= %.2f (tolerance %.2f)"
                        % (score, expected, penalty, final, MATH_TOL))
                if score >= 9.0:
                    warnings.append("$: score >= 9.0 requires explicit justification "
                                    "(anti-gaming rule 9)")

    status = doc.get("status")
    threshold = doc.get("threshold", DEFAULT_THRESHOLD)
    score = doc.get("score")
    if status and isinstance(score, (int, float)):
        if status == "pass" and score < threshold:
            errors.append("$: status 'pass' but score %.2f < threshold %.2f"
                          % (score, threshold))
        if status == "rework_required" and score >= threshold:
            errors.append("$: status 'rework_required' but score %.2f >= threshold "
                          "%.2f (unless a blocking critical exists, which must then "
                          "be present in problems)" % (score, threshold))
    if threshold != DEFAULT_THRESHOLD:
        warnings.append("$: non-default threshold %.2f — must be justified by the task"
                        % threshold)

    problems = doc.get("problems", [])
    open_critical = [p for p in problems
                     if p.get("severity") == "critical"
                     and p.get("status", "unresolved") != "verified_fixed"]
    if status == "pass" and open_critical:
        errors.append("$: status 'pass' with %d unresolved critical problem(s)"
                      % len(open_critical))
    if status == "pass" and [p for p in problems
                             if p.get("severity") == "high"
                             and p.get("status", "unresolved") != "verified_fixed"]:
        warnings.append("$: PASS with unresolved HIGH problems — disclose them clearly")

    iteration = doc.get("iteration")
    max_iter = doc.get("max_iterations", DEFAULT_MAX_ITERATIONS)
    if isinstance(iteration, int) and iteration > max_iter:
        errors.append("$: iteration %d exceeds max_iterations %d"
                      % (iteration, max_iter))

    prev, delta = doc.get("previous_score"), doc.get("score_delta")
    if prev is not None and delta is not None and isinstance(score, (int, float)):
        if abs((score - prev) - delta) > MATH_TOL:
            errors.append("$: score_delta %.2f != score %.2f - previous_score %.2f"
                          % (delta, score, prev))

    na = doc.get("next_action")
    if status == "pass" and na not in (None, "accept"):
        warnings.append("$: status 'pass' but next_action is %r (expected 'accept')"
                        % na)
    if status == "rework_required" and na == "accept":
        errors.append("$: status 'rework_required' but next_action 'accept'")

    ne = set(doc.get("not_evaluable", []))
    if ne & set(cats):
        errors.append("$: not_evaluable %s overlap with scored categories"
                      % sorted(ne & set(cats)))
    return errors, warnings


# --------------------------------------------------------------------------
# Validation drivers
# --------------------------------------------------------------------------

_schema_cache = None


def load_schema():
    global _schema_cache
    if _schema_cache is None:
        _schema_cache = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    return _schema_cache


def validate_json_doc(doc, label, schema_only=False):
    errors, warnings = [], []
    val = MiniSchemaValidator(load_schema())
    errors.extend("%s (schema)" % e for e in val.validate(doc))
    if not schema_only:
        ce, cw = check_consistency(doc)
        errors.extend(ce)
        warnings.extend(cw)
    return errors, warnings


def validate_json_file(path, schema_only=False):
    try:
        doc = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return ["%s: cannot read/parse JSON: %s" % (path, exc)], []
    return validate_json_doc(doc, str(path), schema_only)


# --------------------------------------------------------------------------
# Markdown report validation
# --------------------------------------------------------------------------

REQUIRED_SECTIONS = [
    "## Result",
    "## Category Scores",
    "## What Is Working",
    "## Problems",
    "## Reference Comparison",
    "## Required Changes",
    "## Verification Decision",
]

_RE_H1 = re.compile(r"^# Visual Verification Report\s*$", re.M)
_RE_H1_SPLIT = re.compile(r"^(# Visual Verification Report)\s*$", re.M)
_RE_STATUS = re.compile(r"^\**\s*Status:\**\s*(PASS|REWORK REQUIRED)\b", re.M)
_RE_SCORE = re.compile(r"^\**\s*Score:\**\s*([0-9]+(?:\.[0-9]+)?)\s*/\s*10\b", re.M)
_RE_THRESHOLD = re.compile(r"^\**\s*Threshold:\**\s*([0-9]+(?:\.[0-9]+)?)\b", re.M)
_RE_ITER = re.compile(r"^\**\s*Iteration:\**\s*(\d+)\s*/\s*(\d+)\b", re.M)
_RE_WTOTAL = re.compile(r"^\**\s*Weighted total:\**\s*([0-9]+(?:\.[0-9]+)?)\b", re.M)
_RE_PTOTAL = re.compile(r"^\**\s*Penalty total:\**\s*([0-9]+(?:\.[0-9]+)?)\b", re.M)
_RE_ROW = re.compile(
    r"^\|\s*([A-Za-z][A-Za-z /]*?)\s*\|\s*([0-9]+(?:\.[0-9]+)?|—|-)\s*(?:/10)?\s*"
    r"\|\s*([0-9]+(?:\.[0-9]+)?)\s*%(?:\s*\([^)]*\))?\s*\|", re.M)
_RE_CRIT = re.compile(r"^###\s*\[CRITICAL\]", re.M)
_RE_DECISION = re.compile(r"REWORK REQUIRED|PASS", re.M)
_RE_JSON_BLOCK = re.compile(r"```json\s*(\{.*?\})\s*```", re.S)


def validate_report_text(text, label):
    """Validate one or more reports ('# Visual Verification Report' sections)."""
    parts = re.split(_RE_H1_SPLIT, text)
    chunks = []
    if len(parts) >= 3:
        for i in range(1, len(parts), 2):
            chunks.append(parts[i] + (parts[i + 1] if i + 1 < len(parts) else ""))
    else:
        chunks = [text]

    errors, warnings = [], []
    for idx, chunk in enumerate(chunks, 1):
        sub = label if len(chunks) == 1 else "%s (report %d)" % (label, idx)
        e, w = _validate_single_report(chunk, sub)
        errors.extend(e)
        warnings.extend(w)
    return errors, warnings


def _validate_single_report(text, label):
    errors, warnings = [], []

    if not _RE_H1.search(text):
        errors.append("%s: missing '# Visual Verification Report' heading" % label)

    m = _RE_STATUS.search(text)
    status = m.group(1) if m else None
    if not status:
        errors.append("%s: missing 'Status: PASS|REWORK REQUIRED' line" % label)

    m = _RE_SCORE.search(text)
    score = float(m.group(1)) if m else None
    if score is None:
        errors.append("%s: missing 'Score: X.X / 10' line" % label)
    elif score > 10:
        errors.append("%s: score %.2f out of range" % (label, score))

    m = _RE_THRESHOLD.search(text)
    threshold = float(m.group(1)) if m else None
    if threshold is None:
        errors.append("%s: missing 'Threshold: X.X' line" % label)

    m = _RE_ITER.search(text)
    if not m:
        errors.append("%s: missing 'Iteration: N / M' line" % label)
    elif int(m.group(1)) > int(m.group(2)):
        errors.append("%s: iteration %s exceeds max %s"
                      % (label, m.group(1), m.group(2)))

    for section in REQUIRED_SECTIONS:
        if not re.search(r"^%s\s*$" % re.escape(section), text, re.M):
            errors.append("%s: missing required section '%s'" % (label, section))

    rows = _RE_ROW.findall(text)
    if not rows:
        errors.append("%s: no parseable rows in Category Scores table" % label)
    else:
        wsum, total = 0.0, 0.0
        for name, sc, wt in rows:
            w = float(wt)
            wsum += w
            if sc not in ("—", "-"):
                total += float(sc) * w / 100.0
        if abs(wsum - 100.0) > 1.0:
            errors.append("%s: table weights sum to %.1f%%, expected 100%%"
                          % (label, wsum))
        mw = _RE_WTOTAL.search(text)
        if mw and abs(float(mw.group(1)) - total) > MATH_TOL:
            errors.append("%s: stated weighted total %.2f != table math %.2f"
                          % (label, float(mw.group(1)), total))
        mp = _RE_PTOTAL.search(text)
        if score is not None and (mw or mp):
            pen = float(mp.group(1)) if mp else 0.0
            wt = float(mw.group(1)) if mw else total
            if abs(score - (wt - pen)) > MATH_TOL:
                errors.append("%s: score %.2f != weighted total %.2f - penalty %.2f"
                              % (label, score, wt, pen))

    if status and score is not None and threshold is not None:
        if status == "PASS" and score < threshold:
            errors.append("%s: Status PASS but score %.2f < threshold %.2f"
                          % (label, score, threshold))
        if status == "REWORK REQUIRED" and score >= threshold:
            errors.append("%s: Status REWORK REQUIRED but score %.2f >= threshold %.2f"
                          % (label, score, threshold))
    if status == "PASS" and _RE_CRIT.search(text):
        errors.append("%s: Status PASS but an unresolved [CRITICAL] problem is listed"
                      % label)

    mm = _RE_JSON_BLOCK.search(text)
    if mm:
        try:
            doc = json.loads(mm.group(1))
            je, jw = validate_json_doc(doc, label + " (embedded json)")
            errors.extend(je)
            warnings.extend(jw)
        except json.JSONDecodeError as exc:
            errors.append("%s: embedded ```json block does not parse: %s"
                          % (label, exc))
    else:
        warnings.append("%s: no embedded ```json result block found" % label)

    return errors, warnings


def validate_report_file(path):
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError as exc:
        return ["%s: cannot read: %s" % (path, exc)], []
    return validate_report_text(text, str(path))


# --------------------------------------------------------------------------
# Reporting / CLI
# --------------------------------------------------------------------------

def report_result(label, errors, warnings):
    for e in errors:
        print("  ERROR   %s" % e)
    for w in warnings:
        print("  WARNING %s" % w)
    if errors:
        print("FAIL  %s (%d error%s, %d warning%s)"
              % (label, len(errors), "s" if len(errors) != 1 else "",
                 len(warnings), "s" if len(warnings) != 1 else ""))
    else:
        print("OK    %s (%d warning%s)"
              % (label, len(warnings), "s" if len(warnings) != 1 else ""))
    return not errors


def self_test():
    print("ScreenshotSkill validator self-test")
    print("=" * 60)
    all_ok = True

    fixtures = sorted((ROOT / "tests" / "fixtures").glob("*.json"))
    if not fixtures:
        print("ERROR: no fixtures found under tests/fixtures")
        return 1
    for f in fixtures:
        expect_ok = f.name.startswith("valid-")
        errors, warnings = validate_json_file(f)
        passed = (not errors) == expect_ok
        marker = "expected %s" % ("pass" if expect_ok else "fail")
        print("- %s (%s)" % (f.name, marker))
        if errors:
            for e in errors:
                print("    %s" % e)
        if warnings and expect_ok:
            for w in warnings:
                print("    warning: %s" % w)
        if not passed:
            print("  UNEXPECTED RESULT -> self-test failure")
            all_ok = False

    examples = sorted((ROOT / "assets" / "examples").glob("*.md"))
    if not examples:
        print("ERROR: no example reports found under assets/examples")
        return 1
    for f in examples:
        errors, warnings = validate_report_file(f)
        print("- %s (example report, expected pass)" % f.name)
        report_result("    ", errors, warnings)
        if errors:
            all_ok = False

    schema_ok = True
    try:
        load_schema()
    except Exception as exc:  # noqa: BLE001 - surface any schema load problem
        print("ERROR: schema file does not load: %s" % exc)
        schema_ok = False
        all_ok = False

    print("=" * 60)
    print("SELF-TEST %s" % ("PASSED" if (all_ok and schema_ok) else "FAILED"))
    return 0 if (all_ok and schema_ok) else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", nargs="*", help="result JSON files (or .md with --report)")
    ap.add_argument("--report", action="store_true",
                    help="treat FILEs as markdown verification reports")
    ap.add_argument("--schema-only", action="store_true",
                    help="skip consistency rules (JSON validation only)")
    ap.add_argument("--self-test", action="store_true",
                    help="validate all fixtures and example reports")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()
    if not args.files:
        ap.error("provide files or --self-test")

    ok = True
    for name in args.files:
        print("%s:" % name)
        if args.report or name.endswith(".md"):
            errors, warnings = validate_report_file(name)
        else:
            errors, warnings = validate_json_file(name, schema_only=args.schema_only)
        ok &= report_result(name, errors, warnings)
        print()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
