# Example: Low-Poly Pine Tree (organic asset, 2 iterations)

Demonstrates: the loop end-to-end, organic-asset symmetry checks, a critical-issue
penalty, reference redistribution is *not* needed here (references exist), and a
regression-checked PASS. Evidence Level 1 throughout (screenshots only).

---

# Visual Verification Report

**Asset:** Low-poly stylized pine tree (forest scatter pack candidate)
**Task:** "Create a low-poly stylized pine tree, game-ready, for a forest scatter system."
**Evidence level:** Level 1 — screenshot only
**Views analyzed:** single ¾ perspective render, neutral background
**References used:** 3 — mature lodgepole/lodgepole-like pine photo set (silhouette + crown range); conifer morphology sheet (whorled branching); stylized conifer game-art exemplar (style target)

## Result

Status: REWORK REQUIRED
Score: 5.2 / 10
Threshold: 7.0
Iteration: 1 / 5
Previous score: none — first evaluation
Score delta: n/a
Weighted total: 5.73
Penalty total: 0.50

## Scoring Weights

Default weights.

## Category Scores

| Category | Score | Weight | Evidence |
|---|---:|---:|---|
| Silhouette | 4.5/10 | 20% | Crown outline is a near-perfect vertical column of 8 evenly spaced bulges; the stepped, serrated conifer profile is absent. |
| Proportions | 6.0/10 | 15% | Height:crown-width ≈ 4.5:1 observed; reference range for mature pines ≈ 3–3.5:1 — crown too narrow. Trunk thickness plausible. |
| Structure | 6.5/10 | 15% | Trunk + crown masses exist, but no branch whorls or connecting stubs are indicated; crown masses attach to nothing visible. |
| Geometry | 6.0/10 | 10% | Visible evidence suggests deep trunk↔crown penetration (class 5) at 8 contacts; 2 upper masses appear fully detached. |
| Materials | 6.5/10 | 10% | Green family correct, single flat value across the whole crown; no value separation between lit and shaded lobes. |
| Reference Similarity | 4.5/10 | 15% | Defining features missing versus all 3 references: whorled branching steps, ragged crown outline, trunk glimpses through crown. |
| Style | 6.5/10 | 10% | Faceted low-poly execution fits the brief, but radial perfection reads procedural rather than stylized. |
| Composition | 7.5/10 | 5% | Subject centered, ~70% of frame, neutral lighting — acceptable review capture. |

## What Is Working

- Trunk taper and trunk/crown thickness relationship are plausible and stylistically on-brief.
- The capture itself is a good verification render (framing, neutral light).
- Color family (cool conifer green, warm trunk brown) matches the requested style.

## Problems

### [CRITICAL] Radial mathematical symmetry of the crown
- **Evidence:** OBSERVED — 8 crown masses evenly spaced around the trunk axis, near-identical size and rotation; outline mirrored left/right.
- **Affected area:** entire crown.
- **Likely cause:** INFERRED — array/radial duplicate placement of one foliage block.
- **Recommended fix:** RECOMMENDED — delete 3 of the 8 masses; cluster survivors in 2–3 lobes; jitter yaw ±20–40° and tilt ±5–15°; scale along a continuous 0.6–1.4× range with one oversized hero lobe; move the upper-right mass 0.25–0.4 crown radii outward.
- **Status:** unresolved

### [HIGH] Crown masses deeply intersect the trunk
- **Evidence:** OBSERVED — at 8 contact points the foliage cones pass roughly a third of their radius into/through the trunk (class 5); visible on the left edge and behind the tip.
- **Affected area:** all crown–trunk contacts.
- **Likely cause:** INFERRED — foliage placed on concentric rings around the axis with no contact pass.
- **Recommended fix:** RECOMMENDED — move each mass outward to shallow class-3 contact; add short branch stubs bridging trunk→mass at the 5 most visible contacts.
- **Status:** unresolved

