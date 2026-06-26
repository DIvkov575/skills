---
name: research
description: End-to-end procedure for finding a novel, winnable ML research direction — scan the bleeding edge, creatively find shortfalls, generate a WIDE set of directions and record them all to a persistent ledger (Phase 1), evaluate and pare down (Phase 2), then for each survivor build cheap MVP gates, verify the metric, run, and escalate to a real MVP/design gate before committing. On failure, pull the next idea from the ledger instead of regenerating. Use when starting research, picking a direction, or deciding whether to abandon one.
---

# Research

One procedure, blank page → go/no-go. Two phases: **generate** (diverge), then **narrow** (converge by cheaply trying things). Core rule: effort ∝ 1/confidence — the cheapest experiment that could kill an idea runs before any expensive one. Killing ideas early and cheap is the goal, not a failure.

## Hard reflexes (these were violated in past projects — obey them)
- **Metric before method.** Build + sanity-check the eval metric BEFORE implementing the method. Loss on the wrong tokens once faked 39–47% "wins".
- **Too-good is a bug.** Any first-run improvement >10–15% → mandatory adversarial audit before believing it.
- **Pre-register every gate.** Metric + threshold + scale written down BEFORE running; the urge to edit a gate after seeing results = the result is negative.
- **Cheap kill beats expensive kill.** Killing a direction at the literature stage for ~$0 beats killing it after a multi-hour run.
- **Building never fixes a selection problem.** Most leverage is in Phase 1–2 and the gates, not in code.

---

## PHASE 1 — Generate directions (diverge; no pruning)

**1a. Scan the bleeding edge.** Run the bundled tool to map the landscape:
```
Workflow({ scriptPath: "<deep-research-efficient>/scripts/deep-research-efficient.js",
           args: { question: "open problems + recent work in <domain> — what's solved, claimed-but-shaky, conspicuously absent (last 6-12mo)", mode: "quick" } })
```
(Fallback: built-in `deep-research` skill, narrow scope, or parallel WebSearch.) Capture three buckets: **solved**, **claimed-but-shaky**, **conspicuously absent**.

**1b. Find shortfalls — creatively, using everything we have.** Before ideating, pull context that sharpens where the gaps are:
- **Global memories** (`~/.claude/projects/.../memory/MEMORY.md` + `.remember/`): past directions, what failed and why, recorded preferences/constraints. Don't repeat a dead end.
- **Existing skills/repo**: prior `PROJECT_RESEARCH.md`, design specs, abandoned branches — reusable assets and known-bad paths.
- Ask: where is the bleeding edge *brittle*? What does everyone assume that might be wrong? What's provable-but-unproven? What breaks at scale that no method addresses?

**1c. Fan out ideation — wide.** In ONE message dispatch parallel `Agent` calls, each blind to the others, each given the 1a landscape + 1b shortfalls. Use ≥6 distinct lenses for a wide span — Theorist (gaps in bounds/guarantees), Contrarian (invert a load-bearing assumption), Cross-pollinator (port a technique from an adjacent field), Practitioner (deployment/scale failure modes), Historian (revive an abandoned idea that newer tools now make feasible), Adjacent-domain (what would a physicist / linguist / systems person try here). Each returns 6–10 one-line directions: `"<First-to-X / X-beats-Y-because-Z>" — 2-sentence why-novel-and-winnable`. Bias for breadth and weirdness; cost of a bad candidate is ~zero because the gate kills cheaply.

**1d. Dedup → record the FULL peak set to the ledger.** Merge near-duplicates (keep sharpest phrasing). Target ≥20 candidates after dedup. **No pruning, no ranking by quality.** Then **write every candidate to the persistent ledger** (see below) — this is the peak, captured before any Phase-2 attrition, so a failed attempt later returns to the shelf instead of regenerating from scratch.

