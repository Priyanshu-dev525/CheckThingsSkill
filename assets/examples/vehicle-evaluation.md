# Example: 1980s Pickup Truck (multi-view, reference reconstruction, 2 iterations)

Demonstrates: multi-screenshot evaluation merged into one model, custom weights for
a reference-reconstruction task, a floating-part penalty, contradiction handling
between views, and specification-anchored proportions. Evidence Level 1.

---

# Visual Verification Report

**Asset:** 1980s American full-size pickup truck, regular cab, long bed, game-ready
**Task:** "Model a mid-1980s American full-size pickup, regular cab with the long (8 ft) bed, lightly stylized but proportionally accurate to the real truck."
**Evidence level:** Level 1 — screenshot only
**Views analyzed:** front, left side, rear, ¾ front (4 views, merged)
**References used:** 4 — F-Series seventh-generation overview (specs/variants); era brochure side profile (proportion ratios); rear three-quarter photo set (bed/cab relationship); front fascia photo (grille + quad headlights)

## Result

Status: REWORK REQUIRED
Score: 6.2 / 10
Threshold: 7.0
Iteration: 1 / 5
Previous score: none — first evaluation
Score delta: n/a
Weighted total: 6.48
Penalty total: 0.25

## Scoring Weights

Custom weights (reference-reconstruction preset): silhouette 20%, proportions 20%,
structure 15%, geometry 10%, materials 5%, reference similarity 20%, style 5%,
composition 5%. Justification: the brief is "proportionally accurate to the real
truck", so proportions and reference similarity carry the task; materials and style
are deliberately light ("lightly stylized").

## Category Scores

| Category | Score | Weight | Evidence |
|---|---:|---:|---|
| Silhouette | 6.5/10 | 20% | Side profile reads as a short-bed pickup; the long-bed rear overhang that defines the requested variant is absent. Frontal and rear silhouettes read correctly. |
| Proportions | 6.0/10 | 20% | Bed:cab length ≈ 1.0:1 observed in side view; reference-supported ≈ 1.35:1 for the 8-ft box regular cab. Wheels ≈ 0.21 of overall length vs reference ≈ 0.24. |
| Structure | 7.0/10 | 15% | Cab, bed, bumpers, grille all present and correctly assembled; both side mirrors missing on all four views. |
| Geometry | 6.5/10 | 10% | Wheels in clean class-2 ground contact in all views; antenna hovers above the right fender with a visible shadow gap (floater); no severe intersections visible. |
| Materials | 7.0/10 | 5% | Paint / chrome / rubber separation reads in all views; glass reads dark but consistent. |
| Reference Similarity | 6.0/10 | 20% | Grille and quad headlights match the era reference; long bed missing (defining feature of the requested variant); mirrors missing; two-box stance correct. |
| Style | 7.0/10 | 5% | Consistent lightly-stylized execution across all parts; no mixed-fidelity components. |
| Composition | 7.5/10 | 5% | Four-view set with consistent scale and neutral light; side view is a true profile (no perspective skew) — good verification material. |

## What Is Working

- Front fascia (grille, quad headlights, bumper) matches the era reference strongly — the truck's identity anchor is right.
- Wheel/ground contact is class 2 in every view; stance is believable.
- Consistent style and clean material separation across the whole vehicle.

## Problems

### [HIGH] Long bed missing — truck is a short-bed
- **Evidence:** OBSERVED — side view bed:cab ≈ 1.0:1, rear overhang short; REFERENCE-SUPPORTED (brochure side profile, spec overview) — long-bed regular cab ≈ 1.35:1 bed:cab, wheel-to-bed-end overhang visually longer.
- **Affected area:** bed, rear quarter.
- **Likely cause:** INFERRED — modeled from a short-bed memory/reference instead of the requested long bed.
- **Recommended fix:** RECOMMENDED — scale bed length ×1.3–1.35 along the wheel axis, extend the frame accordingly, and add the resulting rear overhang; re-check wheelbase:overall-length ratio (target ≈ 0.62 reference range).
- **Status:** unresolved

### [HIGH] Side mirrors missing on both doors
- **Evidence:** OBSERVED — absent in side, front, and ¾ views (3 independent views agree).
- **Affected area:** both front doors.
- **Likely cause:** INFERRED — tertiary part dropped during detail pass.
- **Recommended fix:** RECOMMENDED — add period-correct west-coast style mirrors on both doors; attach with class-2 contact to the door skin.
- **Status:** unresolved

### [LOW] Antenna floats above the right fender
- **Evidence:** OBSERVED — shadow gap and air between antenna base and fender in the ¾ and side views (2 views agree).
- **Affected area:** right front fender.
- **Likely cause:** INFERRED — antenna placed to a remembered fender position before fender reshaping.
- **Recommended fix:** RECOMMENDED — move antenna down to class-2 contact on the fender crown.
- **Status:** unresolved

