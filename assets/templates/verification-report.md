<!--
  ScreenshotSkill — Visual Verification Report template.
  Copy this file per evaluation (one report per iteration) and replace every {{placeholder}}.
  Parser note: scripts/validate_verification.py --report expects the exact heading text,
  the "Status:", "Score:", "Threshold:", "Iteration:", "Weighted total:", and
  "Penalty total:" lines, and a Category Scores table with "X/10" scores and "NN%" weights.
-->
# Visual Verification Report

**Asset:** {{asset name or short description}}
**Task:** {{quote or tight paraphrase of the original user request}}
**Evidence level:** {{Level 1 — screenshot only | Level 2 — screenshot + model data}}
**Views analyzed:** {{e.g. single three-quarter render | front, side, rear, three-quarter}}
**References used:** {{count + what each supports | none — external research unavailable/not needed}}

## Result

Status: {{PASS | REWORK REQUIRED}}
Score: {{X.X}} / 10
Threshold: {{7.0 unless the task overrides}}
Iteration: {{N}} / {{M}}
Previous score: {{X.X | none — first evaluation}}
Score delta: {{+X.X | −X.X | n/a}}
Weighted total: {{X.XX}}
Penalty total: {{X.XX}}

## Scoring Weights

{{Default weights | Custom weights — table + justification | Reference Similarity not evaluable — weight redistributed; show effective weights}}

## Category Scores

| Category | Score | Weight | Evidence |
|---|---:|---:|---|
| Silhouette | {{X.X}}/10 | {{NN}}% | {{one-line visible evidence}} |
| Proportions | {{X.X}}/10 | {{NN}}% | {{...}} |
| Structure | {{X.X}}/10 | {{NN}}% | {{...}} |
| Geometry | {{X.X}}/10 | {{NN}}% | {{...}} |
| Materials | {{X.X}}/10 | {{NN}}% | {{...}} |
| Reference Similarity | {{X.X}}/10 or — | {{NN or 0}}% | {{cite reference(s), or "not evaluable"}} |
| Style | {{X.X}}/10 | {{NN}}% | {{...}} |
| Composition | {{X.X}}/10 | {{NN}}% | {{...}} |

## What Is Working

- {{concrete positive observation — so fixes preserve it}}

## Problems

### [{{CRITICAL|HIGH|MEDIUM|LOW}}] {{short title}}
- **Evidence:** {{labeled OBSERVED / INFERRED / REFERENCE-SUPPORTED}}
- **Affected area:** {{where on the asset/frame}}
- **Likely cause:** {{INFERRED cause}}
- **Recommended fix:** {{specific, actionable, universal operations with relative magnitude}}
- **Status:** {{unresolved | addressed | verified_fixed}}

{{repeat per problem, ordered by repair priority; omit the section only on a clean PASS}}

## Penalties (if any)

- {{issue}}: −{{X.XX}} — {{why this is not double-counting a category deduction}}
- **Penalty total:** −{{X.XX}} (cap 3.00)

## Reference Comparison

### Observed
{{facts directly visible in the render}}

### Reference-supported
{{claims backed by named references — cite each}}

### Inferred
{{reasoned claims that may be wrong — say why}}

### Differences
{{render vs reference/task, one bullet per difference with severity}}

## Required Changes

1. {{change — specific, measurable in relative units, in the repair-priority order of SKILL.md §8}}

## Verification Decision

{{PASS — rationale, surviving issues | REWORK REQUIRED — top fixes and next action: modify and re-render (iteration N+1/M)}}

```json
{{machine-readable result conforming to schemas/visual-verification.schema.json}}
```
