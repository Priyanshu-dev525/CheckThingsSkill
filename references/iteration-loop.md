# The Iteration Loop

Rules for SKILL.md §9. The loop exists to *converge*, not to *redo*. Every cycle must
change either the asset (modification) or the understanding (better diagnosis/new
reference).

## Canonical loop

```
iteration = 1
while True:
    report = inspect_and_score(current_render)     # all ten lenses, SCHEMA-valid result
    if report.score >= threshold and no unresolved CRITICAL:  accept; break
    if iteration == max_iterations:                escalate; break
    if plateau(report, history):                   escalate_or_change_strategy; break
    fixes = prioritize(report.problems)            # repair priority, SKILL.md §8
    modify(asset, fixes)                           # universal ops; keep a change log
    current_render = render_again()                # NEW evidence — mandatory
    regression_check(history[-1], report)          # before continuing
    iteration += 1
```

## Hard rules

1. **New evidence per iteration.** A new score requires a render produced *after* a
   modification. Re-scoring the same pixels with new adjectives is score laundering.
2. **Max iterations = 5 by default.** When hit without passing: report the best
   iteration, list blocking problems by priority, `next_action: escalate_to_user`.
3. **Fix by priority.** Priority 1–5 items (wrong object, silhouette, proportions,
   missing majors, severe intersections) consume early iterations; detail polish is
   never done while they are open.
4. **Change log.** Record per iteration: changes applied → expected visual effect.
   Compare expected vs observed on the next render; mismatches mean your *model of the
   asset* is wrong, not the score.

## Regression check (every iteration after the first)

Compare the new render against the previous one, same views where possible:

- Per-problem status: `unresolved` / `addressed` (fix applied, needs verification) /
  `verified_fixed` (confirmed gone in the new render).
- Did the *targeted* problems improve? By how much (category scores)?
- Did the fix **introduce** anything new? Common transfer failures:
  - moving a part fixes an intersection but creates a floater,
  - scaling fixes proportions but stretches a texture,
  - jittering foliage breaks symmetry but opens holes in a crown,
  - relighting fixes readability but kills the style mood.
- `score_delta = score − previous_score`. Any delta ≤ 0 requires explicit analysis:
  which changes hurt, and why was that not predicted?

## Plateau

Plateau = two consecutive iterations with `score_delta ≤ +0.2` **and** the same
highest-priority problem. Response (pick one, say which):

1. **Change diagnosis** — the problem is being misidentified; re-inspect with a
   fresher lens set or new references.
2. **Rebuild instead of patch** — see below.
3. **Escalate** — evidence or tooling is the blocker; ask the user.

Do not run a 3rd iteration of the same fix recipe.

## Oscillation

Oscillation = a problem is fixed in iteration *n*, broken in *n+1*, "fixed" again in
*n+2* (classic: two coupled parts traded back and forth). Response: treat the coupled
parts as **one** problem, fix them in a single change (e.g. set contact first, then
size), and lock the verified-fixed side from further edits.

## Rebuild trigger

Patching has diminishing returns. Rebuild **primary forms** (not details) when:

- silhouette or proportions are still the top problem after 2 fix attempts directed at
  them, or
- the same CRITICAL survives 2 iterations, or
- the change log shows ≥3 patches fighting each other over the same region.

A rebuild is a new iteration with new evidence — it does not reset the counter — and
the report must say it happened (`Rebuild of primary forms: crown` etc.).

## Ratcheting

When a fix is `verified_fixed`, freeze it: subsequent modifications must not regress
verified areas; the regression check explicitly re-examines them. If a frozen area
regresses, that regression outranks new work.

## Stopping well

On PASS, still record surviving MEDIUM/LOW issues. A PASS means "meets the bar for
this task", not "flawless". Deliver the last two reports (or the final report +
delta) so the user sees convergence, not just the destination.