## Penalties (if any)

- Floating part (antenna): −0.25 — a small but damning defect that Geometry's 10% weight only dents; no category double-count (silhouette unaffected, structure unaffected).
- **Penalty total:** −0.25 (cap 3.00)

## Reference Comparison

### Observed
Short-bed stance; wheels ≈ 0.21 of length; correct fascia; correct cab; no mirrors; floating antenna; clean ground contact.

### Reference-supported
Requested long-bed variant: bed:cab ≈ 1.35:1 (brochure); wheels ≈ 0.24 of length (brochure); west-coast mirrors standard equipment; grille/quad-headlight arrangement matches the model exactly.

### Inferred
The wheelbase itself may also be short — side view suggests it, but perspective in the ¾ is inconclusive; re-measure after the bed extension.

### Differences
- Bed length (HIGH) · Rear overhang (HIGH, coupled to bed) · Mirrors (HIGH) · Wheel ratio (MEDIUM, coupled to bed).

## Required Changes

1. Extend bed and frame as specified above (priority 1 — this changes the variant identity).
2. Add both side mirrors with class-2 door contact.
3. Seat the antenna on the fender.
4. Re-render all four views at identical scale and re-evaluate (bed fix may expose a hidden wheelbase error — see Inferred note).

## Verification Decision

REWORK REQUIRED — the wrong-bed variant fails "proportionally accurate to the real truck" for the requested configuration. Next action: modify and re-render (iteration 2/5). Watch the coupled wheelbase question.

```json
{
  "schema_version": "1.0",
  "asset": "1980s American full-size pickup, regular cab long bed",
  "task_summary": "Model a mid-1980s American full-size pickup, regular cab with the long (8 ft) bed, lightly stylized but proportionally accurate to the real truck.",
  "status": "rework_required",
  "score": 6.2,
  "threshold": 7.0,
  "iteration": 1,
  "max_iterations": 5,
  "evidence_level": "level_1_screenshot_only",
  "views_analyzed": ["front", "left side", "rear", "three-quarter front"],
  "categories": {
    "silhouette": 6.5,
    "proportions": 6.0,
    "structure": 7.0,
    "geometry": 6.5,
    "materials": 7.0,
    "reference_similarity": 6.0,
    "style": 7.0,
    "composition": 7.5
  },
  "weights": {
    "silhouette": 0.20,
    "proportions": 0.20,
    "structure": 0.15,
    "geometry": 0.10,
    "materials": 0.05,
    "reference_similarity": 0.20,
    "style": 0.05,
    "composition": 0.05
  },
  "custom_weights_rationale": "Reference-reconstruction task: brief demands proportional accuracy to the real truck, so proportions (.20) and reference similarity (.20) lead; materials and style are deliberately light per 'lightly stylized'.",
  "penalties": [
    {
      "issue": "Floating antenna above right fender",
      "points": 0.25,
      "rationale": "Small, discrete visible defect that Geometry's reduced 10% weight cannot price; no other category is affected, so no double-count."
    }
  ],
  "problems": [
    {
      "severity": "high",
      "category": "reference_similarity",
      "issue": "Long bed missing: truck is a short-bed (bed:cab ~1.0:1 vs requested variant ~1.35:1)",
      "evidence": "OBSERVED: side-view bed:cab ratio ~1.0:1 and short rear overhang; REFERENCE-SUPPORTED (brochure side profile): ~1.35:1 for the 8-ft box regular cab",
      "affected_area": "bed, rear quarter, frame",
      "likely_cause": "modeled from short-bed memory or wrong reference",
      "recommended_fix": "Scale bed length x1.3-1.35 along the wheel axis, extend frame, add rear overhang; re-check wheelbase:overall ~0.62",
      "status": "unresolved"
    },
    {
      "severity": "high",
      "category": "structure",
      "issue": "Both side mirrors missing",
      "evidence": "OBSERVED: absent in side, front, and three-quarter views (3 views agree)",
      "affected_area": "both front doors",
      "likely_cause": "tertiary part dropped in detail pass",
      "recommended_fix": "Add period-correct west-coast mirrors on both doors with class-2 door contact",
      "status": "unresolved"
    },
    {
      "severity": "low",
      "category": "geometry",
      "issue": "Antenna floats above right fender",
      "evidence": "OBSERVED: shadow gap and visible air at the antenna base in 3/4 and side views",
      "affected_area": "right front fender",
      "likely_cause": "antenna placed before fender reshaping",
      "recommended_fix": "Move antenna down to class-2 contact on the fender crown",
      "status": "unresolved"
    }
  ],
  "what_is_working": [
    "Front fascia matches the era reference (grille, quad headlights, bumper)",
    "Class-2 wheel/ground contact in all four views",
    "Consistent lightly-stylized execution and clean material separation"
  ],
  "required_changes": [
    "Extend bed length x1.3-1.35 with frame extension and correct rear overhang",
    "Add both west-coast side mirrors (class-2 door contact)",
    "Seat antenna on fender crown",
    "Re-render all four views at identical scale; re-evaluate"
  ],
  "references_used": [
    {
      "title": "Ford F-Series seventh generation overview",
      "url": "https://en.wikipedia.org/wiki/Ford_F-Series_(seventh_generation)",
      "kind": "spec",
      "used_for": "variant lineup (regular cab + 8-ft box exists), era identity, wheelbase class"
    },
    {
      "title": "Era brochure side profile (F-150 regular cab long box)",
      "kind": "photo",
      "used_for": "bed:cab ~1.35:1, wheels ~0.24 of overall length, rear overhang read"
    },
    {
      "title": "Rear three-quarter photo set",
      "kind": "photo",
      "used_for": "bed/cab relationship and bed-side height"
    },
    {
      "title": "Front fascia photo",
      "kind": "photo",
      "used_for": "grille and quad-headlight arrangement"
    }
  ],
  "confidence_notes": "Level 1: ratios only, no absolute dimensions. Four merged views agree on all reported observations; the wheelbase question is occlusion-limited and flagged as Inferred.",
  "next_action": "modify_and_rerender"
}
```

