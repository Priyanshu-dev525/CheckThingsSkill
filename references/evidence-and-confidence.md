# Evidence & Confidence

The skill's credibility rests on never claiming more than the evidence supports.
This file defines the levels, the labels, and the banned moves.

## Evidence levels

**LEVEL 1 — Screenshot only** (default)

| You MAY evaluate | You may NOT claim |
|---|---|
| Visible silhouette, major masses, outline proportion | Exact real-world dimensions ("it is 4.2 m tall") |
| Approximate *ratios* between visible parts ("wheel ≈ 0.22 of length") | Absolute measurements of anything (pixels carry no units) |
| Materials/colors as they *appear* | Material parameter values ("roughness 0.4") |
| Composition, framing, readability | Performance, memory, or poly counts |
| *Visible* intersections, floaters, holes, artifacts | Hidden/backside/interior geometry state |
| Style match, reference similarity, task compliance | Topology quality (edge flow, non-manifold) except where a shading artifact is *visible* |

**LEVEL 2 — Screenshot + model data** (only when actual model/scene data is supplied:
dimensions, triangle counts, hierarchy, transforms, material parameters, bounding
boxes)

Everything in Level 1, plus: exact dimensions and ratios · triangle/vertex counts ·
topology facts from the data · transforms and pivots · intersections computable from
bounding/mesh data (including hidden ones) · material parameter values · scene
structure. Still label which claims come from rendering vs from data.

**Promotion rule:** screenshot-only + assumptions ≠ Level 2. If data is missing for a
claim you need, request it (`next_action: request_more_evidence`) or downgrade the
claim to INFERRED.

## Claim labels (use verbatim)

- **OBSERVED** — directly visible: "OBSERVED: 8 crown masses evenly spaced around the
  trunk axis."
- **INFERRED** — reasoned: "INFERRED: the radial arrangement suggests array/duplicate
  placement rather than authored placement."
- **REFERENCE-SUPPORTED** — backed by a named reference: "REFERENCE-SUPPORTED (USDA
  silhouette sheet): mature lodgepole crowns occupy 40–60% of tree height."
- **RECOMMENDED** — the fix: "RECOMMENDED: delete 3 of the 8 masses and jitter the
  rest 10–20° in yaw."

Never let an INFERRED claim shed its label when quoted later in the report or in
follow-up iterations. Inference drift ("we established the array was random" — you
established nothing) is the main way evaluators hallucinate certainty.

## Confidence

Attach high/medium/low where it matters (e.g. in `confidence_notes`):

- **High** — multiple clear views or Level 2 data.
- **Medium** — one clear view; minor hidden areas.
- **Low** — small/blurry subject, heavy occlusion, no references available.

Low confidence is a reason to request more evidence, **not** a reason to lower the
bar or to soften a decision into a pass.

## Required honest phrases (use these exact forms)

- "Insufficient visual evidence to evaluate X." (resolution/occlusion/angle)
- "Area not visible in the provided screenshot(s)." (hidden side/interior)
- "No external reference verification was available." (no web access)
- "Visible evidence suggests …" (Level 1 geometry suspicion)

## Image-quality pre-check (gate before lens 1)

1. Subject ≥ ~40% of frame height? Sharper than soft blur? Not cropped mid-subject
   (unless that region is the subject)? Separable from background in value?
2. Lighting: forms readable, no crushed blacks/blown highlights over the subject?
3. If any check fails → stop, request a corrected capture (conventions in
   `composition.md`), `next_action: request_more_evidence`. Do not analyze a bad
   image and pretend the analysis is real.

## What you may NEVER do

- Invent detail, components, or references you cannot see/cite.
- Convert pixel distances into real-world units.
- Claim "the mesh is clean" from a pretty render.
- Treat your own generated texture/material *settings* as observed *appearance*.
- Upgrade certainty across iterations without new evidence.
