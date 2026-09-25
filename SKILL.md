---
name: ScreenshotSkill
description: Visually inspect, verify, score, diagnose, and iteratively improve AI-generated visual output — 3D models, low-poly assets, game assets, characters, environments, game scenes, buildings, vehicles, props, terrain, vegetation, procedural assets, UI, renders, and animation frames — through a screenshot-driven CREATE → RENDER → OBSERVE → COMPARE → SCORE → DIAGNOSE → FIX → RE-RENDER loop with weighted 0–10 scoring and a 7.0 acceptance threshold. Software-independent (Blender, Maya, 3ds Max, Houdini, Cinema 4D, Unreal, Unity, Godot, Three.js, OpenSCAD, procedural generators, AI image/model generators, or unknown tools). Sub-agents optional, never required.
---

# ScreenshotSkill

Visual quality control for AI-generated visual output.

> **Why this skill exists:** a model that opens successfully, has valid geometry, the
> correct file format, and the correct polygon count can still *look wrong*. Technical
> success is not visual correctness. ScreenshotSkill catches the failures that file
> validators cannot see.

## Golden rules (never violated)

1. **Never accept on first impression.** Actively hunt for visible problems; do not wait for them to be noticed.
2. **Never claim evidence you do not have.** Say "Insufficient visual evidence" or "Area not visible" instead of guessing. (→ `references/evidence-and-confidence.md`)
3. **Never inflate the score.** Score the visible result against the requested target — never effort, loadability, or the fact that you made it. (→ §12)
4. **Never re-score a stale screenshot.** Every new score requires a *new* render produced *after* a modification.
5. **Bounded iteration.** Default max 5 iterations. Stop conditions are mandatory, not advisory. (→ §9)
6. **Fixed threshold.** Default acceptance threshold is **7.0 / 10**. A PASS also requires **zero unresolved CRITICAL problems**.

---

## 1. When to activate

Activate whenever the task involves producing or judging something that must *look* correct:

- A 3D model, low-poly asset, character, environment, building, vehicle, prop, terrain, vegetation, or procedural asset was generated and can be rendered or screenshotted.
- A game scene, level, or UI was assembled and a screenshot/frame is available.
- An image or render was AI-generated and must match a description or reference.
- Animation frames are available and motion correctness matters (sample frames; → `references/multi-screenshot.md`).
- The user asks to verify, compare, review, QA, or "check" a visual result.

Do **not** activate for purely non-visual work (logic, audio, text) except to verify that its visual *presentation* (e.g., a rendered chart or UI) is correct.

## 2. The core loop

```
CREATE → RENDER / SCREENSHOT → OBSERVE → UNDERSTAND → FIND REFERENCES
→ COMPARE → SCORE → DIAGNOSE → MODIFY → RENDER AGAIN → VERIFY AGAIN → ACCEPT
```

You are *both* inspector and fixer unless sub-agents are available (§11). Analysis
without modification authority is still useful — produce the report and concrete fixes
for whoever/whatever applies them.

## 3. Inputs — intake checklist

Accept any subset of:

| Input | How to use it |
|---|---|
| Screenshot(s) / render(s) | Primary evidence. Run the image-quality pre-check below first. |
| Reference image(s) | Comparison target. Record what each reference supports. |
| Text description / original task | The compliance contract. Quote it in the report. |
| Model/scene information | Elevates you to Evidence Level 2 (exact dimensions, topology, hierarchy). |
| Screen recording / video | Sample frames (start, middle, end, and 2–4 random frames). Treat each as a screenshot; also check temporal artifacts. |
| Before/after screenshots | Regression evidence (§9). |
| User evaluation criteria | Overrides default weights/threshold if stricter; document the change. |

**Image-quality pre-check (do this before any analysis):**
- Is the subject large enough in frame to inspect (ideally 60–80% of frame)?
- Is the image sharp enough to judge edges and materials?
- Is the subject cropped, occluded, or rendered against a same-value background?
- Is lighting bright enough to see form, without blown highlights?

