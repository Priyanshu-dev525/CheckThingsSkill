# Composition, Framing & Readability

Two distinct jobs share this lens:

1. **Review captures** — screenshots *you* (or the generating agent) take so the asset
   can be verified. Bad capture = bad evidence.
2. **Scene composition** — evaluating a game scene / final image *as* an image, where
   composition is part of the deliverable.

Do not conflate them: a beautifully moody scene render can be terrible verification
evidence, and a neutral review render can be a badly composed scene.

## Part 1 — Review capture conventions

**For single assets / props / vehicles:**
- ¾ perspective at ~20–40° elevation as the hero view.
- Orthographic front / side / top when proportions are under test.
- Subject fills 60–80% of the frame; whole subject inside the frame with margin.
- Ground/shadow contact visible (floating-vs-standing is a top failure class).
- Neutral environment: mid-grey background, no same-value backdrop behind dark assets.
- Neutral lighting: soft key from upper front-left + fill + rim; no colored lights, no
  heavy vignette. Mood lighting *hides* geometry.
- One asset per capture unless the task is an arrangement.

**For characters:**
- Eye-level camera; full body in frame; A/T-pose or neutral stance for structure, plus
  one posed view for appeal; front / side / back / ¾ set (see `multi-screenshot.md`).

**For UI:**
- Capture at target resolution, unscaled (no browser zoom); include the states the
  task names (hover/pressed/disabled where applicable); check alignment against the
  pixel grid, contrast of text over backgrounds, and truncation/overflow.

If a capture request fails the image-quality pre-check (SKILL.md §3), send back a
corrected capture request using these conventions instead of interpreting a bad image.

## Part 2 — Scene composition checks

Evaluate in this order (matches the repair-priority philosophy: big things first):

1. **Focal point** — can you point at where the eye should land? Is it supported by
   value contrast, saturation, detail density, or framing? Missing focal point is HIGH
   for scenes.
2. **Value grouping** — squint test: do the big value masses separate foreground /
   midground / background? Mud = everything mid-grey.
3. **Readability at gameplay size** — shrink the screenshot to actual gameplay
   footprint (e.g. 25% for a strategy view). If units/exits/interactables vanish,
   readability fails regardless of beauty.
4. **Leading lines & flow** — do roads, rivers, sight-lines pull toward the focal
   point or out of the frame?
5. **Scale continuity** — comparative sizes of repeated elements (trees near vs far)
   must respect perspective; a far tree larger than a near one breaks depth.
6. **Background noise** — detail density competing with the subject; flatten/fog it.
7. **Color direction** — one dominant temperature/palette with a controlled accent;
   rainbow-equal emphasis fragments the scene.

## Scene-specific failure signatures

- **Everything equally detailed** → no hierarchy; reduce detail density away from the
  focal point before adding anything.
- **Horizon dead-center, subject dead-center, symmetry dead-center** → static and
  accidental; only religious/formal symmetry survives centering.
- **Edge tangent pile-ups** — objects kissing the frame edge or each other's contours;
  ask for small moves (0.5–2% of frame) to resolve tangents.
- **Sky/ground split 50/50** with no value difference between them.

## Communication rule

Composition fixes are moves, not adjectives. "Strengthen the focal point" is a wish;
"desaturate and darken the background islands by ~20% and add a rim light on the main
island's east edge so the eye lands there first" is a fix.
