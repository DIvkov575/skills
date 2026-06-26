---
name: research-gate
description: Use when converging a list of candidate ML research directions to a go/no-go — the convergent half of research selection. Escalating filters cheapest-first, from literature checks through actually-run MVP falsifiers and metric-first kill gates, with explicit pivot/double-down. Pair with research-fanout for generation.
---

# Research Gate

Convergent triage. Convergence is **empirical, not just literature filtering** — you converge by *cheaply trying things and killing on evidence*. Effort ∝ 1/confidence: the cheapest experiment that could kill a candidate runs before any expensive one. Killing a candidate early and cheap is success, not failure.

## Input

`$ARGUMENTS` = a candidate list (e.g. from `research-fanout`), or a single direction to vet. If empty, ask for candidates.

## Hard reflexes (the gate exists because these were violated before)

- **Metric before method.** Build + sanity-check the eval metric BEFORE implementing the method. (Loss on the wrong tokens once faked 39–47% "wins".)
- **Too-good is a bug.** Any first-run improvement >10–15% triggers a mandatory adversarial audit before you believe it.
- **Pre-register the gate.** Write metric + threshold + scale BEFORE running. The urge to edit a gate after seeing results = the result is negative.
- **Cheap kill beats expensive kill.** A direction killed at the literature filter for ~$0 beats one killed after a multi-hour run.

## Stage A — Literature filters (cheapest, no code; each candidate must survive ALL)

Run per candidate, cheapest sub-check first:
1. **Triviality** — write the core method as pseudocode. <10 lines + direct port of an existing technique → thin wrapper. Kill.
2. **Scoop/redundancy** — run `deep-research-efficient` (`thorough` mode) on "does <candidate> already exist; who's active in this area, last 12mo". Exact contribution exists, or 3+ active groups → kill (unless a specific unfair advantage).
3. **Thin contribution** — would a top reviewer call it incremental ("combined more X", ablation table, +1 dataset)? Demand a mechanism/result that changes thinking.
4. **Winnability** — name the *specific experiment* that, if it works, gives an edge on budget (1 GPU, weeks, no from-scratch pretraining). Edge = "nobody tried it" → ask *why*; absence is usually a signal, not an opening.

Survivors get a 3–5 sentence dossier: contribution / closest prior art + our delta / the winnable experiment / the risk. **Bring 1–3 survivors to the user for an explicit pick before spending compute.** Zero survivors → report that; concluding "none clear the bar" is a valid, valuable outcome — do not soften it to keep a project alive.

## Stage B — MVP falsifier (cheap empirical kill, the "trying things" part)

For the picked candidate:
- State the hypothesis as ONE falsifiable claim.
- **Pre-register the kill gate:** exact metric + threshold + smallest informative scale. Freeze it.
- Write the smallest script (<50 lines) that could falsify the claim. Data runs <2 min, model trains in the same budget. NO data loaders / model libraries / config systems / test suites yet.

**Verify the metric before running it (this is non-negotiable):**
- random/untrained model → chance level
- two identical models (same seed/data) → exact tie
- metric measures what training optimizes, not a proxy that rewards trivial behavior
- masks/seeds/eval grid fixed so all conditions compare identically

Then run and compare to the frozen gate:
- **Clean positive** (beats gate + audit passes) → Stage C
- **Clean negative** → pivot: one-line negative result, return to the next Stage-A survivor or to `research-fanout`
- **Ambiguous** → one cheap iteration at slightly larger scale; still ambiguous → treat as negative (weak small-scale signals rarely strengthen)
- **>10–15% gain** → mandatory adversarial audit (re-derive metric, check leakage, confirm baselines real) before believing it

## Stage C — Design gate (right-sized confirmation, pivot or double down)

Only after a clean, audited MVP positive:
- Design the best method for the now-confirmed effect (brainstorm a few architectures, pick on effect size / cost / scoop risk / contribution isolation).
- Pre-register the **design gate**: a ~20–30 min experiment beating baselines, with its own metric + threshold + architecture. Verify metric AND architecture with the Stage-B checks (new scale/baselines reintroduce metric bugs).
- Run it (~20–30 min config ≈ same verdict a 10× run would give).
- **Beats baselines + clean audit → DOUBLE DOWN:** building is now justified (hand to writing-plans → implementation → code-review with extra scrutiny on the eval path → full experiments + ablations).
- **Fails or marginal → PIVOT:** never edit the gate to pass. Return to method brainstorm or to `research-fanout`. Report honestly.

## Rules

- Each stage is cheaper than the next; a candidate must clear the current stage before the next runs.
- Pre-registered gates are immutable.
- Surface negatives plainly and promptly.
- Default to the cheaper test, not the bigger build. Most leverage is in Stage A and the gate discipline.
