# Sub-Agent Orchestration (OPTIONAL)

Sub-agents are a convenience, never a dependency. Everything they do, the main agent
can do solo, in the same order, with identical quality. **Never block on delegation.**

## Step 0 — detect capability (do not assume)

Treat delegation as available only when the host environment documents or exposes a
task/spawn/delegate mechanism you can actually invoke. Writing a prompt addressed to
a sub-agent proves nothing — unread prompts are the classic failure. If capability is
unknown → assume **absent** → solo mode. Record the mode in your process notes.

## Architecture (delegation mode)

```
MAIN AGENT (owns: task contract, modifications, re-rendering, the loop, the decision)
 │
 ├─ Visual Inspection Agent       first-pass findings across the ten lenses
 ├─ Reference Research Agent      sourced references + extracted facts (ratios, defining features)
 ├─ Geometry/Structure QA Agent   intersections, floaters, missing/misplaced parts
 ├─ Style/Composition Agent       style match, framing, readability, value structure
 └─ Final Judge                   merges all findings, dedupes, resolves conflicts, scores
```

Loop position: sub-agents analyze **after each new render**; the main agent applies
fixes, re-renders, and re-convenes them. Sub-agents never modify the asset and never
see each other's drafts (independent first, merged by the Judge — this avoids
groupthink).

## Role contracts

| Agent | Input contract | Output contract |
|---|---|---|
| Visual Inspection | screenshot(s) + task text + view labels | findings list: `[lens] OBSERVED/INFERRED claim (+severity hint)`; no scores |
| Reference Research | object identity + task text | 3–6 references: title, URL, kind, extracted ratios, defining-features list, disagreements |
| Geometry/Structure QA | screenshot(s) + (if Level 2) mesh/scene data | classified intersections (1–5), floaters/holes/missings, each with evidence + severity hint |
| Style/Composition | screenshot(s) + style brief | style deltas, composition issues, readability notes, suggested capture improvements |
| Final Judge | all of the above + weights + threshold | schema-conformant JSON result + penalties with rationales |

Roles may be merged when delegation slots are scarce (Inspection+Geometry is the
natural pairing; Style+Judge also merges well). Do not delegate a trivial asset at
all — solo costs less.

## Conflict resolution (Final Judge rules)

1. **Evidence beats hierarchy:** an OBSERVED claim from the junior role outranks an
   INFERRED claim from anyone.
2. **Label strictly:** unsupported certainty gets downgraded to INFERRED or dropped.
3. **Dedupe:** same defect reported by two roles = one problem with two evidence
   lines.
4. **Disagreement on a score-relevant fact** (e.g. "intersection vs contact") →
   score conservatively (the less flattering reading) and note the disagreement in
   `confidence_notes`.
5. **The Judge scores independently** of role opinions; roles propose, the Judge
   disposes — no averaging of role-given scores.

## Solo mode (no delegation)

The main agent performs the roles sequentially, in this order:

1. Reference research (so comparisons exist before judgments).
2. Visual inspection across all ten lenses.
3. Geometry/structure QA pass (dedicated intersection scan).
4. Style/composition pass.
5. Self-judge: score, penalties, decision — explicitly re-reading findings for
   evidence labels before committing numbers.

Skipping role steps because "one brain did it all" is how lenses get missed; the
sequence is enforced in solo mode too.

## Anti-gaming additions for delegation

- A sub-agent must never see the current running score (prevents anchoring).
- The Judge must publish per-category *evidence lines*, not just numbers.
- Re-convening sub-agents on the **same unchanged render** is forbidden (anti-gaming
  rule 3 in SKILL.md).
