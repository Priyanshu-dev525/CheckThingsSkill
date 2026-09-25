# Visual Analysis — the Ten Inspection Lenses

Deep reference for SKILL.md §5. Run **all ten lenses** on every evaluation, in this
order, even when one lens seems obviously fine. Actively hunt for problems: your job
is to falsify "looks good", not to confirm it.

Practical techniques that help any lens:

- **Squint/thumbnail test** — shrink the image until only big shapes and value masses
  remain. If the subject stops being recognizable, the silhouette/value design fails.
- **Greyscale test** — strip color mentally. If two parts that should read as
  different materials become one flat value, materials or lighting fail.
- **Flip test** — mirror the image mentally. Fresh lateral view exposes lopsided
  proportions and accidental asymmetry your eye adapted to.
- **Edge walk** — trace the entire outer contour and note every bump, gap, and
  tangent. Silhouette defects hide between landmarks.

---

## 1. Silhouette

Check: overall outline · recognizability from outline alone · major masses · negative
space · proportion of the outline (height:width of bounding shape) · asymmetry budget ·
shape language (round/square/spiky reads).

Failure signatures: outline could be many different objects; masses blob into one
ellipse; internal detail strong but outline featureless; jagged noise where the real
object is smooth (and vice versa).

**Organic objects:** explicitly check for *unnatural* symmetry — mirrored halves,
radial rings, evenly spaced bumps. See `organic-assets.md`.

Wording: "OBSERVED: the outline reads as a cylinder with a cap; the conifer's stepped
crown profile is not visible in silhouette."

## 2. Proportions

Check: overall height/width/depth · component ratios (cab:bed, torso:leg, trunk:crown)
· spacing rhythm · relative scale of parts.

Rules:
- Compare **ratios**, never absolute pixels ("wheel diameter ≈ 0.22 of overall length"
  is valid; "the truck is 40 meters long" is not — pixels carry no units).
- Anchor ratios against references when available (REFERENCE-SUPPORTED), else against
  common real-world ranges (label INFERRED).
- Symmetric pairs (wheels, arms, windows) must be equal unless the style says otherwise.

## 3. Structure / completeness

Check in hierarchy order:

1. **Primary forms** — the big masses that define identity.
2. **Secondary forms** — subassemblies (bed, crown, limbs, wings).
3. **Tertiary details** — handles, bolts, needles, trim.

Failure signatures: all detail, no primary read; a listed component of the task is
absent ("missing mirrors"); a part exists but is misplaced (headlights above the hood
line); hierarchy inverted (trim louder than the body).

A **missing reference-defining or task-listed component** is at least HIGH severity.

## 4. Geometry (visible only)

Check for: broken/inverted surfaces · obvious intersections · floating parts ·
disconnected parts · excessive penetration · visible bad topology (pinching, shading
tears) · unnatural surfaces · accidental holes · z-fighting (flickering/striped
coplanar faces) · duplicate geometry (doubled edges) · clipping (into ground/camera).

Classify every intersection:

| Class | Name | Meaning | Default action |
|---|---|---|---|
| 1 | No intersection | Clear contact or clear air. | None |
| 2 | Intentional contact | Touching by design (feet on ground, lid on pot). | None |
| 3 | Acceptable shallow overlap | Cluster masses (foliage, rocks) kissing slightly. | Accept; note if repeated |
| 4 | Suspicious overlap | Penetration visible but ambiguous in intent/depth. | Fix unless justified |
| 5 | Severe intersection | Parts pass deeply through each other; reads as an error. | Must fix; HIGH+ |

Level 1 wording discipline: "Visible evidence suggests the left mirror intersects the
door deeply." Only with mesh data (Level 2) may you state intersections as fact for
hidden areas. Catalog of errors, signatures, and fixes: `geometry-errors.md`.

## 5. Materials

Check: does each surface read as its intended material (wood reads wood, metal reads
metal)? · roughness/metallic plausibility · color correctness vs task/reference ·
material **separation** (can you tell where rubber ends and paint begins?) ·
consistency of a shared material across the asset.

Do not confuse lighting faults with material faults: a great material under flat light
looks like bad material. If unsure which is at fault, say so and propose isolating
with a neutral lighting pass (see `composition.md`).

## 6. Lighting

Check: can every important form be read? · crushed blacks hiding parts · blown
highlights erasing detail · flat ambient with no form gradient · shadows cast on the
subject that camouflage geometry · distracting shadow direction.

For review renders, demand neutral readability over mood; mood is a style choice but
never allowed to hide geometry you are being asked to verify.

## 7. Composition

Check: camera angle appropriate to the asset class · subject fills 60–80% of frame ·
nothing important cropped · visual hierarchy leads to the subject/focal point ·
background not fighting the subject · for scenes: focal point, value grouping,
leading lines. Details: `composition.md`.

If the camera *itself* prevents verification (area hidden), that is an evidence
problem: request another view instead of penalizing the asset.

## 8. Style consistency

Check against the **requested** style, not your preference: low-poly · realistic ·
stylized · cartoon · hand-painted · game-ready · minimalist.

Failure signatures: one part realistic, another low-poly; bevels/subdivision softness
in a flat-shaded low-poly brief; photoreal textures on flat-color geometry. Mixed
execution inside one asset is a MEDIUM+ problem.

## 9. Reference similarity

Compare, per reference: silhouette · proportions · characteristic/defining features ·
color palette · material families · component arrangement · style.

Rules:
- Name the reference that supports each comparison (REFERENCE-SUPPORTED).
- Weigh *defining* features most: the stepped crown of a conifer, the crew-cab cut of
  a pickup. Missing a defining feature is HIGH/CRITICAL; missing a niche detail is LOW.
- References disagree? Note the range and pick the task-consistent interpretation; see
  `reference-research.md`.

## 10. Task compliance

Re-read the original request literally. Every explicit requirement is a checklist
item: subject, style, count, composition constraints, technical constraints stated in
*visual* terms.

- Wrong object identity (asked pine, built oak) → CRITICAL, automatic REWORK, score
  capped at 2.9.
- Partial compliance (asked "three crates", two visible) → HIGH.
- Extra unrequested content is not automatically wrong; flag it as a question, not a
  failure, unless it violates the brief.

---

## Severity rubric (use consistently)

| Severity | Definition | Pass impact |
|---|---|---|
| CRITICAL | Wrong identity; destroyed silhouette; asset unreadable/unusable for the task. | Blocks PASS |
| HIGH | Major visible defect a user would immediately notice. | Effectively blocks (score impact) |
| MEDIUM | Notable defect; tolerable in a pinch. | Allowed on PASS if disclosed |
| LOW | Polish-level nitpick. | Allowed on PASS |
