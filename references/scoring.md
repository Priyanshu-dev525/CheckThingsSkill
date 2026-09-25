# Scoring — Anchors, Weights, Penalties, Worked Math

The score must be *derivable*, never vibes. Every number in a report must be
reproducible from the category table, the weights, and the penalties.

## Category anchors (0–10, 0.5 steps allowed)

| Band | Meaning |
|---|---|
| 9.0–10 | Near-flawless for the brief; only nitpicks remain. Rare. Justify explicitly. |
| 7.0–8.9 | Good; shippable with minor visible issues properly disclosed. |
| 5.0–6.9 | Recognizable and on-task, but notable visible problems; rework expected. |
| 3.0–4.9 | Major problems; identity survives only partially. |
| 0–2.9 | Wrong object, destroyed silhouette, or unusable output. (Wrong identity caps the whole evaluation at 2.9.) |

Anchor each category score to the band descriptors, not to how much effort the
generation took.

## Default weights

| Category | Weight |
|---|---:|
| Silhouette | 0.20 |
| Proportions | 0.15 |
| Structure / completeness | 0.15 |
| Geometry quality | 0.10 |
| Materials / colors | 0.10 |
| Reference similarity | 0.15 |
| Style consistency | 0.10 |
| Composition / readability | 0.05 |

## Custom weight presets (declare and justify when used)

| Preset | silh. | prop. | struct. | geom. | mat. | ref-sim. | style | comp. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Hard-surface model / prop | .20 | .20 | .15 | .15 | .10 | .10 | .05 | .05 |
| Character / creature (anatomy-first) | .15 | .25 | .15 | .10 | .05 | .10 | .10 | .10 |
| Reference reconstruction (vehicle shown) | .20 | .20 | .15 | .10 | .05 | .20 | .05 | .05 |
| Game scene / environment (readability-first) | .15 | .10 | .20 | .10 | .10 | .15 | .10 | .25* |
| UI screenshot | .05 | .15 | .20 | .05 | .10 | .10 | .10 | .25 |

\* scene preset assumes reference_similarity redistributed to composition when no
reference exists; adjust and state the effective weights.

These are starting points, not a fixed menu. The only hard rules: every weight in
[0,1], weights over evaluated categories sum to 1.00 ± 0.01, differences from
defaults are justified in `custom_weights_rationale`.

## Not-evaluable categories

If a category cannot be evaluated (most commonly `reference_similarity` when no
reference exists and web research is unavailable/inappropriate), remove it, list it in
`not_evaluable`, and redistribute its weight proportionally over the rest:

```
effective_w_i = default_w_i / (1 - w_removed)
```

Round to 2 decimals, then fix rounding drift on the largest weight so the sum is
exactly 1.00. Show effective weights in the report.

## Formula

```
weighted_total = Σ (category_score × effective_weight)
final_score    = round_to_1_decimal( clamp(weighted_total − total_penalty, 0, 10) )
```

## Critical-issue penalties

Penalties punish **cross-cutting** visible failures whose category deductions alone
understate the damage. Size 0.25–1.5 each; **total penalty cap 3.0**. Always state,
per penalty, why it is not double-counting.

| Issue | Typical size |
|---|---|
| Wrong object identity | Automatic REWORK + cap 2.9 (do not also stack penalties to reach the same effect) |
| Severe silhouette failure | 1.0–1.5 |
| Missing reference-defining feature | 0.5–1.0 |
| Severe intersection / deep clipping | 0.5–1.0 |
| Floating / broken parts | 0.25–0.75 |
| Severe visual artifact (z-fighting storm, texture meltdown) | 0.25–1.0 |

Anti double-count example: radial-symmetry foliage already cut Silhouette (20%) and
Structure (15%) hard — an extra penalty would punish it a third time, so none is
applied. A floating antenna, by contrast, is a small but damning defect that category
scores only dent; 0.25 is fair.

## Worked example (tree, iteration 1 — from assets/examples/tree-evaluation.md)

| Category | Score | Weight | Contribution |
|---|---:|---:|---:|
| Silhouette | 4.5 | 0.20 | 0.90 |
| Proportions | 6.0 | 0.15 | 0.90 |
| Structure | 6.5 | 0.15 | 0.975 |
| Geometry | 6.0 | 0.10 | 0.60 |
| Materials | 6.5 | 0.10 | 0.65 |
| Reference similarity | 4.5 | 0.15 | 0.675 |
| Style | 6.5 | 0.10 | 0.65 |
| Composition | 7.5 | 0.05 | 0.375 |

weighted_total = 5.725; penalty 0.50 (severe trunk↔foliage intersection, justified
because Geometry's 0.10 weight cannot price a defect spanning silhouette+materials);
final = round1(5.725 − 0.50) = **5.2** → REWORK.

## Regression numbers

Every iteration after the first records `previous_score`, `score`, `score_delta`.
A delta ≤ +0.2 twice in a row with the same top problem = plateau → stop and change
strategy (see `iteration-loop.md`).

## Inflation traps (self-audit before publishing a score)

- Did I give points because the file loads / the poly count is right? → forbidden.
- Did one CRITICAL hide behind seven decent category scores? → CRITICAL blocks PASS.
- Did the score rise without new render evidence? → forbidden.
- Did I compare against my own previous output instead of the task/reference?
  → forbidden.
- Is any score ≥ 9.0 explicitly justified? → required.
- Did insufficient evidence lower my *standards* instead of my *confidence*?
  → wrong direction.
