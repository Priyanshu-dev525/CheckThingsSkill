# Example: Stylized Knight Character (Level 2 evidence, anatomy weights, 2 iterations)

Demonstrates: Level 2 evaluation where model/scene data accompanies the renders,
anatomy-first custom weights, a severe-intersection penalty with an anti-double-count
rationale, and bounds on what Level 2 data may claim.

---

# Visual Verification Report

**Asset:** Stylized knight character, T-pose, full-body
**Task:** "Create a stylized knight character in T-pose, 6.5 heads tall, game-ready low-poly with clean silhouette, for a top-down action game."
**Evidence level:** Level 2 — screenshots + model data (triangle count, bone/mesh hierarchy, component dimensions supplied by the generating pipeline)
**Views analyzed:** front, left side, back (eye-level, full-body)
**References used:** 3 — arm-span/reach anatomy sheet (limb ratios); stylized character proportion exemplar (6.5-head target); medieval plate construction reference (armor layering)

## Result

Status: REWORK REQUIRED
Score: 5.6 / 10
Threshold: 7.0
Iteration: 1 / 5
Previous score: none — first evaluation
Score delta: n/a
Weighted total: 6.08
Penalty total: 0.50

## Scoring Weights

Custom weights (anatomy-first preset): silhouette 15%, proportions 25%, structure
15%, geometry 10%, materials 5%, reference similarity 10%, style 10%, composition
10%. Justification: the task is decided by body ratios ("6.5 heads tall"), so
proportions lead; materials stay light because the brief's material demand is only
"game-ready low-poly".

## Category Scores

| Category | Score | Weight | Evidence |
|---|---:|---:|---|
| Silhouette | 6.5/10 | 15% | Armor masses read against a neutral background, but the short arms make the side silhouette read childlike rather than heroic. |
| Proportions | 5.0/10 | 25% | OBSERVED+DATA: model measured 5.5 heads tall vs 6.5 required; fingertips end at the hip crease vs mid-thigh expectation; head oversized for the brief. |
| Structure | 6.5/10 | 15% | All armor components present (helm, pauldrons, cuirass, greaves); gorget missing between helm and cuirass; pauldrons float (see Geometry). |
| Geometry | 6.0/10 | 10% | DATA: hands intersect the torso deeply (class 5) — fingertips pass ~3.8 cm into the hip plates; left pauldron hovers 1.2 cm above the shoulder; boots clip 0.6 cm below the ground plane. |
| Materials | 6.5/10 | 5% | Steel/leather/cloth separation reads at gameplay distance; edge-wear pass absent but the brief doesn't demand it. |
| Reference Similarity | 6.0/10 | 10% | Anatomy sheet: reach to mid-thigh — model reaches hip crease; exemplar: 6.5-head ratio — model is 5.5; armor layering matches plate reference. |
| Style | 6.5/10 | 10% | Facet budget and flat-shaded look fit; the oversized head reads chibi, conflicting with the heroic exemplar. |
| Composition | 7.0/10 | 10% | Eye-level full-body set at consistent scale; back view slightly underlit, plate read suffers. |

## What Is Working

- Armor layering logic (cuirass over gambeson, pauldrons over shoulder) matches the
  construction reference — the knight reads as *armored*, not as a person in metal
  paint.
- Facet budget consistent across the whole body; no mixed-fidelity parts.
- Review captures follow the character view-set convention.

## Problems

### [HIGH] Body proportions miss the brief: 5.5 heads, not 6.5; short arms
- **Evidence:** OBSERVED — side/front view show head ≈ 1/5.5 of height and fingertips at the hip crease; LEVEL-2 DATA — mesh measures 183 cm total height with a 33 cm head height (5.5:1) and arm span 171 cm.
- **Affected area:** global proportions; arms specifically.
- **Likely cause:** INFERRED — head scaled up for appeal without compensating leg/torso lengths; arms authored to the smaller body.
- **Recommended fix:** RECOMMENDED — scale head 0.92×, lengthen legs ~8% and arms until fingertips reach mid-thigh (≈+6 cm each); re-measure to confirm 6.5:1 after the edit.
- **Status:** unresolved

