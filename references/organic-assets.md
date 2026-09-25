# Organic Asset Analysis

Applies to trees, plants, bushes, rocks, mountains, clouds, creatures, terrain, and
any clustered natural forms. Organic assets fail differently from hard-surface ones:
their enemy is not missing bolts but **mathematical perfection and uncontrolled
noise**. The target is always:

> **DESIGNED IRREGULARITY** — variation that looks intentional and natural.
> Not mathematical symmetry. Not random noise.

## Symmetry & repetition checklist (run on every organic asset)

For each, note OBSERVED counts where possible ("8 crown masses", "5 rock plates"):

- [ ] **Mirrored halves** — left and right sides identical across the main axis?
- [ ] **Radial rings** — elements evenly spaced around a center like spokes?
- [ ] **Equal spacing** — gaps between repeated elements near-identical?
- [ ] **Identical clones** — same shape/size/rotation repeated (foliage cards, tufts)?
- [ ] **Uniform rotation** — all elements upright or stepped by a constant angle?
- [ ] **Repeated scale** — one or two discrete sizes instead of a continuous range?
- [ ] **Perfect primitives** — spheres, cones, cylinders readable as math objects?
- [ ] **Stacking** — elements piled in vertical totems or neat layers?
- [ ] **Excessive overlap** — deep interpenetration (class 4–5; see
      `visual-analysis.md`) inside what should read as one mass?
- [ ] **Gaps** — visible holes/splits inside a mass meant to be continuous?
- [ ] **Detached/floating pieces** — elements with no visible support/connection?
- [ ] **Implausible center of mass** — top-heavy growth that would fall/spin?
- [ ] **Unnatural silhouette** — contour too smooth/geometric for the subject?

Three or more checked boxes ⇒ treat symmetry as a HIGH+ structural problem, not a
style choice.

## Controlled vs uncontrolled randomness

Good irregularity is **parameterized around an authorial intent**:

| Parameter | Designed target | Red flag |
|---|---|---|
| Element size | Continuous range around a mean (e.g. 0.6–1.4×) with a few heroes larger | 1–2 discrete sizes; or sizes random from 0.1–5× |
| Position | Clustered with ellipsoid/noise falloff, center of mass near the support | Uniform grid, perfect ring, or pure confetti |
| Rotation | Jittered yaw (±20–40°), slight tilt (±5–15°) | All identical, or full random flip chaos |
| Spacing | Varied gaps with big–small rhythm | Metronome equal gaps |
| Silhouette | Asymmetric but balanced, leaning into a read | Oval/round cone with noise bumps |

Uncontrolled randomness reads as noise: no dominant masses, no rhythm, equal visual
energy everywhere. Designed irregularity has 2–4 dominant masses and subordinate
variance around them.

## Cluster overlap rules (foliage, rocks, clouds)

Use the 5-class intersection scale from `visual-analysis.md`:

- **Class 3 (shallow overlap)** is the *correct* default for cluster elements — it
  fuses them into one readable mass.
- **Class 4–5** inside a cluster usually means a placement bug (copies dragged onto
  one point). Fix by offsetting, not by shrinking.
- **Class 1 gaps** *inside* a cluster meant to be continuous read as holes: either
  separate the cluster deliberately (make it two masses) or close the gap.

## Per-asset notes

**Conifers** — expect a stepped/whorled crown: branches attach in rings that shorten
upward but are *not* perfectly regular; crown tip often slightly off-axis; silhouette
serrated, not a smooth cone. Root flare visible at the base in mature trees.

**Broadleaf trees** — crown = a few large lobes with air between them, not one solid
ball; trunk usually leans or forks; branches taper and zigzag.

**Palms** — fronds arc and droop with a clear order (new upright, old hanging); dead
frond skirt on many species; trunk ringed/leaning.

**Rocks/cliffs** — planar facets with 2–3 dominant directions; cracks follow planes;
a pile of identical egg-shaped stones is a failure.

**Terrain/mountains** — drainage logic: ridges and valleys interlock; slopes vary;
perfect bulldoze-smooth or pure-noise surfaces both fail.

**Clouds** — flat-ish bases, cauliflower tops, value gradient bottom→top; cloned puffs
in a row fail.

**Creatures/characters (organic)** — bilateral *overall* but asymmetric in surface
detail: scars, hair parting, muscle tension, pose; check joint bends for candy-wrapper
collapse on frames (see `multi-screenshot.md` for animation).

## Fix vocabulary (universal ops)

From math-symmetry to designed irregularity, in order of leverage:

1. **Delete** 20–40% of cloned elements; keep a hero set.
2. **Move** survivors into clustered positions; break rings and grids (offsets
   0.25–0.5 element radii are typical).
3. **Rotate** with bounded jitter: yaw ±20–40°, tilt ±5–15°.
4. **Scale** along a continuous range (e.g. 0.6–1.4×), with 1–2 oversized heroes.
5. **Deform/reshape** hero elements so no two read as the same primitive.
6. **Add** small filler elements only after the big masses are right.

Then **re-render and re-verify** — irregularity fixes frequently create new gaps,
floaters, or a worse silhouette. Regression-check every time.
