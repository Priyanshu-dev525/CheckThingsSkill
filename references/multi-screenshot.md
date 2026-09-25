# Multi-Screenshot & Video Evaluation

Multiple views make you *more* accurate only if you merge them into **one** model of
the asset. Different cameras are different looks at one object — never score them as
separate objects and average.

## Recommended view sets (request these when evidence is thin)

| Asset class | Views |
|---|---|
| Prop / vehicle / building | front · back · left · right · top · ¾ perspective (~20–40° elevation) |
| Character | front · side · back · ¾ front; eye-level; plus one posed view if appeal matters |
| Organic asset (tree, rock) | two perpendicular sides + ¾; foliage also from below if the canopy matters |
| Game scene | establishing view · gameplay camera (the view players actually get) · 1–2 detail close-ups of focal areas |
| UI | full screen at target resolution + state captures the task names (hover/pressed/disabled/error) |
| Animation | frames at start / middle / end + 2–4 random samples; plus consecutive frames around fast motion |

## Merging evidence into one model

1. **Correspondence first:** identify the same landmark in every view (that bump on
   the left fender = that bump on the ¾ view). If a landmark can't be matched, suspect
   a view-dependent artifact, not a new feature.
2. **Triangulate proportions:** a ratio must survive across views. Something that
   looks elongated in side view and normal in front view is *deep*, not elongated.
3. **Track contact:** a part in class-2 contact in one view but floating in another
   is floating — the generous view is lying to you via perspective.
4. **Aggregate problems once:** an issue visible in 3 views is one problem with 3
   evidence lines, not 3 problems inflating the list.

## Contradictions (flag explicitly)

- **Feature appears/vanishes between views** → likely z-fighting, backface culling,
  or a renderer visibility bug. Severity at least MEDIUM; request a moving frame or
  wireframe if available.
- **proportions disagree between orthographic views** → the model, not the camera, is
  wrong (camera orthos don't lie); treat as a real proportion defect.
- **material changes color between views** → lighting/environment influence or
  view-dependent shading; isolate with a neutral-light capture before judging
  materials.

Record the merged view in `views_analyzed[]` and the reconciliation in
`confidence_notes`.

## Video / animation frames

Frame sampling: start, middle, end, + 2–4 random frames + consecutive pairs around
fast motion. Beyond the ten static lenses, check:

- **Foot/contact sliding** — planted feet shift across ground between frames.
- **Clipping during motion** — parts coincide only mid-animation (cape through leg,
  door through fender). Class 5 where visible.
- **Deformation artifacts** — candy-wrapper forearm collapse, shoulder tearing,
  volume loss at extreme poses.
- **Intersection popping** — class changes between adjacent frames (2 → 5 → 2).
- **Temporal shimmer** — texture/shadow crawl, z-fighting flicker caught by comparing
  consecutive frames.

Severity weights motion failures like structural ones: a walk cycle with sliding feet
is HIGH even if every still frame is handsome — the *asset-in-use* is what matters.

## Before/after (regression) pairs

For regression checks use the **same view, same lighting, same framing**; otherwise
differences may come from the camera, not the change. If a capture convention changed
mid-loop, note it and capture both conventions once to re-baseline.