### The Candidate Ledger (persistent across attempts)
Maintain `docs/RESEARCH_LEDGER.md` (create if absent). It is the durable backlog of every idea ever generated, with its status. Each entry:
```
- [ID] <one-line contribution claim>  ·  status: pool | picked | killed:<stage> | shipped
       lens: <which lens(es) produced it>  ·  added: <date>
       prior-art/delta: <if known>  ·  killed-because: <reason, when killed>
```
Rules:
- Phase 1 appends ALL new candidates as `pool` (dedup against existing IDs — don't re-add a known-killed idea unless something material changed; note what changed).
- Phase 2 updates status in place: `picked`, `killed:<2a-triviality|2a-scoop|2a-thin|2a-winnability|2b-mvp|2c-design>`, or `shipped`. Always fill `killed-because`.
- **When an attempt fails, do NOT regenerate from scratch — first read the ledger and pull the next-best `pool` candidate.** Only return to Phase 1 if the pool is exhausted or stale.
- Killed entries stay (don't delete) — they record dead ends so they aren't re-tried, and a newer tool/insight can resurrect one (move back to `pool` with a note).

---

## PHASE 2 — Narrow (converge; cheapest filter first, each candidate survives ALL)

### 2a. Literature filters (no code, fastest)
Per candidate, cheapest sub-check first:
1. **Triviality** — core as pseudocode. <10 lines + direct port of an existing technique → thin wrapper. Kill.
2. **Scoop** — `deep-research-efficient` (`thorough` mode): "does <candidate> exist; who's active, last 12mo." Exists, or 3+ active groups → kill (unless a specific unfair advantage).
3. **Thin** — would a top reviewer call it incremental ("combined more X", ablation table, +1 dataset)? Demand a mechanism/result that changes thinking.
4. **Winnability** — name the *specific experiment* that, if it works, gives an edge on budget (1 GPU, weeks, no from-scratch pretraining). Edge = "nobody tried it" → ask *why*; absence is usually a signal.

Survivors get a 3–5 sentence dossier (contribution / closest prior art + delta / winnable experiment / risk). **Bring 1–3 survivors to the user for an explicit pick before spending compute.** Zero survivors → say so; "none clear the bar" is a valid, valuable outcome.

### 2b. MVP gate — per surviving candidate (the "cheaply trying things" part)
For each (in priority order; one at a time):
- Hypothesis = ONE falsifiable claim.
- **Pre-register the kill gate**: exact metric + threshold + smallest informative scale. Freeze it.
- Smallest script (<50 lines) that could falsify it. Data runs <2 min, model trains in same budget. NO loaders / model libraries / configs / test suites yet.
- **Verify the metric BEFORE running** (non-negotiable): random model → chance; two identical models (same seed/data) → exact tie; metric measures what training optimizes, not a proxy rewarding trivial behavior; masks/seeds/grid fixed across conditions. Any failure → metric broken, fix first.
- Run, compare to frozen gate:
  - **Clean positive** (+ audit) → 2c
  - **Clean negative** → record `killed:2b-mvp` + reason in the ledger; pull the next survivor, then the next-best `pool` candidate from the ledger; only return to Phase 1 if the pool is exhausted
  - **Ambiguous** → one cheap larger-scale iteration; still ambiguous → treat as negative
  - **>10–15% gain** → mandatory adversarial audit (re-derive metric, check leakage, confirm baselines) before believing

### 2c. Real MVP / design gate — only after a clean, audited positive
- Design the best method for the now-confirmed effect (brainstorm a few architectures; pick on effect size / cost / scoop risk / contribution isolation).
- **Pre-register the design gate**: a right-sized (~20–30 min) experiment beating baselines, with its own metric + threshold + architecture. Verify metric AND architecture with the 2b checks (new scale/baselines reintroduce metric bugs).
- Run it (~20–30 min config ≈ same verdict a 10× run gives).
- **Beats baselines + clean audit → DOUBLE DOWN**: building is justified — hand to `writing-plans` → implementation → `code-review` (extra scrutiny on the eval path) → full experiments + ablations.
- **Fails or marginal → PIVOT**: never edit the gate to pass. Record `killed:2c-design` + reason; pull the next-best `pool` candidate from the ledger; only return to Phase 1 if the pool is exhausted. Report honestly.

---

## Rules
- Each stage is cheaper than the next; clear the current before the next runs.
- Pre-registered gates are immutable.
- Surface negatives plainly and promptly; don't soften a kill to keep a project alive.
- Default to the cheaper test, not the bigger build.
- The ledger is the source of truth for what's been tried. Read it before generating; update it on every status change. A failed attempt returns to the shelf, not to a blank page.
