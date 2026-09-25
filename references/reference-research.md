# Reference Research

Goal: give comparisons a factual backbone — **object identity, real-world proportions,
characteristic features, construction, materials, type/species** — not a pile of
visually similar pictures.

## When to research

- Almost always for real-world objects (vehicles, animals, architecture, props,
  furniture, clothing).
- For style targets: gather 2–3 exemplars of the requested game-art style.
- Skip or minimize when: the task is abstract/original (logo, fantasy scene from
  imagination), references were already supplied by the user, or web access is
  unavailable (state this in the report and continue; lower confidence, not standards).

## How many references

**3–6** for most assets. Fewer than 3 risks anchoring on one atypical example; more
than 6 wastes time without changing conclusions. Never treat one image as truth.

## Query templates

Build queries around identity + aspect, not vibes:

| Asset class | Example queries |
|---|---|
| Tree | "lodgepole pine silhouette", "lodgepole pine mature crown structure", "pine trunk bark reference", "<species> winter silhouette no foliage" |
| Vehicle | "1985 Ford F-150 side profile", "F-150 regular cab dimensions wheelbase", "1980s pickup rear three-quarter", "pickup cab bed ratio" |
| Character | "<archetype> anatomy reference", "<era> knight armor construction", "stylized 3D character proportions 6 heads tall" |
| Building | "<style> facade proportions", "<style> roof pitch reference", "<style> window rhythm" |
| Prop | "<object> orthographic view", "<object> exploded view", "<object> materials" |
| Environment | "<biome> ground cover reference", "<style> game environment value composition" |

Add "side view / front view / plan view" to kill perspective distortion when you need
proportions. Add "dimensions / specifications / blueprint / model sheet" when factual
numbers matter.

## What to extract per reference

For each reference, record before closing it:

1. **Identity facts** — species/variant/era/configuration.
2. **2–4 ratios** (unitless: e.g. "crown height ≈ 0.6 × total height"; "wheelbase ≈ 0.62 × overall length"; "8-ft box ≈ 1.35 × cab length").
3. **Defining features list** — the 3–5 things without which it stops being that thing.
4. **Material/color palette** — families, not hex values (unless UI/brand task).
5. **Construction logic** — how parts join (bed bolts to frame, branches whorl from trunk).
6. **Source + URL** and what it is authoritative for.

## Triangulation

Record conclusions only when supported honestly:

- **All/most references agree** → treat as REFERENCE-SUPPORTED.
- **References disagree** (species differences, angle illusions, stylization) → record
  the *range* ("crown ratio varies 0.5–0.7 across species"), pick the interpretation
  consistent with the task, and say so.
- **One reference only supports a claim** → label INFERRED, not REFERENCE-SUPPORTED.

## Source quality

- Factual dimensions/specs: prefer manufacturer data, official documentation, standards bodies, then reputable encyclopedias.
- Visual references: prefer real photos and orthographic model sheets over other
  artists' interpretations (which import someone else's errors).
- AI-generated images are *not* references; they are other outputs.

## Citation discipline

- Cite URLs/sources when the host environment supports it.
- Record `references_used[]` entries in the JSON result mapping each reference to what
  it informed (`used_for`).
- Never claim a web image is *the* original reference unless the user supplied it.
- Distinguish supplied reference images from researched ones in the report.

## Feeding it back into scoring

Reference work feeds: Reference similarity (15% default), Proportions (ratios),
Structure (feature checklist), Materials (palette). In the report's Reference
Comparison section, sort findings into Observed / Reference-supported / Inferred /
Differences — see `assets/templates/verification-report.md`.
