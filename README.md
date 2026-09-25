# ScreenshotSkill

**Visual quality control for AI-generated visuals.** ScreenshotSkill is a
software-independent AI skill that inspects, verifies, compares, scores, diagnoses,
and iteratively improves visual output produced by another AI or pipeline — 3D models,
low-poly assets, game assets, characters, environments, game scenes, buildings,
vehicles, props, terrain, vegetation, procedural assets, UI/game interfaces, renders,
and animation frames.

> A model can open successfully, have valid geometry, the right format, and the right
> polygon count — and still look wrong. ScreenshotSkill exists to catch exactly those
> failures.

## The loop

```
CREATE → RENDER / SCREENSHOT → OBSERVE → UNDERSTAND → FIND REFERENCES
→ COMPARE → SCORE → DIAGNOSE → MODIFY → RENDER AGAIN → VERIFY AGAIN → ACCEPT
```

- **Weighted 0–10 scoring** across 8 visual categories (silhouette, proportions,
  structure, geometry, materials, reference similarity, style, composition), with
  explained penalties for critical visible failures.
- **7.0 acceptance threshold** (customizable per task), blocked by any unresolved
  CRITICAL problem regardless of total.
- **Bounded iteration** (default max 5) with a mandatory before/after regression
  check — scores may only rise on new render evidence.
- **Evidence discipline:** two evidence levels (screenshot-only vs screenshot +
  model data) and strict OBSERVED / INFERRED / REFERENCE-SUPPORTED / RECOMMENDED
  labeling so the agent never claims to see what it cannot.
- **Reference research** via targeted web search, triangulated across multiple
  sources, never a single image treated as truth.
- **Sub-agents optional.** Runs fully solo or orchestrates specialist agents
  (inspection, reference research, geometry QA, style/composition, final judge),
  detecting delegation capability from the host environment.
- **Software-independent.** Speaks universal operations (move, rotate, scale,
  extrude, bevel, assign material, …) — works conceptually with Blender, Maya,
  3ds Max, Houdini, Cinema 4D, Unreal, Unity, Godot, Three.js, OpenSCAD, procedural
  generators, AI image/model generators, or unknown tools.

## Repository layout

```
.
├── SKILL.md                              # Main operational instruction (agent reads this)
├── README.md
├── LICENSE
├── schemas/
│   └── visual-verification.schema.json   # JSON contract for machine-readable results
├── references/
│   ├── visual-analysis.md                # The ten inspection lenses in depth
│   ├── scoring.md                        # Anchors, weights, penalties, worked math
│   ├── reference-research.md             # Finding / triangulating / citing references
│   ├── organic-assets.md                 # Designed irregularity for organic assets
│   ├── geometry-errors.md                # Visible geometry error catalog
│   ├── composition.md                    # Camera, framing, readability
│   ├── iteration-loop.md                 # Loop, regression, plateau, oscillation
│   ├── evidence-and-confidence.md        # Evidence levels and claim labels
│   ├── multi-screenshot.md               # View sets, merging, video frames
│   └── sub-agents.md                     # Optional delegation architecture
├── assets/
│   ├── templates/
│   │   └── verification-report.md        # Fill-in report template
│   └── examples/
│       ├── tree-evaluation.md            # Organic asset, 2 iterations, PASS
│       ├── vehicle-evaluation.md         # Multi-view, reference reconstruction
│       ├── character-evaluation.md       # Level 2 evidence, anatomy weights
│       └── game-scene-evaluation.md      # Scene context, redistributed weights
├── scripts/
│   └── validate_verification.py          # Validates JSON results + markdown reports
└── tests/
    ├── README.md
    └── fixtures/                         # valid-* (must pass) / invalid-* (must fail)
```

## Using the skill

**For an agent:** read `SKILL.md` first (or place this repository in your agent's
skills directory). Follow the intake checklist, run all ten inspection lenses, score
with the weighted table, and emit both a markdown report (from the template) and a
JSON result (conforming to the schema) for every evaluation. Deep-dive rules live in
`references/`; consult them when a case needs more than the core instructions.

**For a human:** give the agent the original task text plus one or more screenshots or
renders. Optionally provide references and evaluation criteria. The agent returns a
structured Visual Verification Report with a 0–10 score, evidence-labeled findings,
prioritized fixes, and a PASS / REWORK REQUIRED decision.

## Validating results

```bash
# Validate a machine-readable JSON result against the schema + consistency rules
python3 scripts/validate_verification.py result.json

# Validate a markdown verification report (sections, table math, status logic)
python3 scripts/validate_verification.py --report assets/examples/tree-evaluation.md

# Run the full self-test (fixtures + all example reports)
python3 scripts/validate_verification.py --self-test
```

The validator is dependency-free (Python 3.8+ standard library). Consistency checks
include: weights sum to 1, stated score matches the weighted math minus penalties,
status agrees with score vs threshold, unresolved CRITICALs block PASS, iteration is
within bounds, and `score_delta` matches `previous_score`.

## Defaults

| Setting | Default | Notes |
|---|---|---|
| Acceptance threshold | 7.0 / 10 | Task may set a stricter value; document it. |
| Max iterations | 5 | Hard bound; stop conditions are mandatory. |
| Category weights | See `SKILL.md` §7 | Custom weights allowed with justification. |
| Penalty total cap | 3.0 points | Each penalty 0.25–1.5, always explained. |
| Evidence level | Level 1 | Level 2 only when model/scene data is supplied. |

## License

MIT — see [LICENSE](LICENSE).
