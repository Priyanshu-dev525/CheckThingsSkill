# Example: Inventory Screen UI (game interface, UI weight preset, 1 iteration shown)

Demonstrates: the UI presets from `references/scoring.md` (readability-led weights),
how the ten lenses adapt to a 2D interface, honest handling of uncaptured UI states
("area not visible"), and a REWORK verdict that preserves what works.

---

# Visual Verification Report

**Asset:** Fantasy RPG inventory screen (full-screen capture)
**Task:** "Design an inventory screen for a fantasy RPG: item-slot grid, item detail panel, gold counter, readable at 1080p, dark-fantasy hand-painted style."
**Evidence level:** Level 1 — screenshot only (one static state)
**Views analyzed:** single full-screen 1920×1080 capture, 100% scale
**References used:** 2 — dark-fantasy game UI exemplar sheet (style target); handheld-era inventory screen anatomy reference (component expectations)

## Result

Status: REWORK REQUIRED
Score: 6.6 / 10
Threshold: 7.0
Iteration: 1 / 5
Previous score: none — first evaluation
Score delta: n/a
Weighted total: 6.60
Penalty total: 0.00

## Scoring Weights

Custom weights (UI preset): silhouette 5%, proportions 15%, structure 20%, geometry
5%, materials 10%, reference similarity 10%, style 10%, composition 25%.
Justification: UI tasks live or die on readability (composition) and required
component completeness (structure). Lens mapping for 2D: *silhouette* = panel/layout
blocking; *proportions* = grid rhythm, alignment, spacing; *geometry* = rendering
integrity (overlaps, truncation, clipping of text/icons).

## Category Scores

| Category | Score | Weight | Evidence |
|---|---:|---:|---|
| Silhouette | 8.0/10 | 5% | Panel blocking reads instantly: grid left, detail panel right, gold top-right; layout skeleton survives the thumbnail test. |
| Proportions | 6.5/10 | 15% | Grid rows 1–3 are evenly spaced; row 4 sits ~half a slot lower, breaking the vertical rhythm; detail-panel margins inconsistent left vs right. |
| Structure | 7.0/10 | 20% | All three brief-listed components present (grid, detail panel, gold counter); slot count and tab bar match brief; no scroll affordance for overflow shown. |
| Geometry | 6.0/10 | 5% | Gold icon overlaps the leading digit of the counter; no other rendering damage visible; text edges crisp at 100% scale. |
| Materials | 7.5/10 | 10% | Parchment/leather/iron families separate clearly; frames and fills read as intended families at target resolution. |
| Reference Similarity | 7.0/10 | 10% | Panel vocabulary (framed grid + side detail card) matches both references; exemplar uses stronger value separation between interactive vs decorative frames. |
| Style | 7.0/10 | 10% | Hand-painted dark-fantasy read works; two "rare" items show different border treatments — rarity coding inconsistent (see Problems). |
| Composition | 5.5/10 | 25% | Tooltip body text sits ~40% grey on ~50% grey parchment — fails the thumbnail test into an unreadable smear; hierarchy otherwise sound. |

## What Is Working

- Layout skeleton is right on the first attempt: grid/detail/gold zones are where a
  player expects them, confirmed against the anatomy reference.
- Text rendering at 100% scale is crisp — no scaling artifacts at target resolution.
- Material families (parchment vs leather vs iron) separate cleanly in greyscale.

## Problems

### [HIGH] Tooltip/body text contrast is unreadable at gameplay distance
- **Evidence:** OBSERVED — body copy ≈40% value on ≈50% value parchment; at 25% shrink (gameplay-distance simulation) the text field collapses into texture; REFERENCE-SUPPORTED — the style exemplar keeps body text ≥3 value-steps off its background.
- **Affected area:** detail panel tooltip/body text (center-right of screen).
- **Likely cause:** INFERRED — text color sampled for mood without a contrast floor.
- **Recommended fix:** RECOMMENDED — raise body text to ≥85% value (or darken its parchment field ~15%) and re-run the 25% shrink check before re-render.
- **Status:** unresolved

### [MEDIUM] Grid row 4 misaligned by ~half a slot
- **Evidence:** OBSERVED — rows 1–3 share one Y rhythm; row 4 drops ≈0.5 slot height, visibly kinking the column gutters at full resolution.
- **Affected area:** item grid, bottom row.
- **Likely cause:** INFERRED — row offset typo or an unpaired header margin.
- **Recommended fix:** RECOMMENDED — snap row 4 to the shared row pitch; verify gutter lines run unbroken down all four rows.
- **Status:** unresolved

### [MEDIUM] Gold icon overlaps the leading digit
- **Evidence:** OBSERVED — the coin icon's rim cuts into the first digit of "12,460" at current counter width.
- **Affected area:** gold counter, top-right.
- **Likely cause:** INFERRED — fixed icon-text gap sized for a 3-digit value.
- **Recommended fix:** RECOMMENDED — add a fixed minimum gap (≈0.5 icon width) and anchor text right so digit growth expands leftward away from the icon; test a 6-digit value.
- **Status:** unresolved

### [LOW] Rarity color coding applied inconsistently
- **Evidence:** OBSERVED — two items both labeled "Rare" in their tooltips carry different border treatments (blue glow vs plain iron).
- **Affected area:** item slots (rarity borders).
- **Likely cause:** INFERRED — legacy slot frame reused for one of the items.
- **Recommended fix:** RECOMMENDED — unify rarity → border mapping; re-check all rarity tiers in one pass.
- **Status:** unresolved

## Reference Comparison

### Observed
Grid + side detail card + top-right counter; hand-painted frames; value structure strong except the tooltip field; row-4 kink; icon/digit overlap; inconsistent rare borders.

