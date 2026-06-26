# Workflow scripts

Reusable Workflow scripts. Invoke with `Workflow({ scriptPath: "<abs path>", args: ... })`.

## deep-research-efficient.js

Budget-bounded, model-tiered variant of the built-in `deep-research` skill.

**Why:** the built-in runs every stage (search/fetch/verify/synth) on the capable model with fixed fan-out (6 angles, 15 sources, 25 claims × 3 votes ≈ 100 agents, ~3M tokens). Cost is dominated by `claims × votes`.

**This version:**
- **Model tiering** — search + fetch run on `haiku` + `effort: low` (mechanical); only verify + synthesize use the capable model (judgment).
- **Tunable fan-out** via `mode` or explicit overrides.
- **Hard budget gate** — if the turn has a `+Nk` directive, verification claim count auto-scales to fit `budget.remaining()`.

**Invoke:**
```
Workflow({ scriptPath: ".../scripts/deep-research-efficient.js", args: "your question" })          // balanced
Workflow({ scriptPath: ".../scripts/deep-research-efficient.js", args: { question: "...", mode: "quick" } })
Workflow({ scriptPath: ".../scripts/deep-research-efficient.js", args: { question: "...", votes: 3, claims: 30 } })
```

**Modes** (`angles / fetch / claims / votes`):
| mode | angles | fetch | claims | votes | ~cost vs built-in |
|---|---|---|---|---|---|
| quick | 3 | 8 | 8 | 1 | ~6-10× cheaper |
| balanced (default) | 5 | 12 | 15 | 1 | ~3-4× cheaper |
| thorough | 6 | 15 | 25 | 3 | ≈ built-in (+ haiku savings on search/fetch) |

Explicit args (`angles`, `fetch`, `claims`, `votes`, `question`, `mode`) override the preset.

**Note:** 1-vote verify (quick/balanced) is less robust than 3-vote — a single skeptic can wrongly kill or pass a claim. Use `thorough` or `votes: 3` when correctness of the verdict matters.