### [CRITICAL] Hands severely intersect the torso
- **Evidence:** OBSERVED — fingertips visibly disappear into the hip plates in front and side views; LEVEL-2 DATA — maximum penetration 3.8 cm.
- **Affected area:** both hands / hip plates.
- **Likely cause:** INFERRED — arms placed for the pre-resize torso and never re-posed.
- **Recommended fix:** RECOMMENDED — rotate shoulders outward 5–8° and move hands laterally until a 0.3–0.5 cm air gap remains; verify with a fresh intersection pass.
- **Status:** unresolved

### [MEDIUM] Left pauldron floats above the shoulder
- **Evidence:** LEVEL-2 DATA — 1.2 cm gap to the shoulder surface; OBSERVED — shadow gap visible in the side view at full zoom.
- **Affected area:** left shoulder.
- **Likely cause:** INFERRED — pauldron parented before shoulder reshape.
- **Recommended fix:** RECOMMENDED — move pauldron down 1.2 cm into class-2 contact.
- **Status:** unresolved

### [MEDIUM] Boots clip the ground plane
- **Evidence:** OBSERVED — soles sink below the floor line in all three views; LEVEL-2 DATA — 0.6 cm.
- **Affected area:** both boots.
- **Likely cause:** INFERRED — ground plane set after a boot adjustment.
- **Recommended fix:** RECOMMENDED — raise the character 0.6 cm or drop the plane; class-2 contact required.
- **Status:** unresolved

### [LOW] Back view underlit for review
- **Evidence:** OBSERVED — plate read collapses in the back view while front/side read fine.
- **Affected area:** capture, not asset.
- **Likely cause:** INFERRED — single key light used for the review set.
- **Recommended fix:** RECOMMENDED — add a fill light for the back capture only.
- **Status:** unresolved

## Penalties (if any)

- Severe intersection (hands↔torso): −0.50 — Geometry's 10% weight cannot price a class-5 fault that also destroys the T-pose silhouette read; Proportions was *not* charged for this defect, so no double-count.
- **Penalty total:** −0.50 (cap 3.00)

## Reference Comparison

### Observed
Head 1/5.5 of height; fingertips at hip crease; hands inside the torso; pauldron gap; boots below the floor; armor layers correct.

### Reference-supported
Anatomy sheet: fingertips end at mid-thigh in neutral stance. Exemplar: 6.5-head heroic stylized ratio. Plate reference: gambeson→cuirass→pauldron layering, which the model matches.

### Inferred
The chibi-adjacent read comes from head size more than limb mass — fix head scale first, limbs second, and re-inspect before touching mass.

### Differences
- Height ratio 5.5 vs 6.5 (HIGH) · Arm reach (HIGH, coupled) · Gorget missing (LOW→part of structure) · Back-view lighting (LOW, capture).

## Required Changes

1. Separate hands from torso (0.3–0.5 cm gap; CRITICAL first).
2. Rescale head 0.92×; lengthen legs ~8% and arms to mid-thigh; re-measure 6.5:1.
3. Add the gorget; seat the left pauldron; resolve boot/ground clipping.
4. Relight the back view capture and re-render all three views.

## Verification Decision

REWORK REQUIRED — a class-5 intersection and a missed headline spec (6.5 heads) both violate the task contract. Next action: modify and re-render (iteration 2/5). Proportion edits risk breaking everything at the shoulders — re-verify pauldrons, gorget, and hands after the resize.