If the pre-check fails → **stop and request a better capture** (view list and framing
guidance in `references/multi-screenshot.md`). Set `next_action` to
`request_more_evidence`. Do not guess from a bad image.

If **no reference image exists**, still evaluate: task compliance, visual quality,
proportions, composition, materials, lighting, technical visual problems, and internal
consistency. Mark Reference Similarity *not evaluable* and redistribute its weight (§7).

## 4. Evidence discipline

Two evidence levels — never claim Level 2 facts from Level 1 evidence:

- **Level 1 — screenshot only:** visible silhouette, approximate proportions and ratios, materials/colors, composition, *visible* intersections and artifacts, style, reference similarity.
- **Level 2 — screenshot + model data:** additionally exact dimensions, triangle counts, topology, transforms, hidden intersections, material parameters, bounding boxes, hierarchy.

Label every claim. Use exactly these labels:

| Label | Meaning |
|---|---|
| **OBSERVED** | Directly visible in the provided evidence. |
| **INFERRED** | Reasoned from observations; may be wrong. |
| **REFERENCE-SUPPORTED** | Backed by a named reference; cite which one. |
| **RECOMMENDED** | A proposed change, not a finding. |

Banned claims from screenshots alone: exact real-world dimensions (ratios are OK),
hidden/inside geometry, topology quality you cannot see, backside correctness. Use
"Visible evidence suggests…" for Level 1 geometry suspicions.
Full rules: `references/evidence-and-confidence.md`.

## 5. The ten inspection lenses

Run all ten on every evaluation. Details, failure signatures, and per-lens questions:
`references/visual-analysis.md`.

1. **Silhouette** — outline, recognizability, masses, negative space, proportions of the outline itself, unnatural symmetry (mandatory for organics).
2. **Proportions** — height/width/depth, component ratios, spacing, scale relationships. Compare as *ratios*, never absolute pixels.
3. **Structure** — primary / secondary / tertiary forms, hierarchy, missing or misplaced components.
4. **Geometry** — visible breakage: intersections, floating parts, holes, z-fighting, clipping, duplicates, bad shading. Classify intersections 1–5 (§5a).
5. **Materials** — identity, roughness/metallic appearance, color, separation, consistency. Don't confuse lighting faults with material faults.
6. **Lighting** — readability, crushed blacks, blown highlights, flatness, shadows hiding geometry.
7. **Composition** — camera angle, framing, subject visibility, hierarchy, background noise.
8. **Style** — match to the *requested* style (low-poly, realistic, stylized, hand-painted, game-ready…).
9. **Reference similarity** — silhouette, proportions, characteristic features, color, arrangement vs references.
10. **Task compliance** — does it actually satisfy the original request?

### 5a. Intersection / overlap classification

Classify every visible intersection:

1. **No intersection** 2. **Intentional contact** 3. **Acceptable shallow overlap** 4. **Suspicious overlap** 5. **Severe intersection**

For clustered masses (foliage, rocks, clouds): shallow overlap is acceptable, deep
penetration must usually be corrected, and visible gaps inside a mass meant to read as
one object must be closed. Geometry-error catalog with severity guidance and fixes:
`references/geometry-errors.md`. Organic-asset specifics (designed irregularity vs
mathematical symmetry vs random noise): `references/organic-assets.md`.

## 6. Reference research

Search the web for references when it can inform proportions, identity, construction,
materials, or style — i.e., almost always for real-world objects.

- Target **object identity, proportions, characteristic features, silhouette, materials, construction, type/species**, not "images that look similar."
- Use **3–6 references**; never treat one image as truth; reconcile disagreements between references explicitly.
- Record which reference supports which conclusion (REFERENCE-SUPPORTED label, with source).
- Prefer authoritative sources for factual dimensions/specs (manufacturer data, official docs).
- Query templates and per-asset-class checklists: `references/reference-research.md`.
- **No web access?** Continue with supplied references and internal knowledge, and state in the report that external verification was unavailable (lower confidence, not lower standards).

## 7. Scoring (0–10, weighted — never arbitrary)

