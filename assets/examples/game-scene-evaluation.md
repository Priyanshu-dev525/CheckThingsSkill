# Example: Floating-Island Game Scene (scene context, first-pass acceptance)

Demonstrates: scene evaluation with readability-first custom weights,
`reference_similarity` marked not-evaluable (imagination-driven scene, no supplied or
sensible web reference) with weight redistribution, a PASS on iteration 1 with
disclosed MEDIUM/LOW issues, and the "PASS may be accepted" rule applied honestly.

---

# Visual Verification Report

**Asset:** Low-poly floating-island game scene (establishing render)
**Task:** "Compose a low-poly floating-island scene with a main island, waterfall, and 3 satellite islands, readable as a game environment establishing shot, stylized pastel palette."
**Evidence level:** Level 1 — screenshot only
**Views analyzed:** single establishing view (the requested deliverable) + one gameplay-camera view supplied for readability
**References used:** none — this is an original composition; `reference_similarity` is not evaluable (no canonical target exists; web search results would be other artists' outputs, not a truth source)

## Result

Status: PASS
Score: 7.6 / 10
Threshold: 7.0
Iteration: 1 / 5
Previous score: none — first evaluation
Score delta: n/a
Weighted total: 7.63
Penalty total: 0.00

## Scoring Weights

Custom weights with redistribution: reference_similarity removed and its weight
redistributed over scene-relevant categories. Effective weights: silhouette 15%,
proportions 10%, structure 20%, geometry 10%, materials 10%, reference similarity 0%
(not evaluable), style 10%, composition 25%. Justification: the brief is a scene
"readable as a game environment establishing shot" — composition/readability leads;
structure follows because the task lists a specific part inventory.

## Category Scores

| Category | Score | Weight | Evidence |
|---|---:|---:|---|
| Silhouette | 7.5/10 | 15% | Main island reads as a distinct stepped mass against the sky; satellite islands separate clearly; waterfall anchors the main mass visually. |
| Proportions | 8.0/10 | 10% | Main:satellite scale ratio reads ~3:1 and ~4:1 — a convincing island hierarchy; perspective diminution consistent between near and far satellites. |
| Structure | 7.5/10 | 20% | Brief's inventory fully present: main island, waterfall, exactly 3 satellites, vegetation, bridge elements; no unrequested focal elements. |
| Geometry | 7.0/10 | 10% | Visible evidence suggests shallow class-3 overlaps where rock plates meet the grass caps — acceptable for clusters; one foreground grass tuft row repeats an identical rotation (see Problems). |
| Materials | 7.5/10 | 10% | Grass/rock/water/cloud families separate cleanly in greyscale; pastel palette matches the brief. |
| Reference Similarity | — | 0% | Not evaluable — no canonical reference for an original scene; declared in the header and Notes. |
| Style | 7.5/10 | 10% | Consistent faceted low-poly across all islands; clouds slightly softer than the rest but inside the stylized band. |
| Composition | 8.0/10 | 25% | Clear focal point on the main island (value contrast + waterfall leading line); foreground/midground/background separate at 25% scale; horizon off-center. |

## What Is Working

- Focal structure works: at 25% shrink the eye still lands on the main island first
  (squint test passed); the waterfall doubles as a leading line.
- Task inventory exact — main island + waterfall + exactly 3 satellites, no more.
- Value grouping separates the three depth planes without atmospheric band aid.

## Problems

### [MEDIUM] Background satellite competes with the focal island
- **Evidence:** OBSERVED — the rightmost satellite's rock underside is nearly the same value as the main island's, and its size is ~55% of the main island; at 25% shrink the eye flickers between them.
- **Affected area:** right-mid background.
- **Likely cause:** INFERRED — satellites authored at similar value/saturation as the hero without depth-falloff grading.
- **Recommended fix:** RECOMMENDED — desaturate and lighten the rightmost satellite ~15–20% toward the sky value, or shrink it to ≤40% of the main island.
- **Status:** unresolved

### [LOW] Foreground grass tufts repeat one rotation
- **Evidence:** OBSERVED — 6 foreground tufts at the lower edge share an identical lean angle, reading as copy-paste at full size.
- **Affected area:** foreground frame edge.
- **Likely cause:** INFERRED — single tuft instance cloned along the edge.
- **Recommended fix:** RECOMMENDED — rotate tufts with ±15–25° yaw jitter and vary scale 0.8–1.3×.
- **Status:** unresolved

## Reference Comparison

### Observed
Main island with stepped grass/rock masses, waterfall at its right edge, 3 satellites at varied depths, consistent faceted low-poly, pastel palette, clear three-plane value separation.

### Reference-supported
None — no external references used; this section intentionally records that.

### Inferred
The rightmost satellite's competition with the hero island would likely also read as a distraction at gameplay camera distances — confidence medium; the supplied gameplay view weakens but does not eliminate the concern.

### Differences
Scene-vs-brief deltas only: none in inventory; focal competition (MEDIUM) and tuft repetition (LOW) are internal-quality issues, not compliance gaps.

## Required Changes

1. (Optional polish, recommended before ship) Grade the rightmost satellite ~15–20% toward sky value or shrink it to ≤40% of the main island.
2. (Optional polish) Jitter foreground tuft rotations ±15–25° and scale 0.8–1.3×.

## Verification Decision

PASS — 7.6 ≥ 7.0 with zero unresolved CRITICAL/HIGH. Two issues disclosed above are polish-level and do not compromise the brief (inventory exact, readability proven at 25% scale, focal structure working). No further iteration required; the two items may be handled in a non-blocking polish pass without re-verification gates, though a spot-check render is advised.

```json
{
  "schema_version": "1.0",
  "asset": "low-poly floating-island game scene",
  "task_summary": "Compose a low-poly floating-island scene with a main island, waterfall, and 3 satellite islands, readable as a game environment establishing shot, stylized pastel palette.",
  "status": "pass",
  "score": 7.6,
  "threshold": 7.0,
  "iteration": 1,
  "max_iterations": 5,
  "evidence_level": "level_1_screenshot_only",
  "views_analyzed": ["establishing view", "gameplay camera"],
  "categories": {
    "silhouette": 7.5,
    "proportions": 8.0,
    "structure": 7.5,
    "geometry": 7.0,
    "materials": 7.5,
    "style": 7.5,
    "composition": 8.0
  },
  "weights": {
    "silhouette": 0.15,
    "proportions": 0.10,
    "structure": 0.20,
    "geometry": 0.10,
    "materials": 0.10,
    "style": 0.10,
    "composition": 0.25
  },
  "custom_weights_rationale": "Readability-first scene brief: composition leads (.25), structure follows (.20) because the task lists a specific inventory. reference_similarity removed (original scene, no canonical target) and its weight redistributed over scene-relevant categories.",
  "not_evaluable": ["reference_similarity"],
  "penalties": [],
  "problems": [
    {
      "severity": "medium",
      "category": "composition",
      "issue": "Rightmost background satellite competes with the focal island (same value family, ~55% of hero size)",
      "evidence": "OBSERVED: at 25% shrink the eye flickers between the right satellite and the main island",
      "affected_area": "right-mid background",
      "likely_cause": "satellites authored at the hero's value/saturation without depth falloff",
      "recommended_fix": "Grade the satellite ~15-20% toward sky value or shrink it to <=40% of the main island",
      "status": "unresolved"
    },
    {
      "severity": "low",
      "category": "geometry",
      "issue": "Six foreground grass tufts share one identical rotation",
      "evidence": "OBSERVED: identical lean angle across the tuft row at the lower frame edge",
      "affected_area": "foreground frame edge",
      "likely_cause": "single tuft instance cloned along the edge",
      "recommended_fix": "Jitter tuft yaw +/-15-25deg and vary scale 0.8-1.3x",
      "status": "unresolved"
    }
  ],
  "what_is_working": [
    "Focal structure proven at 25% shrink; waterfall acts as leading line",
    "Task inventory exact: main island + waterfall + exactly 3 satellites",
    "Three-plane value separation without atmospheric band aid"
  ],
  "required_changes": [
    "Optional polish: grade rightmost satellite ~15-20% toward sky value or shrink to <=40% of main island",
    "Optional polish: jitter foreground tufts +/-15-25deg yaw, scale 0.8-1.3x"
  ],
  "references_used": [],
  "confidence_notes": "reference_similarity not evaluable: original composition with no canonical target; web search would surface other artists' outputs, not truth. Level 1 only. Gameplay-view evidence supports the focal-competition finding at medium confidence. External reference verification was intentionally not used, not unavailable.",
  "next_action": "accept"
}
```
