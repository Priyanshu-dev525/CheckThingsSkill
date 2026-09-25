# Example: Walk-Cycle Frames (animation via sampled frames, 2 iterations)

Demonstrates: `references/multi-screenshot.md` frame-sampling in practice (keyframes
+ consecutive pairs), temporal failure classes (foot sliding, mid-motion clipping,
deformation collapse) that no single frame can reveal, and a class-5 temporal
penalty with a regression-checked fix.

---

# Visual Verification Report

**Asset:** Low-poly robot character — walk cycle (8 sampled frames, one stride)
**Task:** "Provide a walk cycle for the low-poly robot character for a platformer game; we will judge it from exported frames."
**Evidence level:** Level 1 — screenshot only (8 exported frames + consecutive pairs)
**Views analyzed:** frames 1–8 side view; consecutive pairs 3→5 and 4→6 (fast-motion regions)
**References used:** 2 — walk-cycle keyframe sheet (contact/down/passing/up pose expectations); robot walk style exemplar (mechanical weight-shift read)

## Result

Status: REWORK REQUIRED
Score: 6.4 / 10
Threshold: 7.0
Iteration: 1 / 5
Previous score: none — first evaluation
Score delta: n/a
Weighted total: 6.88
Penalty total: 0.50

## Scoring Weights

Default weights. Temporal checks (sliding, popping, deformation) run inside the
Geometry and Proportions lenses per `references/multi-screenshot.md`; composition
carries only capture quality since framing is fixed per frame.

## Category Scores

| Category | Score | Weight | Evidence |
|---|---:|---:|---|
| Silhouette | 7.5/10 | 20% | Pose silhouettes read clearly in all 8 frames; stride arc legible; arm-through-torso in frames 4–6 corrupts the side read mid-stride. |
| Proportions | 7.0/10 | 15% | Limb ratios stay consistent frame-to-frame (no accidental squash); head leads the body by roughly one frame in the bob (see Problems). |
| Structure | 7.0/10 | 15% | All key poses present (contact, down, passing, up ×2); no missing rig parts in any frame. |
| Geometry | 5.5/10 | 10% | Class-5 arm/torso intersection frames 4–6; planted foot translates backward frames 3→5 (sliding); knee volume collapse at max bend frame 5. |
| Materials | 7.5/10 | 10% | Panel/joint material separation stable across frames; no crawl or shimmer between consecutive frames. |
| Reference Similarity | 6.0/10 | 15% | Contact and up poses match the keyframe sheet; passing pose frame 5 has bent-knee collapse absent from the sheet; weight-shift read weaker than the robot exemplar. |
| Style | 7.0/10 | 10% | Consistent low-poly execution across frames; motion reads mechanical as intended except the organic head-lead bob. |
| Composition | 7.5/10 | 5% | Fixed side view at consistent scale is correct verification capture; all limbs inside frame in all samples. |

## What Is Working

- Pose vocabulary is correct: contact/down/passing/up all present and readable —
  the cycle's skeleton is right and worth preserving.
- Materials are temporally stable: zero shimmer/crawl across the consecutive pairs.
- Capture is exemplary: fixed side view, consistent scale, full-body in all frames.

## Problems

### [HIGH] Planted foot slides backward frames 3→5
- **Evidence:** OBSERVED — between frames 3 and 5 the right foot (visually planted at frame 3) translates ≈15% of stride length across the ground reference line; classic contact sliding.
- **Affected area:** right foot, contact phase.
- **Likely cause:** INFERRED — root motion and foot keyframes not synchronized (foot keyed on the body, not pinned to the ground).
- **Recommended fix:** RECOMMENDED — pin the contact foot (IK lock or equivalent) from heel-strike to toe-off; drive motion from the root; re-verify frames 3→5 consecutive pair.
- **Status:** unresolved