Category scores are 0–10 (0.5 steps). Default weights:

| Category | Weight |
|---|---:|
| Silhouette | 20% |
| Proportions | 15% |
| Structure / completeness | 15% |
| Geometry quality | 10% |
| Materials / colors | 10% |
| Reference similarity | 15% |
| Style consistency | 10% |
| Composition / readability | 5% |

**Formula:** `final_score = round_to_1dp( clamp( Σ(category × weight) − total_penalty, 0, 10 ) )`

- **Custom weights** are allowed when the task demands it (character → anatomy/proportions; game scene → composition; reference reconstruction → similarity). Always state custom weights and *why*.
- **Not-evaluable categories** (e.g., no reference available): redistribute their weight proportionally over the remaining categories and show the effective weights.
- **Critical-issue penalties** (0.25–1.5 points each, **total cap 3.0**): apply for cross-cutting visible failures — wrong object identity, severe silhouette failure, missing reference-defining feature, severe intersection, floating/broken parts, major clipping, severe artifacts. Never double-count: if a problem already dragged a category down, a penalty is justified only for its cross-category severity, and must be explained.
- **Hard rule:** wrong object identity → automatic REWORK, score capped at 2.9.
- Anchors, worked math, and inflation traps: `references/scoring.md`.

## 8. Diagnose and plan fixes (repair priority)

When score < threshold, fix in this order — never polish details while structure is broken:

1. Wrong object / major task failure
2. Major silhouette failure
3. Major proportion failure
4. Missing major components
5. Severe intersections / clipping
6. Structural problems
7. Material / color problems
8. Style inconsistencies
9. Small details
10. Cosmetic polish

Every fix must be **specific and actionable**, in universal operations (§13), with
relative magnitudes when absolute units are unavailable.

- Bad: "Make it better."
- Good: "Move the upper-right foliage mass 0.25–0.4 crown radii outward and rotate it 10–20° so the crown no longer forms a radial ring."

**Rebuild trigger:** if silhouette or proportions still fail after 2 targeted fix
attempts, rebuild the primary forms instead of stacking patches
(→ `references/iteration-loop.md`).

## 9. Iterate — bounded loop with regression check

```
iteration = 1
loop:
    inspect screenshot → identify problems → prioritize (§8)
    → propose specific fixes → modify → RENDER AGAIN
    → inspect NEW screenshot → score again
    → regression check (below)
    stop when: score >= threshold AND no unresolved CRITICAL
            OR iteration == max_iterations (default 5)
            OR required tools/evidence are unavailable
            OR plateau (two consecutive deltas <= +0.2 with the same top problem)
    iteration += 1
```

**Regression check on every new render** — compare against the previous screenshot and record `previous_score`, `score`, `score_delta`:

- Did silhouette / proportions actually improve?
- Did the fix introduce a *new* problem (broken contact, new intersection, new symmetry)?
- Did one problem get fixed while another got worse? (Track per-problem status: `unresolved` / `addressed` / `verified_fixed`.)

Never assume a modification helped. A negative or zero delta requires a *different*
diagnosis, not a reapplied fix. Full loop rules, oscillation and plateau handling:
`references/iteration-loop.md`.

## 10. Accept or reject