---

# Visual Verification Report

**Asset:** 1980s American full-size pickup truck, regular cab, long bed, game-ready
**Task:** "Model a mid-1980s American full-size pickup, regular cab with the long (8 ft) bed, lightly stylized but proportionally accurate to the real truck."
**Evidence level:** Level 1 — screenshot only
**Views analyzed:** front, left side, rear, ¾ front (same 4 views, same scale — regression pair)
**References used:** same 4 references as iteration 1

## Result

Status: PASS
Score: 7.6 / 10
Threshold: 7.0
Iteration: 2 / 5
Previous score: 6.2
Score delta: +1.4
Weighted total: 7.60
Penalty total: 0.00

## Scoring Weights

Custom weights (unchanged from iteration 1 — reference-reconstruction preset).

## Category Scores

| Category | Score | Weight | Evidence |
|---|---:|---:|---|
| Silhouette | 8.0/10 | 20% | Side profile now carries the long-bed two-box read with the correct rear overhang; identity holds in thumbnail test. |
| Proportions | 8.0/10 | 20% | Bed:cab ≈ 1.32:1 (target 1.35:1 band); wheels ≈ 0.23 of length; wheelbase question resolved — no hidden error surfaced after the bed extension. |
| Structure | 7.5/10 | 15% | All components present including both mirrors; fuel cap and tailgate hardware land in plausible positions. |
| Geometry | 7.0/10 | 10% | Antenna seated class 2; wheels class 2; visible evidence suggests shallow (class 3) front-bumper/frame overlap plus the new rear-tire texture stretch — acceptable, disclosed below. |
| Materials | 7.0/10 | 5% | Separation unchanged; window glass fractionally darker than reference photos but consistent across views. |
| Reference Similarity | 7.5/10 | 20% | Long bed, overhang, mirrors and stance now match the brochure profile; remaining deltas: mirror arms ~15% slimmer than period parts. |
| Style | 7.0/10 | 5% | Unchanged — consistent lightly-stylized execution. |
| Composition | 7.5/10 | 5% | Identical four-view regression set; framing unchanged. |

## What Is Working

- The bed extension converted the variant identity without disturbing the strong
  front fascia or the wheel/ground contacts (the two biggest regression risks of
  this fix passed cleanly).
- Mirror addition landed in class-2 contact on both doors, matching period photos.

## Problems

### [LOW] Tire sidewall texture stretched on rear wheels
- **Evidence:** OBSERVED — sidewall lettering band visibly elongated along the tangent on the rear wheels in side view; fronts are clean.
- **Affected area:** both rear tires.
- **Likely cause:** INFERRED — rear wheels enlarged/mirrored during proportion pass without re-mapping.
- **Recommended fix:** RECOMMENDED — re-map rear tire sidewalls to match front texture density.
- **Status:** unresolved

## Reference Comparison

### Observed
Bed:cab 1.32:1; rear overhang present; both mirrors in class-2 contact; antenna seated; crossed-era details absent.

### Reference-supported
Brochure band for bed:cab is ≈1.3–1.4:1 across years — 1.32:1 is inside it; mirror size is the one sub-reference discrepancy (arms slimmer than period photos).

### Inferred
Class-3 bumper/frame overlap may be intentional assembly; without mesh data it reads acceptable.

### Differences
- Mirror arm thickness (LOW) · Rear tire texture (LOW, task-internal, not reference).

## Required Changes

