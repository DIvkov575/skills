# Workflow scripts

Reusable Workflow scripts. Invoke with `Workflow({ scriptPath: "<abs path>", args: ... })`.

## deep-research-efficient.js

Budget-bounded, model-tiered variant of the built-in `deep-research` skill.

**Why:** the built-in runs every stage (search/fetch/verify/synth) on the capable model with fixed fan-out (6 angles, 15 sources, 25 claims × 3 votes ≈ 100 agents, ~3M tokens). Cost is dominated by `claims × votes`.

**This version:**
- **Model tiering** — search + fetch run on `haiku` + `effort: low` (mechanical); only verify + synthesize use the capable model (judgment).
- **Two-stage escalating verification** — a cheap 1-vote *screen* on all claims; only screen-survivors escalate to a full `votes`-majority. Cost ≈ `claims + survivors*(votes-1)` instead of `claims*votes` flat. Keeps robustness (no lone skeptic passes a claim into the report) while paying extra votes only on claims that would actually appear.
- **Tunable fan-out** via `mode` or explicit overrides.
- **Hard budget gate** — if the turn has a `+Nk` directive, verification claim count auto-scales to fit `budget.remaining()` (accounts for escalation's average cost).

**Invoke:**
```
Workflow({ scriptPath: ".../scripts/deep-research-efficient.js", args: "your question" })          // balanced
Workflow({ scriptPath: ".../scripts/deep-research-efficient.js", args: { question: "...", mode: "quick" } })
Workflow({ scriptPath: ".../scripts/deep-research-efficient.js", args: { question: "...", votes: 5, claims: 30 } })
```

**Modes** (`angles / fetch / claims / votes`; `votes` = total an escalated claim receives):
| mode | angles | fetch | claims | votes | ~cost vs built-in |
|---|---|---|---|---|---|
| quick | 3 | 8 | 8 | 3 | ~4-6× cheaper |
| balanced (default) | 5 | 12 | 15 | 3 | ~2-3× cheaper |
| thorough | 6 | 15 | 25 | 5 | ≈ built-in, stronger verdicts |

Explicit args (`angles`, `fetch`, `claims`, `votes`, `question`, `mode`) override the preset.

**Robustness:** every surviving claim gets a real majority vote (≥3), so a single skeptic can never pass a bad claim into the report. The savings come from killing weak claims at the 1-vote screen (cheap and safe — the verifier defaults to refute when uncertain, so a lone kill is conservative), not from under-verifying what survives. Set `votes: 1` only if you explicitly want a fast, low-confidence scan.