- **PASS** ⇔ `score ≥ 7.0` (or the task's stricter threshold) **and** zero unresolved CRITICAL problems. Even then, record surviving MEDIUM/LOW issues honestly.
- Otherwise **REWORK REQUIRED** with prioritized, specific changes.
- At max iterations without passing: report the best iteration, the blocking problems, and `escalate_to_user` — never declare victory by exhaustion.

## 11. Sub-agents (OPTIONAL — never a dependency)

First, **infer delegation capability from the host environment** (documented
task/sub-agent/delegate tools). Never assume writing instructions for a sub-agent
means one will run. If capability is unknown, assume it is **absent**.

**With delegation** (contracts and merge rules: `references/sub-agents.md`):

```
MAIN AGENT (orchestrates, modifies, re-renders)
 ├─ Visual Inspection Agent      → first-pass findings per lens
 ├─ Reference Research Agent     → sourced references + extracted facts
 ├─ Geometry/Structure QA Agent  → intersections, missing parts, structure
 ├─ Style/Composition Agent      → style match, framing, readability
 └─ Final Judge                  → merges findings, dedupes, scores independently
```

**Without delegation:** perform every role yourself, in the same order; the loop is
identical. Do not skip lenses because you are solo.

## 12. Anti-gaming rules (score integrity)

1. Score the **visible result vs the requested target** — never effort, never loadability, never "it has the right poly count."
2. A category average must never hide a critical failure: any unresolved CRITICAL blocks PASS regardless of total.
3. Never re-evaluate the same unchanged screenshot and call it a new iteration.
4. A score may rise only with new render evidence — cite exactly what visibly changed.
5. Never compare the output against your own previous output instead of the task/references (no goalpost moving).
6. Do not redefine or soften the task to match what was produced.
7. If evidence is insufficient, lower **confidence**, never **standards**.
8. Explain every penalty; penalties must be non-duplicative and within the cap.
9. 9–10 is reserved for near-flawless work; justify any score ≥ 9 explicitly.

## 13. Software independence

Speak in **universal operations** — never tool-specific commands — in analysis and fix
plans: move, rotate, scale, duplicate, instance, mirror, deform, extrude, inset, bevel,
merge, delete, reshape, assign material, change color, change topology, adjust camera,
render, screenshot.

If a host environment needs tool-specific commands, keep them in optional per-tool
adapters (an `adapters/` directory you may add downstream). The core skill must stay
tool-agnostic.

## 14. Multi-screenshot and video

Combine all views into **one** mental model — different cameras are not different
objects. Flag contradictions between views explicitly. Recommended view sets per asset
class, contradiction handling, and frame sampling for video:
`references/multi-screenshot.md`.

## 15. Missing tools or evidence

If you cannot render/screenshot at all, say so and produce the best static review
possible from available evidence with `next_action: abort` (or
`request_more_evidence`). Never simulate, assume, or fabricate a screenshot's
contents.

## 16. Outputs (required every evaluation)

1. **Markdown report** using `assets/templates/verification-report.md` — Result, Category Scores table, What Is Working, Problems (severity/evidence/area/cause/fix), Reference Comparison (Observed / Reference-supported / Inferred / Differences), Required Changes, Verification Decision.
2. **Machine-readable JSON** conforming to `schemas/visual-verification.schema.json`. Validate with `scripts/validate_verification.py` when a runtime is available.

Worked examples (tree, vehicle, character, game scene, UI screen, animation frames): `assets/examples/`.

---

## File map

| Path | Purpose |
|---|---|
| `SKILL.md` | This operational instruction (read first). |
| `README.md` | Human-facing overview and usage. |
| `schemas/visual-verification.schema.json` | JSON contract for machine-readable results. |
| `references/visual-analysis.md` | The ten lenses in depth + intersection classes. |
| `references/scoring.md` | Score anchors, weights, penalties, worked math. |
| `references/reference-research.md` | How to find, triangulate, and cite references. |
| `references/organic-assets.md` | Irregularity rules for trees, rocks, terrain, creatures. |
| `references/geometry-errors.md` | Visible geometry error catalog + fixes. |
| `references/composition.md` | Camera, framing, readability, UI capture guidance. |
| `references/iteration-loop.md` | Loop rules, regression, plateau, oscillation, rebuild. |
| `references/evidence-and-confidence.md` | Evidence levels, claim labels, banned claims. |
| `references/multi-screenshot.md` | View sets, merging evidence, video frames. |
| `references/sub-agents.md` | Optional delegation architecture and contracts. |
| `assets/templates/verification-report.md` | Fill-in report template. |
| `assets/examples/*.md` | Six worked evaluations. |
| `scripts/validate_verification.py` | Validates JSON results and markdown reports; self-test. |
| `tests/fixtures/*.json` | Valid/invalid fixtures for the validator. |
