# Visible Geometry Error Catalog

Geometry claims from screenshots are Level 1 evidence: report only what is visible,
with wording like "Visible evidence suggests…". Exact topology statements require
model data (Level 2). Intersections use the 5-class scale in `visual-analysis.md`.

| # | Error | Visual signature in a screenshot | Typical severity | Level 1 wording | Typical fix (universal ops) |
|---|---|---|---|---|---|
| 1 | Floating part | Part hovers with visible air/shadow gap where contact is expected (mirror off door, foliage off trunk) | HIGH (LOW if tiny trim) | "OBSERVED: the antenna hovers ~2% of body height above the fender with no contact point." | Move into class-2 contact; or delete; or add connector |
| 2 | Detached component | Subassembly clearly separate from the body it must join | HIGH | "OBSERVED: crown masses hang clear of the trunk, no branch connects them." | Move/merge onto parent; add connecting geometry |
| 3 | Shallow overlap (cluster) | Kissing intersections inside foliage/rock masses | Acceptable (class 3) | "OBSERVED: shallow mutual overlap, reads as one mass." | None, unless repeated everywhere |
| 4 | Suspicious overlap | Penetration deeper than a kiss, intent unclear | MEDIUM–HIGH | "Visible evidence suggests the bed sides penetrate the cab back by roughly a quarter of their thickness." | Offset along contact normal; reshape contact area |
| 5 | Severe intersection | Parts pass deeply through each other (wheel through fender, sword through hand) | HIGH–CRITICAL + penalty 0.5–1.0 | "OBSERVED: the front wheel passes through the fender arch by ≈40% of wheel radius." | Reposition to class 2 contact; rescale offender; then re-render |
| 6 | Z-fighting | Flickering/striped/moiré surfaces where two faces are coplanar; changes between frames/views | MEDIUM (HIGH if large) | "OBSERVED: striped shimmer on the side plane, consistent with coplanar duplicate faces." | Offset one face slightly; delete duplicate |
| 7 | Duplicate geometry | Doubled edges, shading doubling, same element twice in one spot (ghost foliage) | MEDIUM | "Visible evidence suggests two identical canopy cards stacked at one point." | Delete duplicate; check instance counts |
| 8 | Accidental hole | Background visible through the body where solid surface is expected | HIGH | "OBSERVED: sky visible through the torso at the left shoulder." | Merge/weld gap; reshape patch |
| 9 | Inverted/flipped faces | Black or inside-out shaded patches among correctly lit neighbors | MEDIUM–HIGH | "Visible evidence suggests inverted faces on the fender's underside (black patch)." | Flip/reorient offending faces; recheck shading |
| 10 | Topology pinching / shading tear | Star-shaped pinching, long shading streaks across what should be smooth | MEDIUM | "Visible evidence suggests pole pinching at the hood's front corner." | Reflow topology around the pinch; broaden bevel |
| 11 | Ground clipping | Contact line sinks below the ground plane; objects 'stand in' the floor | MEDIUM–HIGH | "OBSERVED: tires sink ≈15% of their diameter into the ground plane." | Move up to class-2 contact; or drop ground |
| 12 | Camera clipping | Subject cut by the frame or near plane | Evidence problem, not asset problem | "Area not visible — cropped by frame." | Adjust camera; re-capture (see `composition.md`) |
| 13 | Scale inconsistency | Components sized for different scales (giant door handle, toy wheels) | MEDIUM–HIGH | "OBSERVED: door handle height ≈ 25% of door height; typical is far smaller." | Rescale component to ratio from reference |
| 14 | Unintended facets | Visible polygon edges on objects that should be smooth for the brief | LOW–MEDIUM (fine if low-poly brief) | "OBSERVED: 16-sided faceting on a barrel that the realistic brief expects smooth." | Subdivide/bevel; or accept if low-poly style |
| 15 | Stretched texture/mapping | Surface pattern smeared along one axis, density changes abruptly | MEDIUM | "OBSERVED: wood grain stretched vertically on the trunk relative to branches." | Fix mapping/unwrap scale on the stretched region |
| 16 | Merged-into-void | Part ends inside another with no believable joint (arm enters torso) | MEDIUM–HIGH | "Visible evidence suggests the forearm terminates inside the torso with no shoulder structure." | Reshape joint; add connecting forms |

## Using the catalog

1. Scan the whole asset per row (#1–#9 first; they are the most damning).
2. Classify each hit by intersection class and severity; severe intersection (#5) is
   penalty-eligible (see `scoring.md`).
3. Write fixes as universal ops with relative magnitudes.
4. After any geometry fix, re-render from the **same** view (regression check) **and**
   one other view — geometry fixes love to break a side you were not watching.

## Evidence limits (do not cross)

- Never claim non-manifold geometry, exact vertex/weld counts, or backside state from
  a screenshot. Those require mesh inspection → request model data (Level 2) or say
  "Insufficient visual evidence."
- A flicker between two frames *suggests* z-fighting or duplicates; a single still
  shows only the shimmer pattern — phrase accordingly.