```json
{
  "schema_version": "1.0",
  "asset": "stylized knight character, T-pose",
  "task_summary": "Create a stylized knight character in T-pose, 6.5 heads tall, game-ready low-poly with clean silhouette, for a top-down action game.",
  "status": "rework_required",
  "score": 5.6,
  "threshold": 7.0,
  "iteration": 1,
  "max_iterations": 5,
  "evidence_level": "level_2_screenshot_plus_model_data",
  "views_analyzed": ["front", "left side", "back"],
  "categories": {
    "silhouette": 6.5,
    "proportions": 5.0,
    "structure": 6.5,
    "geometry": 6.0,
    "materials": 6.5,
    "reference_similarity": 6.0,
    "style": 6.5,
    "composition": 7.0
  },
  "weights": {
    "silhouette": 0.15,
    "proportions": 0.25,
    "structure": 0.15,
    "geometry": 0.10,
    "materials": 0.05,
    "reference_similarity": 0.10,
    "style": 0.10,
    "composition": 0.10
  },
  "custom_weights_rationale": "Character anatomy task with an explicit head-count spec: proportions lead at .25; materials reduced to .05 because the brief's material demand is only game-ready low-poly.",
  "penalties": [
    {
      "issue": "Hands severely intersect torso (class 5, max 3.8 cm penetration)",
      "points": 0.5,
      "rationale": "Geometry's reduced 10% weight cannot price a class-5 fault that also breaks the T-pose silhouette; Proportions was not charged for it, so no double-count."
    }
  ],
  "problems": [
    {
      "severity": "critical",
      "category": "geometry",
      "issue": "Hands severely intersect the torso",
      "evidence": "OBSERVED: fingertips disappear into hip plates in front and side views; LEVEL-2 DATA: max penetration 3.8 cm",
      "affected_area": "both hands / hip plates",
      "likely_cause": "arms placed for the pre-resize torso",
      "recommended_fix": "Rotate shoulders outward 5-8deg and move hands laterally to a 0.3-0.5 cm air gap; re-run intersection check",
      "status": "unresolved"
    },
    {
      "severity": "high",
      "category": "proportions",
      "issue": "Model is 5.5 heads tall vs required 6.5; arms too short (fingertips at hip crease, not mid-thigh)",
      "evidence": "OBSERVED across views; LEVEL-2 DATA: 183 cm height, 33 cm head (5.5:1), arm span 171 cm",
      "affected_area": "global proportions",
      "likely_cause": "head scaled for appeal without leg/torso compensation",
      "recommended_fix": "Scale head 0.92x; lengthen legs ~8% and arms ~+6 cm to mid-thigh; re-measure 6.5:1",
      "status": "unresolved"
    },
    {
      "severity": "medium",
      "category": "geometry",
      "issue": "Left pauldron floats 1.2 cm above the shoulder; boots clip 0.6 cm below ground",
      "evidence": "LEVEL-2 DATA: 1.2 cm and 0.6 cm gaps; OBSERVED: shadow gap at zoom, soles below floor line",
      "affected_area": "left shoulder; both boots",
      "likely_cause": "pauldron parented pre-reshape; ground plane moved after boot edit",
      "recommended_fix": "Lower pauldron 1.2 cm to class-2 contact; raise character 0.6 cm or drop the plane",
      "status": "unresolved"
    },
    {
      "severity": "medium",
      "category": "structure",
      "issue": "Gorget missing between helm and cuirass",
      "evidence": "OBSERVED: neck gap in all three views; REFERENCE-SUPPORTED (plate construction reference): gorget present",
      "affected_area": "neck",
      "likely_cause": "secondary armor piece dropped",
      "recommended_fix": "Add a low-profile gorget bridging helm and cuirass",
      "status": "unresolved"
    },
    {
      "severity": "low",
      "category": "composition",
      "issue": "Back view underlit for review capture",
      "evidence": "OBSERVED: plate read collapses in back view only",
      "affected_area": "capture, not asset",
      "likely_cause": "single key light in the review rig",
      "recommended_fix": "Add a fill light for the back capture",
      "status": "unresolved"
    }
  ],
  "what_is_working": [
    "Armor layering matches the plate construction reference",
    "Consistent facet budget, no mixed-fidelity parts",
    "Correct character review-view conventions"
  ],
  "required_changes": [
    "Separate hands from torso to a 0.3-0.5 cm gap",
    "Head 0.92x, legs +8%, arms to mid-thigh; re-measure 6.5:1",
    "Add gorget; seat left pauldron; resolve boot clipping",
    "Relight back view; re-render all three views"
  ],
  "references_used": [
    {
      "title": "Arm-span and reach anatomy sheet",
      "kind": "diagram",
      "used_for": "fingertips at mid-thigh expectation"
    },
    {
      "title": "Stylized character proportion exemplar (6.5 heads)",
      "kind": "model_sheet",
      "used_for": "heroic stylized ratio target from the brief"
    },
    {
      "title": "Medieval plate construction reference",
      "kind": "diagram",
      "used_for": "gambeson-cuirass-pauldron layering, gorget presence"
    }
  ],
  "confidence_notes": "Level 2: heights/reach/penetration depths are model-data facts, not screenshot estimates. Back-side shader read is limited by the underlit capture and reported as a capture problem, not an asset problem.",
  "next_action": "modify_and_rerender"
}
```