None — score meets threshold with zero unresolved CRITICAL/HIGH. The disclosed LOW items (mirror arms, rear tire texture) are scheduled for a non-blocking polish pass.

## Regression Check

- Long bed: **verified_fixed** — ratio inside reference band; silhouette recovered.
- Mirrors: **verified_fixed** — both doors, both views.
- Floating antenna: **verified_fixed** — class-2 contact in ¾ and side views.
- Wheelbase (Inferred risk from iteration 1): resolved — post-extension measurement matches the reference range; no new proportion fault.
- New problems introduced: rear tire texture stretch (new, caused by the fix) — LOW, disclosed, fix deferred as polish.

## Verification Decision

PASS — 7.6 ≥ 7.0 with zero unresolved CRITICAL/HIGH. One fix-introduced LOW (rear tire texture) is disclosed and scheduled for polish; it does not affect variant identity, proportions, or the requested configuration.

```json
{
  "schema_version": "1.0",
  "asset": "1980s American full-size pickup, regular cab long bed",
  "task_summary": "Model a mid-1980s American full-size pickup, regular cab with the long (8 ft) bed, lightly stylized but proportionally accurate to the real truck.",
  "status": "pass",
  "score": 7.6,
  "threshold": 7.0,
  "iteration": 2,
  "max_iterations": 5,
  "previous_score": 6.2,
  "score_delta": 1.4,
  "evidence_level": "level_1_screenshot_only",
  "views_analyzed": ["front", "left side", "rear", "three-quarter front"],
  "categories": {
    "silhouette": 8.0,
    "proportions": 8.0,
    "structure": 7.5,
    "geometry": 7.0,
    "materials": 7.0,
    "reference_similarity": 7.5,
    "style": 7.0,
    "composition": 7.5
  },
  "weights": {
    "silhouette": 0.20,
    "proportions": 0.20,
    "structure": 0.15,
    "geometry": 0.10,
    "materials": 0.05,
    "reference_similarity": 0.20,
    "style": 0.05,
    "composition": 0.05
  },
  "custom_weights_rationale": "Reference-reconstruction task: proportions (.20) and reference similarity (.20) lead the brief.",
  "penalties": [],
  "problems": [
    {
      "severity": "high",
      "category": "reference_similarity",
      "issue": "Long bed missing (iteration 1)",
      "evidence": "OBSERVED in this render: bed:cab 1.32:1, overhang correct in side and 3/4 views",
      "recommended_fix": "None — freeze this area",
      "status": "verified_fixed"
    },
    {
      "severity": "high",
      "category": "structure",
      "issue": "Side mirrors missing (iteration 1)",
      "evidence": "OBSERVED: both mirrors present in class-2 door contact across views",
      "recommended_fix": "None — freeze this area",
      "status": "verified_fixed"
    },
    {
      "severity": "low",
      "category": "geometry",
      "issue": "Floating antenna (iteration 1)",
      "evidence": "OBSERVED: antenna base seated on fender crown, no shadow gap",
      "recommended_fix": "None — freeze this area",
      "status": "verified_fixed"
    },
    {
      "severity": "low",
      "category": "geometry",
      "issue": "Rear tire sidewall texture stretched (introduced by iteration-2 wheel work)",
      "evidence": "OBSERVED: lettering band elongated tangentially on rear tires only; fronts clean",
      "affected_area": "both rear tires",
      "likely_cause": "rear wheels enlarged without re-mapping",
      "recommended_fix": "Re-map rear sidewalls to match front texture density",
      "status": "unresolved"
    }
  ],
  "what_is_working": [
    "Variant identity recovered: long-bed two-box read inside the brochure band",
    "Front fascia and ground contacts survived the bed fix (regression-safe)",
    "Mirrors landed in class-2 contact matching period photos"
  ],
  "required_changes": [],
  "references_used": [
    {
      "title": "Ford F-Series seventh generation overview",
      "url": "https://en.wikipedia.org/wiki/Ford_F-Series_(seventh_generation)",
      "kind": "spec",
      "used_for": "variant verification"
    },
    {
      "title": "Era brochure side profile (F-150 regular cab long box)",
      "kind": "photo",
      "used_for": "bed:cab band 1.3-1.4:1, wheel ratio, overhang verification"
    },
    {
      "title": "Rear three-quarter photo set",
      "kind": "photo",
      "used_for": "bed/cab relationship verification"
    },
    {
      "title": "Front fascia photo",
      "kind": "photo",
      "used_for": "fascia verification"
    }
  ],
  "confidence_notes": "Level 1; four-view regression set at identical framing. Mirror arm thickness and bumper/frame overlap are the only sub-reference deltas; both disclosed. Rear tire texture issue was introduced by this iteration's fix and is fix-scheduled.",
  "next_action": "accept"
}
```
