# Tests — ScreenshotSkill

Fixtures in `fixtures/` pin the behavior of `scripts/validate_verification.py`:

- `valid-*.json` — must validate with **zero errors** (schema + consistency rules).
- `invalid-*.json` — must be **rejected** (each demonstrates one failure class):

| Fixture | Failure demonstrated |
|---|---|
| `invalid-missing-required.json` | Schema: missing required properties (`status`, `iteration`, `evidence_level`, `problems`, `next_action`). |
| `invalid-category-range.json` | Schema: category score above the 0–10 bound (anti-inflation bound). |
| `invalid-status-score-mismatch.json` | Consistency: `status: pass` with `score < threshold`. |
| `invalid-bad-weights.json` | Consistency: category weights do not sum to 1.00. |
| `invalid-wrong-score-math.json` | Consistency: stated score does not equal the weighted total (score laundering detection). |

Run the whole suite (fixtures + the four worked example reports in
`assets/examples/`):

```bash
python3 scripts/validate_verification.py --self-test
```

Expected output ends with `SELF-TEST PASSED` and exit code 0. The same command runs
in CI on every push and pull request (`.github/workflows/self-test.yml`).

Ad-hoc usage:

```bash
python3 scripts/validate_verification.py result.json          # JSON result
python3 scripts/validate_verification.py --report report.md   # markdown report
python3 scripts/validate_verification.py --schema-only x.json # schema only, no math
```