---

# Visual Verification Report

**Asset:** Stylized knight character, T-pose, full-body
**Task:** "Create a stylized knight character in T-pose, 6.5 heads tall, game-ready low-poly with clean silhouette, for a top-down action game."
**Evidence level:** Level 2 — screenshots + model data (same pipeline)
**Views analyzed:** front, left side, back (identical rig, back view relit per iteration 1)
**References used:** same 3 references as iteration 1

## Result

Status: PASS
Score: 7.9 / 10
Threshold: 7.0
Iteration: 2 / 5
Previous score: 5.6
Score delta: +2.3
Weighted total: 7.90
Penalty total: 0.00

## Scoring Weights

Custom weights (unchanged from iteration 1 — anatomy-first preset).

## Category Scores

| Category | Score | Weight | Evidence |
|---|---:|---:|---|
| Silhouette | 8.0/10 | 15% | Longer limbs restored the heroic read; profile carries identity in thumbnail test. |
| Proportions | 8.0/10 | 25% | LEVEL-2 DATA: re-measured 6.5:1 exactly (head 28.2 cm / 183 cm); fingertips end at mid-thigh per the anatomy sheet. |
| Structure | 7.5/10 | 15% | Gorget added and correctly layered; pauldron seated; all brief-listed components present. |
| Geometry | 8.0/10 | 10% | LEVEL-2 DATA: hands clear the torso with 0.4 cm gap; boots in class-2 floor contact; no new intersections after the resize. |
| Materials | 7.5/10 | 5% | Separation unchanged; edge definition survives the relit back view. |
| Reference Similarity | 7.5/10 | 10% | Reach and 6.5-head ratio match; armor layering still matches the plate reference. |
| Style | 8.5/10 | 10% | Proportion fix removed the chibi read; consistent heroic-stylized execution in all views. |
| Composition | 8.0/10 | 10% | Relit back view now reads; framing identical to iteration 1 for regression. |

## What Is Working

- Headline spec met exactly: 6.5:1 confirmed by measurement, not estimation.
- The resize did not break the shoulders (the flagged regression risk): pauldrons
  and gorget survived with only one 1.2 cm seating touch-up.
- Back-view capture now readable.

## Problems

### [LOW] Cape is perfectly mirrored across the spine
- **Evidence:** OBSERVED — cape fold pattern identical left/right in the back view; INFERRED — mirrored mesh half.
- **Affected area:** cape.
- **Likely cause:** INFERRED — mirrored construction, acceptable for production but below the brief's "clean, authored" look.
- **Recommended fix:** RECOMMENDED — optional polish: break cape symmetry with 2–3 asymmetric fold groups.
- **Status:** unresolved

## Reference Comparison

### Observed
6.5:1 ratio; mid-thigh fingertip reach; 0.4 cm hand clearance; seated pauldrons; gorget present; class-2 boot contact.

### Reference-supported
Reach and ratio match the anatomy sheet and exemplar; layering matches plate construction; remaining cape-symmetry note is not reference-governed (natural capes drape asymmetrically — INFERRED style guidance).

### Inferred
Cape mirroring was a deliberate production shortcut; fix is polish-level, not correctness.

### Differences
- Cape symmetry (LOW) — the only surviving delta.

## Required Changes

None — score meets threshold with zero unresolved CRITICAL/HIGH/MEDIUM. The cape-symmetry polish item is optional and non-blocking.

## Regression Check