### Reference-supported
Exemplar and anatomy reference agree on: grid-left/detail-right zoning, counter top-right, and a ≥3-step value gap between body text and its field. Exemplar uses per-rarity border coding consistently.

### Inferred
The unreadable tooltip may read acceptably on a dim OLED living-room screen — but at the brief's own target (1080p readable) the current values fail the shrink test; treat as a defect, not a taste call.

### Differences
- Body-text value gap below reference floor (HIGH) · interactive vs decorative frame separation weaker than exemplar (LOW, folded into style) · rarity coding inconsistent vs exemplar (LOW).

## Required Changes

1. Fix tooltip/body text contrast (priority 1 — the brief says "readable"): text to ≥85% value or field ~15% darker; verify at 25% shrink.
2. Snap grid row 4 to the shared row pitch; restore unbroken gutters.
3. Re-anchor the gold counter (min gap, right-anchored text); verify with a 6-digit value.
4. Unify rarity border coding across all tiers.
5. Re-capture INCLUDING one hover state (tooltip open on a rare item) — current capture lacks any interactive state (area not visible this iteration).

## Verification Decision

REWORK REQUIRED — readability is the task's headline requirement and it currently fails on the tooltip text. Apply changes 1–4, capture per change 5 (with a hover state), and re-evaluate (iteration 2/5). The layout skeleton is good — do not redesign it while fixing contrast.

```json
{
  "schema_version": "1.0",
  "asset": "fantasy RPG inventory screen",
  "task_summary": "Design an inventory screen for a fantasy RPG: item-slot grid, item detail panel, gold counter, readable at 1080p, dark-fantasy hand-painted style.",
  "status": "rework_required",
  "score": 6.6,
  "threshold": 7.0,
  "iteration": 1,
  "max_iterations": 5,
  "evidence_level": "level_1_screenshot_only",
  "views_analyzed": ["full-screen 1920x1080, 100% scale"],
  "categories": {
    "silhouette": 8.0,
    "proportions": 6.5,
    "structure": 7.0,
    "geometry": 6.0,
    "materials": 7.5,
    "reference_similarity": 7.0,
    "style": 7.0,
    "composition": 5.5
  },
  "weights": {
    "silhouette": 0.05,
    "proportions": 0.15,
    "structure": 0.20,
    "geometry": 0.05,
    "materials": 0.10,
    "reference_similarity": 0.10,
    "style": 0.10,
    "composition": 0.25
  },
  "custom_weights_rationale": "UI task: readability (composition .25) and component completeness (structure .20) lead; 2D lens mapping: silhouette=layout blocking, proportions=grid rhythm/alignment, geometry=rendering integrity (overlaps, truncation).",
  "penalties": [],
  "problems": [
    {
      "severity": "high",
      "category": "composition",
      "issue": "Tooltip/body text contrast unreadable at gameplay distance",
      "evidence": "OBSERVED: body copy ~40% value on ~50% value parchment; collapses at 25% shrink; REFERENCE-SUPPORTED: exemplar keeps >=3 value-step separation",
      "affected_area": "detail panel tooltip/body text",
      "likely_cause": "text color chosen for mood without a contrast floor",
      "recommended_fix": "Raise body text to >=85% value or darken field ~15%; re-verify at 25% shrink",
      "status": "unresolved"
    },
    {
      "severity": "medium",
      "category": "proportions",
      "issue": "Grid row 4 offset ~half a slot below the shared row pitch",
      "evidence": "OBSERVED: column gutters kink at row 4 at full resolution",
      "affected_area": "item grid, bottom row",
      "likely_cause": "row offset typo or unpaired header margin",
      "recommended_fix": "Snap row 4 to shared pitch; verify unbroken gutters",
      "status": "unresolved"
    },
    {
      "severity": "medium",
      "category": "geometry",
      "issue": "Gold icon overlaps the leading counter digit",
      "evidence": "OBSERVED: coin rim cuts into first digit of '12,460'",
      "affected_area": "gold counter, top-right",
      "likely_cause": "fixed icon-text gap sized for 3 digits",
      "recommended_fix": "Add min gap ~0.5 icon width; right-anchor text; test 6-digit value",
      "status": "unresolved"
    },
    {
      "severity": "low",
      "category": "style",
      "issue": "Rarity border coding inconsistent between two 'Rare' items",
      "evidence": "OBSERVED: blue-glow vs plain-iron borders on two items both labeled Rare",
      "affected_area": "item slot frames",
      "likely_cause": "legacy frame reused for one slot",
      "recommended_fix": "Unify rarity-border mapping across all tiers",
      "status": "unresolved"
    }
  ],
  "what_is_working": [
    "Layout skeleton matches player expectations (grid left, detail right, gold top-right)",
    "Crisp text rendering at 100% target resolution",
    "Material families separate cleanly in greyscale"
  ],
  "required_changes": [
    "Raise tooltip body text to >=85% value (or darken field ~15%); verify at 25% shrink",
    "Snap grid row 4 to the shared row pitch",
    "Re-anchor gold counter with min gap and right-anchored text; test 6 digits",
    "Unify rarity border coding; re-capture including one hover state"
  ],
  "references_used": [
    {
      "title": "Dark-fantasy game UI exemplar sheet",
      "kind": "artwork",
      "used_for": "style target, >=3 value-step text/field separation, rarity border coding"
    },
    {
      "title": "Inventory screen anatomy reference",
      "kind": "diagram",
      "used_for": "component expectations: grid/detail/counter zoning"
    }
  ],
  "confidence_notes": "Single static state only: hover/pressed/disabled/drag states are area-not-visible this iteration — no claims made about them; capture of one hover state requested in Required Changes. Contrast measured in value steps, not WCAG ratios.",
  "next_action": "modify_and_rerender"
}
```