### [MEDIUM] Crown too narrow for the species read
- **Evidence:** REFERENCE-SUPPORTED (pine photo set) — mature pine height:crown ≈ 3–3.5:1; OBSERVED ≈ 4.5:1.
- **Affected area:** overall crown.
- **Likely cause:** INFERRED — columnar placement from the radial layout.
- **Recommended fix:** RECOMMENDED — widen crown ~25% at the lower whorl; keep total height.
- **Status:** unresolved

### [MEDIUM] Crown material is one flat value
- **Evidence:** OBSERVED — lit and shaded crown lobes share one green; greyscale test collapses crown into one mass.
- **Affected area:** crown material.
- **Likely cause:** INFERRED — single material, no lobe-level value variation.
- **Recommended fix:** RECOMMENDED — assign a second crown material ~15% darker to 2 of 5 lobes or add per-lobe value variation.
- **Status:** unresolved

## Penalties (if any)

- Severe intersection (trunk↔crown, spanning Silhouette and Materials beyond Geometry's 10% weight): −0.50 — justified because the defect damages three categories whose combined deduction (≈0.8) understates a class-5 fault visible without zooming.
- **Penalty total:** −0.50 (cap 3.00)

## Reference Comparison

### Observed
Columnar, radially symmetric crown; 8 equal masses; uniform green; no whorl steps; no trunk visible through crown.

### Reference-supported
Mature pines show whorled branch steps, ragged crown outline, height:crown ≈ 3–3.5:1, and visible trunk gaps near the crown break.

### Inferred
The perfection of the ring implies array placement; INFERRED, possibly authored by hand — visual result is identical either way.

### Differences
- Stepped conifer profile absent (HIGH) · Whorls absent (HIGH) · Crown 25% too narrow (MEDIUM) · Single-value crown (MEDIUM).

## Required Changes

1. Break radial symmetry per the CRITICAL fix above (delete 3 masses, cluster, jitter, rescale range 0.6–1.4×).
2. Move every crown mass to shallow class-3 trunk contact; add branch stubs at 5 visible contacts.
3. Widen the crown ~25% at the lower whorl to reach ≈ 3.2:1 height:crown.
4. Introduce 2-value crown material variation.

## Verification Decision

REWORK REQUIRED — apply changes 1–4 in order, then re-render the same ¾ view and re-evaluate (iteration 2/5). Expected: silhouette and reference similarity recover fastest; watch that mass moves do not open crown holes.

```json
{
  "schema_version": "1.0",
  "asset": "low-poly stylized pine tree",
  "task_summary": "Create a low-poly stylized pine tree, game-ready, for a forest scatter system.",
  "status": "rework_required",
  "score": 5.2,
  "threshold": 7.0,
  "iteration": 1,
  "max_iterations": 5,
  "evidence_level": "level_1_screenshot_only",
  "views_analyzed": ["three-quarter perspective"],
  "categories": {
    "silhouette": 4.5,
    "proportions": 6.0,
    "structure": 6.5,
    "geometry": 6.0,
    "materials": 6.5,
    "reference_similarity": 4.5,
    "style": 6.5,
    "composition": 7.5
  },
  "weights": {
    "silhouette": 0.20,
    "proportions": 0.15,
    "structure": 0.15,
    "geometry": 0.10,
    "materials": 0.10,
    "reference_similarity": 0.15,
    "style": 0.10,
    "composition": 0.05
  },
  "penalties": [
    {
      "issue": "Severe deep trunk-foliage intersection (class 5) at 8 contacts, spanning Silhouette and Materials beyond Geometry's weight",
      "points": 0.5,
      "rationale": "Category deductions (~0.8 combined) understate a class-5 fault; penalty prices the cross-category severity without re-charging the Geometry deduction."
    }
  ],
  "problems": [
    {
      "severity": "critical",
      "category": "silhouette",
      "issue": "Crown is radially symmetric: 8 identical evenly-spaced masses around the trunk axis",
      "evidence": "OBSERVED: mirrored outline and equal spacing in the 3/4 render; INFERRED: array/duplicate placement",
      "affected_area": "entire crown",
      "likely_cause": "radial duplicate placement of a single foliage block",
      "recommended_fix": "Delete 3 of 8 masses; cluster survivors in 2-3 lobes; jitter yaw +/-20-40deg, tilt +/-5-15deg; scale 0.6-1.4x continuous with one hero lobe; move upper-right mass 0.25-0.4 crown radii outward",
      "status": "unresolved"
    },
    {
      "severity": "high",
      "category": "geometry",
      "issue": "Crown masses penetrate the trunk deeply (class 5) at 8 contacts; 2 upper masses detached",
      "evidence": "OBSERVED: visible cone-through-trunk passage on the left edge and near the tip",
      "affected_area": "all crown-trunk contacts",
      "likely_cause": "concentric ring placement with no contact pass",
      "recommended_fix": "Move each mass outward to shallow class-3 contact; add branch stubs at the 5 most visible contacts",
      "status": "unresolved"
    },
    {
      "severity": "medium",
      "category": "proportions",
      "issue": "Crown too narrow: height:crown about 4.5:1 vs reference range 3-3.5:1",
      "evidence": "REFERENCE-SUPPORTED (mature pine photo set) for the range; OBSERVED for the 4.5:1 measurement ratio",
      "affected_area": "overall crown",
      "likely_cause": "columnar radial layout",
      "recommended_fix": "Widen crown ~25% at the lower whorl; keep total height",
      "status": "unresolved"
    },
    {
      "severity": "medium",
      "category": "materials",
      "issue": "Single flat crown value; lit and shaded lobes indistinguishable in greyscale",
      "evidence": "OBSERVED: greyscale collapse of the crown into one mass",
      "affected_area": "crown material",
      "likely_cause": "one shared material, no value variation",
      "recommended_fix": "Assign a second crown material ~15% darker to 2 of 5 lobes",
      "status": "unresolved"
    }
  ],
  "what_is_working": [
    "Trunk taper and trunk/crown thickness relationship plausible and on-style",
    "Verification-quality capture: 70% frame fill, neutral lighting",
    "Color family matches the brief"
  ],
  "required_changes": [
    "Delete 3 of 8 crown masses; cluster survivors; jitter yaw +/-20-40deg and tilt +/-5-15deg; continuous scale range 0.6-1.4x with one hero lobe",
    "Move all crown masses to shallow class-3 trunk contact; add branch stubs at 5 visible contacts",
    "Widen crown ~25% at lower whorl (target ~3.2:1 height:crown)",
    "Add a second crown material ~15% darker on 2 of 5 lobes"
  ],
  "references_used": [
    {
      "title": "Mature lodgepole-type pine photo set",
      "url": "https://www.inaturalist.org/taxa/133796-Pinus-contorta",
      "kind": "photo",
      "used_for": "silhouette, height:crown ratio range 3-3.5:1, ragged crown outline"
    },
    {
      "title": "Conifer morphology sheet (whorled branching)",
      "url": "https://www.fs.usda.gov/database/feis/plants/tree/pincon/all.html",
      "kind": "diagram",
      "used_for": "defining features: whorled branch steps, trunk glimpses through crown"
    },
    {
      "title": "Stylized conifer game-art exemplar",
      "kind": "artwork",
      "used_for": "style target: faceted lobes, 2-value crown treatment"
    }
  ],
  "confidence_notes": "Level 1 only: crown backside, exact penetration depth, and topology are not verifiable from one render. Intersections are visible-evidence claims. One-view capture; a second perpendicular view requested for iteration 2.",
  "next_action": "modify_and_rerender"
}
```

---

# Visual Verification Report

**Asset:** Low-poly stylized pine tree (forest scatter pack candidate)
**Task:** "Create a low-poly stylized pine tree, game-ready, for a forest scatter system."
**Evidence level:** Level 1 — screenshot only
**Views analyzed:** same ¾ perspective as iteration 1 (regression pair)
**References used:** same 3 references as iteration 1

## Result

Status: PASS
Score: 7.4 / 10
Threshold: 7.0
Iteration: 2 / 5
Previous score: 5.2
Score delta: +2.2
Weighted total: 7.38
Penalty total: 0.00

## Scoring Weights

Default weights.

## Category Scores

| Category | Score | Weight | Evidence |
|---|---:|---:|---|
| Silhouette | 7.5/10 | 20% | Stepped crown now readable at thumbnail size; 11 masses with varied radii; slight tip lean breaks the axis mirror. |
| Proportions | 7.5/10 | 15% | Height:crown now ≈ 3.2:1, inside the reference range; trunk ≈ 18% of height at the crown break. |
| Structure | 7.5/10 | 15% | One hero lobe + 2 subordinate lobes; branch stubs connect 9 of 11 masses to the trunk. |
| Geometry | 7.0/10 | 10% | Penetration reduced to class 3 at 8 contacts; class 4 suspected at 2 contacts near the tip (monitored, not blocking). |
| Materials | 7.0/10 | 10% | Two-value crown separates lit/shaded lobes in greyscale; shaded side still borderline flat at this light angle. |
| Reference Similarity | 7.5/10 | 15% | Whorl steps and ragged outline now match the 3 references; dead-branch skirt (a minor species cue) still missing. |
| Style | 7.0/10 | 10% | Reads hand-authored stylized; facets consistent with the low-poly brief; no realism leakage. |
| Composition | 8.0/10 | 5% | Same neutral capture; crown fully in frame with margin; shadow contact reads. |

## What Is Working

- Crown silhouette now carries identity at thumbnail scale — biggest single recovery (+3.0 in the heaviest category).
- Branch stubs sell construction, not just contact.
- All iteration-1 strengths preserved (trunk taper, capture, palette).

## Problems

### [LOW] Dead-branch skirt missing at the crown break
- **Evidence:** REFERENCE-SUPPORTED (morphology sheet) — mature pines show a sparse dead-branch ring below live crown; OBSERVED — absent.
- **Affected area:** crown break, mid-trunk.
- **Likely cause:** INFERRED — scoped out; tertiary detail.
- **Recommended fix:** RECOMMENDED — optional polish: add 4–6 sparse dead branches at the crown break in a later polish pass.
- **Status:** unresolved

### [LOW] Shaded-side crown value drifts flat
- **Evidence:** OBSERVED — greyscale test separates lit lobes but shaded lobes merge at the current light angle.
- **Affected area:** crown shaded side.
- **Likely cause:** INFERRED — second crown material only ~15% darker.
- **Recommended fix:** RECOMMENDED — optional: deepen the second crown material another ~10% or rotate the key light for review capture.
- **Status:** unresolved

## Reference Comparison

### Observed
Stepped crown with 11 varied masses, visible whorl steps, hero lobe lower-left, trunk glimpses at the crown break, class-3 contacts at 8 points.

### Reference-supported
Height:crown 3.2:1 within the 3–3.5:1 reference band; ragged outline and whorl steps match the morphology sheet; two-value crown matches the style exemplar.

### Inferred
The remaining class-4 suspicion near the tip may be occlusion ambiguity rather than true intersection — a side view would settle it.

### Differences
- Dead-branch skirt absent (LOW) · Shaded-side value still flat (LOW). All iteration-1 differences closed.

## Required Changes

None — score meets threshold with zero unresolved CRITICAL/HIGH. Optional polish items (dead-branch skirt, shaded-side value) are listed under Problems and may be handled in a later non-blocking pass.

## Regression Check

- Radial symmetry: **verified_fixed** — no ring, mirror, or equal spacing remains in the new render.
- Deep trunk intersection: **verified_fixed** at 8/10 contacts; 2 near-tip contacts improved to suspected class 4 (was class 5) — accepted with monitoring.
- Crown width: **verified_fixed** — ratio now inside reference band.
- Crown value: **verified_fixed** for lit lobes; shaded side regressed to borderline flat at this light angle (tracked as LOW above).
- New problems introduced: none observed. SAME view, lighting, and framing as iteration 1 used for this comparison.

## Verification Decision

PASS — 7.4 ≥ 7.0 with zero unresolved CRITICAL/HIGH; two disclosed LOW polish items recorded above. The asset is accepted for the scatter pack; polish may proceed in a later non-blocking pass.

```json
{
  "schema_version": "1.0",
  "asset": "low-poly stylized pine tree",
  "task_summary": "Create a low-poly stylized pine tree, game-ready, for a forest scatter system.",
  "status": "pass",
  "score": 7.4,
  "threshold": 7.0,
  "iteration": 2,
  "max_iterations": 5,
  "previous_score": 5.2,
  "score_delta": 2.2,
  "evidence_level": "level_1_screenshot_only",
  "views_analyzed": ["three-quarter perspective"],
  "categories": {
    "silhouette": 7.5,
    "proportions": 7.5,
    "structure": 7.5,
    "geometry": 7.0,
    "materials": 7.0,
    "reference_similarity": 7.5,
    "style": 7.0,
    "composition": 8.0
  },
  "weights": {
    "silhouette": 0.20,
    "proportions": 0.15,
    "structure": 0.15,
    "geometry": 0.10,
    "materials": 0.10,
    "reference_similarity": 0.15,
    "style": 0.10,
    "composition": 0.05
  },
  "penalties": [],
  "problems": [
    {
      "severity": "critical",
      "category": "silhouette",
      "issue": "Crown radial symmetry (iteration 1)",
      "evidence": "OBSERVED in this render: no ring, mirror, or equal spacing remains",
      "recommended_fix": "None — do not regress this freeze in future edits",
      "status": "verified_fixed"
    },
    {
      "severity": "high",
      "category": "geometry",
      "issue": "Deep trunk-foliage intersections (iteration 1)",
      "evidence": "OBSERVED: contacts now class 3 at 8 of 10 points; 2 near-tip contacts suspected class 4 (occlusion-ambiguous)",
      "recommended_fix": "Optional: nudge the 2 tip masses outward ~0.1 crown radii if a side view confirms class 4",
      "status": "verified_fixed"
    },
    {
      "severity": "low",
      "category": "reference_similarity",
      "issue": "Dead-branch skirt missing at the crown break",
      "evidence": "REFERENCE-SUPPORTED (morphology sheet): sparse dead-branch ring expected; OBSERVED: absent",
      "affected_area": "crown break, mid-trunk",
      "likely_cause": "tertiary detail scoped out",
      "recommended_fix": "Optional polish: add 4-6 sparse dead branches at the crown break",
      "status": "unresolved"
    },
    {
      "severity": "low",
      "category": "materials",
      "issue": "Shaded-side crown values still merge in greyscale",
      "evidence": "OBSERVED: shaded lobes collapse at current light angle",
      "affected_area": "crown shaded side",
      "likely_cause": "second crown material only ~15% darker",
      "recommended_fix": "Optional: deepen second crown material ~10% or adjust review key light",
      "status": "unresolved"
    }
  ],
  "what_is_working": [
    "Crown silhouette carries identity at thumbnail scale",
    "Branch stubs sell construction at 9 of 11 contacts",
    "All iteration-1 strengths preserved (trunk taper, capture, palette)"
  ],
  "required_changes": [],
  "references_used": [
    {
      "title": "Mature lodgepole-type pine photo set",
      "url": "https://www.inaturalist.org/taxa/133796-Pinus-contorta",
      "kind": "photo",
      "used_for": "silhouette and height:crown ratio verification"
    },
    {
      "title": "Conifer morphology sheet (whorled branching)",
      "url": "https://www.fs.usda.gov/database/feis/plants/tree/pincon/all.html",
      "kind": "diagram",
      "used_for": "whorl steps, dead-branch skirt expectation"
    },
    {
      "title": "Stylized conifer game-art exemplar",
      "kind": "artwork",
      "used_for": "two-value crown style verification"
    }
  ],
  "confidence_notes": "Level 1 only; same single view as iteration 1 (deliberate, for regression). The 2 suspected class-4 tip contacts would need a perpendicular view to confirm. Pass decision does not depend on them.",
  "next_action": "accept"
}
```