- Hands↔torso intersection: **verified_fixed** (0.4 cm clearance, class 1).
- Proportion spec: **verified_fixed** (6.5:1 measured).
- Pauldron float: **verified_fixed** (class-2 contact).
- Boot clipping: **verified_fixed** (class-2 contact).
- Missing gorget: **verified_fixed** (present, correctly layered).
- Back-view lighting: **verified_fixed** (relit capture).
- New problems introduced: none detected; regression risk at the shoulders explicitly re-verified clean.

## Verification Decision

PASS — 7.9 ≥ 7.0 with zero unresolved CRITICAL/HIGH/MEDIUM. One optional LOW polish item (cape symmetry) is disclosed. Headline spec satisfied by measurement.

```json
{
  "schema_version": "1.0",
  "asset": "stylized knight character, T-pose",
  "task_summary": "Create a stylized knight character in T-pose, 6.5 heads tall, game-ready low-poly with clean silhouette, for a top-down action game.",
  "status": "pass",
  "score": 7.9,
  "threshold": 7.0,
  "iteration": 2,
  "max_iterations": 5,
  "previous_score": 5.6,
  "score_delta": 2.3,
  "evidence_level": "level_2_screenshot_plus_model_data",
  "views_analyzed": ["front", "left side", "back"],
  "categories": {
    "silhouette": 8.0,
    "proportions": 8.0,
    "structure": 7.5,
    "geometry": 8.0,
    "materials": 7.5,
    "reference_similarity": 7.5,
    "style": 8.5,
    "composition": 8.0
  },
  "weights": {
    "silhouette": 0.15,
    "proportions": 0.25,
    "structure": 0.15,
    "geometry": 0.10,
    "materials": 0.05,
    "reference_similarity": 0.10,
    "style": 0.10,
    "composition": 0.10
  },
  "custom_weights_rationale": "Character anatomy task with explicit head-count spec: proportions lead at .25.",
  "penalties": [],
  "problems": [
    {
      "severity": "critical",
      "category": "geometry",
      "issue": "Hands intersecting torso (iteration 1)",
      "evidence": "LEVEL-2 DATA: 0.4 cm clearance; OBSERVED: fingertips no longer enter the hip plates in any view",
      "recommended_fix": "None — freeze this area",
      "status": "verified_fixed"
    },
    {
      "severity": "high",
      "category": "proportions",
      "issue": "5.5-head body, short arms (iteration 1)",
      "evidence": "LEVEL-2 DATA: re-measured 6.5:1 (28.2 cm head / 183 cm height); fingertips at mid-thigh",
      "recommended_fix": "None — freeze proportions",
      "status": "verified_fixed"
    },
    {
      "severity": "medium",
      "category": "structure",
      "issue": "Missing gorget / floating pauldron / clipping boots (iteration 1)",
      "evidence": "OBSERVED + DATA: gorget present and layered; pauldron class-2; boots class-2",
      "recommended_fix": "None — freeze these areas",
      "status": "verified_fixed"
    },
    {
      "severity": "low",
      "category": "style",
      "issue": "Cape is perfectly mirrored across the spine",
      "evidence": "OBSERVED: fold pattern identical left/right in the back view (new visibility after the relight)",
      "affected_area": "cape",
      "likely_cause": "mirrored construction",
      "recommended_fix": "Optional polish: break symmetry with 2-3 asymmetric fold groups",
      "status": "unresolved"
    }
  ],
  "what_is_working": [
    "Headline spec met exactly: 6.5:1 by measurement",
    "Resize did not regress shoulders (the flagged risk): pauldrons and gorget clean",
    "Relit back capture now reads"
  ],
  "required_changes": [],
  "references_used": [
    {
      "title": "Arm-span and reach anatomy sheet",
      "kind": "diagram",
      "used_for": "reach verification"
    },
    {
      "title": "Stylized character proportion exemplar (6.5 heads)",
      "kind": "model_sheet",
      "used_for": "ratio verification"
    },
    {
      "title": "Medieval plate construction reference",
      "kind": "diagram",
      "used_for": "armor layering verification"
    }
  ],
  "confidence_notes": "Level 2 throughout; every headline number comes from model data, not pixels. Cape symmetry is a polish item, not a correctness failure.",
  "next_action": "accept"
}
```