### [HIGH] Forearm passes through the torso frames 4–6 (class 5)
- **Evidence:** OBSERVED — in the 4→6 pair the swinging forearm disappears into the hip plate for 3 consecutive frames, deepest (~40% of forearm width) at frame 5.
- **Affected area:** left forearm / left hip plate, swing phase.
- **Likely cause:** INFERRED — arm swing arc authored on a slimmer torso pose; hip plate widened later without re-checking the swing.
- **Recommended fix:** RECOMMENDED — widen the swing arc outward ~8–12° at the shoulder (or narrow the hip plate's lateral bulge ~10%) so the minimum clearance across frames 4–6 is ≥0.5 forearm widths.
- **Status:** unresolved

### [MEDIUM] Knee volume collapses at maximum bend (frame 5)
- **Evidence:** OBSERVED — candy-wrapper pinch on the right knee capsule at frame 5 (passing pose); absent at frame 3's smaller bend.
- **Affected area:** right knee, passing pose.
- **Likely cause:** INFERRED — single-axis joint without a bend-compensation shape.
- **Recommended fix:** RECOMMENDED — add bend compensation (widen the knee's outer profile ~15% at full flex) or reduce maximum bend ~10°; re-check frame 5.
- **Status:** unresolved

### [MEDIUM] Head bob leads the body by ~1 frame
- **Evidence:** INFERRED — head vertical peaks (frames 2, 6) precede the body's center-of-mass peaks (frames 3, 7) in the side view; reads organic, against the mechanical-brief exemplar.
- **Affected area:** head bob timing.
- **Likely cause:** INFERRED — head curve offset copied from an organic reference.
- **Recommended fix:** RECOMMENDED — align head and body peaks within ±0.5 frame; mechanical reads favor synchronous or slightly lagging heads.
- **Status:** unresolved

### [LOW] Contact-pose toes float in frame 1
- **Evidence:** OBSERVED — front toes hover ~1–2% of foot height above the ground line at frame 1's contact pose.
- **Affected area:** left foot, contact pose.
- **Likely cause:** INFERRED — toe-off curve bleeding into the contact key.
- **Recommended fix:** RECOMMENDED — clamp the toe channel to ground contact for the contact key only.
- **Status:** unresolved

## Penalties (if any)

- Class-5 temporal intersection (arm↔torso, 3 consecutive frames): −0.50 — per-frame Geometry already reduced, but a defect spanning 3 of 8 frames also breaks the silhouette lens mid-cycle and the brief's animation deliverable itself; the per-frame category price understates a motion-phase fault.
- **Penalty total:** −0.50 (cap 3.00)

## Reference Comparison

### Observed
All four key poses present; sliding contact foot; 3-frame arm-through-torso; knee pinch at max bend; head-lead bob; clean materials.

### Reference-supported
Keyframe sheet: planted foot is stationary during contact; passing pose keeps knee volume; robot exemplar: head and body weight shift synchronously.

### Inferred
The sliding will be invisible if the game moves the character root at exactly the slide rate — a fragile coincidence; fix the cycle, do not engineer around it.

### Differences
- Contact foot not stationary (HIGH) · passing-pose knee volume (MEDIUM) · head/body sync (MEDIUM) · arm clearance (HIGH, internal collision).

## Required Changes

1. Pin contact feet through their contact windows (priority 1 — motion-breaking).
2. Restore arm swing clearance ≥0.5 forearm widths across frames 4–6.
3. Fix knee volume at full flex; re-verify frame 5.
4. Align head/body bob peaks within ±0.5 frame.
5. Clamp contact-key toe float; re-export the 8 frames and both consecutive pairs.

## Verification Decision

REWORK REQUIRED — two motion-breaking faults (slide, 3-frame class-5 intersection) fail the animation-specific contract even though every still frame is handsome. Apply changes 1–5, re-export frames plus pairs 3→5 and 4→6, re-evaluate (iteration 2/5).

```json
{
  "schema_version": "1.0",
  "asset": "low-poly robot walk cycle (8 frames)",
  "task_summary": "Provide a walk cycle for the low-poly robot character for a platformer game; judged from exported frames.",
  "status": "rework_required",
  "score": 6.4,
  "threshold": 7.0,
  "iteration": 1,
  "max_iterations": 5,
  "evidence_level": "level_1_screenshot_only",
  "views_analyzed": ["frames 1-8 side view", "consecutive pair 3-5", "consecutive pair 4-6"],
  "categories": {
    "silhouette": 7.5,
    "proportions": 7.0,
    "structure": 7.0,
    "geometry": 5.5,
    "materials": 7.5,
    "reference_similarity": 6.0,
    "style": 7.0,
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
      "issue": "Class-5 temporal intersection: forearm through torso over 3 consecutive frames (4-6)",
      "points": 0.5,
      "rationale": "Per-frame Geometry deduction prices one frame; a 3-frame motion-phase fault also breaks the silhouette read mid-cycle and the animation deliverable itself, which the 10% category weight understates."
    }
  ],
  "problems": [
    {
      "severity": "high",
      "category": "geometry",
      "issue": "Planted foot slides backward ~15% of stride length between frames 3 and 5",
      "evidence": "OBSERVED: right foot translates against the ground reference in the 3->5 consecutive pair",
      "affected_area": "right foot, contact phase",
      "likely_cause": "root motion not synchronized with foot keys",
      "recommended_fix": "Pin contact foot (IK lock/equivalent) heel-strike to toe-off; root drives motion; re-verify pair 3-5",
      "status": "unresolved"
    },
    {
      "severity": "high",
      "category": "geometry",
      "issue": "Forearm passes through torso in frames 4-6 (class 5, deepest ~40% width at frame 5)",
      "evidence": "OBSERVED: forearm disappears into hip plate across 3 consecutive frames",
      "affected_area": "left forearm / left hip plate",
      "likely_cause": "swing arc authored before the hip plate widened",
      "recommended_fix": "Widen swing arc ~8-12deg at shoulder or narrow hip bulge ~10%; min clearance >=0.5 forearm widths",
      "status": "unresolved"
    },
    {
      "severity": "medium",
      "category": "geometry",
      "issue": "Knee volume collapse (candy-wrapper) at maximum bend, frame 5",
      "evidence": "OBSERVED: pinch on right knee capsule at passing pose; absent at frame 3 bend",
      "affected_area": "right knee",
      "likely_cause": "single-axis joint, no bend compensation",
      "recommended_fix": "Add bend compensation (~15% outer profile at full flex) or reduce max bend ~10deg",
      "status": "unresolved"
    },
    {
      "severity": "medium",
      "category": "proportions",
      "issue": "Head bob leads body peaks by ~1 frame",
      "evidence": "INFERRED: head peaks at frames 2/6, body center-of-mass peaks at frames 3/7",
      "affected_area": "head bob timing",
      "likely_cause": "head curve offset from organic reference",
      "recommended_fix": "Align head/body peaks within +/-0.5 frame",
      "status": "unresolved"
    },
    {
      "severity": "low",
      "category": "geometry",
      "issue": "Contact-pose toes float ~1-2% of foot height in frame 1",
      "evidence": "OBSERVED: air gap under front toes at contact key",
      "affected_area": "left foot, contact pose",
      "likely_cause": "toe-off curve bleeding into contact key",
      "recommended_fix": "Clamp toe channel at the contact key",
      "status": "unresolved"
    }
  ],
  "what_is_working": [
    "Correct pose vocabulary: contact/down/passing/up all present and readable",
    "Materials temporally stable: zero shimmer across consecutive pairs",
    "Exemplary frame capture: fixed view, consistent scale, full-body"
  ],
  "required_changes": [
    "Pin contact feet through contact windows; re-verify pair 3-5",
    "Restore arm clearance >=0.5 forearm widths across frames 4-6",
    "Fix knee volume at full flex; re-check frame 5",
    "Align head/body bob peaks within +/-0.5 frame",
    "Clamp contact-key toe float; re-export 8 frames + pairs"
  ],
  "references_used": [
    {
      "title": "Walk-cycle keyframe sheet (contact/down/passing/up)",
      "kind": "diagram",
      "used_for": "pose inventory, planted-foot contact expectation, passing-pose knee volume"
    },
    {
      "title": "Robot walk style exemplar",
      "kind": "artwork",
      "used_for": "mechanical weight-shift read, synchronous head/body timing"
    }
  ],
  "confidence_notes": "Level 1 from 8 frames: interpolation between frames unobserved; sliding measured against the ground line in-frame, not world units. No claims about the rig's internals beyond visible frame evidence.",
  "next_action": "modify_and_rerender"
}
```

---

# Visual Verification Report

**Asset:** Low-poly robot character — walk cycle (8 re-exported frames, one stride)
**Task:** "Provide a walk cycle for the low-poly robot character for a platformer game; we will judge it from exported frames."
**Evidence level:** Level 1 — screenshot only (8 re-exported frames + same consecutive pairs — regression set)
**Views analyzed:** frames 1–8 side view; consecutive pairs 3→5 and 4→6 (identical sampling to iteration 1)
**References used:** same 2 references as iteration 1

## Result

Status: PASS
Score: 7.5 / 10
Threshold: 7.0
Iteration: 2 / 5
Previous score: 6.4
Score delta: +1.1
Weighted total: 7.50
Penalty total: 0.00

## Scoring Weights

Default weights (unchanged from iteration 1).

## Category Scores

| Category | Score | Weight | Evidence |
|---|---:|---:|---|
| Silhouette | 8.0/10 | 20% | Mid-stride side read restored: no limb/torso merges in any frame; stride arc clean through the passing pose. |
| Proportions | 7.5/10 | 15% | Limb ratios stable; head/body peaks now synchronous within the half-frame tolerance; weight shift reads mechanical. |
| Structure | 7.5/10 | 15% | Pose inventory intact after fixes; contact poses now genuinely planted. |
| Geometry | 7.5/10 | 10% | Pinned feet hold position across pair 3→5; arm clears the hip by ≥0.5 forearm widths frames 4–6; knee volume holds at frame 5 (residual slight pinch, see LOW). |
| Materials | 7.5/10 | 10% | Still temporally stable; no shimmer introduced by re-export. |
| Reference Similarity | 7.0/10 | 15% | Contact and passing poses now match the keyframe sheet; weight shift matches the robot exemplar's synchronous read. |
| Style | 7.0/10 | 10% | Mechanical read now consistent with the brief; low-poly execution unchanged. |
| Composition | 8.0/10 | 5% | Identical fixed-view regression capture; all limbs framed. |

## What Is Working

- Both motion-breaking faults fixed without touching the pose vocabulary (the
  asset's main strength survived surgery).
- Foot pinning verified on the consecutive pair, not inferred from stills.
- Regressions risk zones (hip plate, swing arc) re-checked clean after the clearance fix.

## Problems

### [LOW] Slight residual knee pinch at frame 5
- **Evidence:** OBSERVED — bend compensation removed ~90% of the collapse; a faint crease remains at extreme flex.
- **Affected area:** right knee, passing pose.
- **Likely cause:** INFERRED — conservative compensation amount.
- **Recommended fix:** RECOMMENDED — optional polish: widen outer knee profile another ~5% at full flex.
- **Status:** unresolved

## Reference Comparison

### Observed
Stationary contact foot across pair 3→5; ≥0.5-width arm clearance frames 4–6; knees hold volume; synchronous head/body peaks; planted toes at contact keys.

### Reference-supported
Contact behavior and passing-pose volume match the keyframe sheet; timing read matches the robot exemplar.

### Inferred
Interpolation smoothness between frames remains unverified by design (frames-only deliverable); no claim made.

### Differences
- Residual knee crease (LOW) — only surviving delta.

## Required Changes

None — score meets threshold with zero unresolved CRITICAL/HIGH. The residual knee crease (LOW) is optional polish and non-blocking.

## Regression Check

- Foot sliding: **verified_fixed** — planted foot immobile across pair 3→5 (were ~15% stride).
- Arm↔torso intersection: **verified_fixed** — clearance ≥0.5 widths in all of frames 4–6 (was class 5).
- Knee collapse: **addressed→partially verified** — ~90% improved; residual crease tracked as LOW above.
- Head/body timing: **verified_fixed** — peaks synchronous within ±0.5 frame.
- Toe float: **verified_fixed** — contact keys clamped.
- New problems introduced: none detected on the full 8-frame set and both pairs.

## Verification Decision

PASS — 7.5 ≥ 7.0 with zero unresolved CRITICAL/HIGH/MEDIUM. One residual LOW (knee crease) disclosed for polish. The cycle's pose structure was preserved throughout the fix loop.

```json
{
  "schema_version": "1.0",
  "asset": "low-poly robot walk cycle (8 frames)",
  "task_summary": "Provide a walk cycle for the low-poly robot character for a platformer game; judged from exported frames.",
  "status": "pass",
  "score": 7.5,
  "threshold": 7.0,
  "iteration": 2,
  "max_iterations": 5,
  "previous_score": 6.4,
  "score_delta": 1.1,
  "evidence_level": "level_1_screenshot_only",
  "views_analyzed": ["frames 1-8 side view", "consecutive pair 3-5", "consecutive pair 4-6"],
  "categories": {
    "silhouette": 8.0,
    "proportions": 7.5,
    "structure": 7.5,
    "geometry": 7.5,
    "materials": 7.5,
    "reference_similarity": 7.0,
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
      "severity": "high",
      "category": "geometry",
      "issue": "Foot sliding (iteration 1)",
      "evidence": "OBSERVED in this export: planted foot immobile across pair 3-5",
      "recommended_fix": "None — freeze the contact pipeline",
      "status": "verified_fixed"
    },
    {
      "severity": "high",
      "category": "geometry",
      "issue": "Arm-through-torso frames 4-6 (iteration 1)",
      "evidence": "OBSERVED: >=0.5 forearm-width clearance in frames 4-6",
      "recommended_fix": "None — freeze the swing arc",
      "status": "verified_fixed"
    },
    {
      "severity": "medium",
      "category": "geometry",
      "issue": "Knee volume collapse at frame 5 (iteration 1)",
      "evidence": "OBSERVED: ~90% improved; faint crease remains at extreme flex",
      "recommended_fix": "Optional polish: widen outer knee profile another ~5% at full flex",
      "status": "addressed"
    },
    {
      "severity": "medium",
      "category": "proportions",
      "issue": "Head bob leading body (iteration 1)",
      "evidence": "OBSERVED: peaks now synchronous within +/-0.5 frame",
      "recommended_fix": "None — freeze the timing",
      "status": "verified_fixed"
    },
    {
      "severity": "low",
      "category": "geometry",
      "issue": "Contact-pose toe float (iteration 1)",
      "evidence": "OBSERVED: contact keys clamped to the ground line",
      "recommended_fix": "None — freeze the contact keys",
      "status": "verified_fixed"
    },
    {
      "severity": "low",
      "category": "geometry",
      "issue": "Residual knee crease at extreme flex",
      "evidence": "OBSERVED: faint pinch remains at frame 5 only",
      "affected_area": "right knee, passing pose",
      "likely_cause": "conservative bend-compensation amount",
      "recommended_fix": "Optional polish: widen outer knee profile another ~5% at full flex",
      "status": "unresolved"
    }
  ],
  "what_is_working": [
    "Both motion-breaking faults fixed without disturbing the pose vocabulary",
    "Foot pinning verified on the consecutive pair, not inferred from stills",
    "Hip plate and swing arc regression zones re-checked clean"
  ],
  "required_changes": [],
  "references_used": [
    {
      "title": "Walk-cycle keyframe sheet (contact/down/passing/up)",
      "kind": "diagram",
      "used_for": "pose and contact verification"
    },
    {
      "title": "Robot walk style exemplar",
      "kind": "artwork",
      "used_for": "synchronous timing verification"
    }
  ],
  "confidence_notes": "Level 1 from 8 frames; interpolation between frames unverified by design (frames-only deliverable). All fixed items verified on the identical sampling used to detect them.",
  "next_action": "accept"
}
```

