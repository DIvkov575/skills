---
name: research-fanout
description: Use when generating candidate ML research directions for a domain/problem — divergent half of research selection. Scans the bleeding edge, then fans out parallel-lens ideation into an exhaustive, unpruned candidate list. Pair with research-gate for convergence.
---

# Research Fan-Out

Divergent generation. Goal: an exhaustive, deliberately over-inclusive list of candidate research directions. **Quantity and variance over quality — no pruning here.** Convergence/killing is `research-gate`'s job, deliberately separate.

## Input

`$ARGUMENTS` = the domain, problem, or seed (e.g. "discrete diffusion sampling efficiency, single-GPU"). If empty, ask for a one-line domain/constraint before proceeding.

## Step 1 — Scan the bleeding edge

Run the bundled deep-research workflow in cheap mode to map the landscape:

```
Workflow({ scriptPath: "<deep-research-efficient plugin>/scripts/deep-research-efficient.js",
           args: { question: "open problems and recent work in <$ARGUMENTS> — what's solved, what's claimed-but-shaky, what's conspicuously absent (last 6-12mo)", mode: "quick" } })
```

(If the deep-research-efficient plugin isn't installed, fall back to the built-in `deep-research` skill in a narrow scope, or parallel WebSearch.) Capture: what's **solved**, what's **claimed but shaky**, what's **conspicuously absent**. The gaps are the raw material.

## Step 2 — Fan out parallel-lens ideation

In a **single message**, dispatch 4 `Agent` calls in parallel, each blind to the others, each handed the Step-1 landscape and asked for 4-6 candidate directions from its lens:

| Lens | Brief |
|---|---|
| Theorist | gaps in guarantees/bounds; "what's provable but unproven"; theory↔practice mismatches |
| Contrarian | invert a load-bearing assumption everyone shares; "what if the standard choice is wrong" |
| Cross-pollinator | port a technique from an adjacent field that hasn't crossed over yet |
| Practitioner | what breaks at scale / in deployment that no method addresses; failure-mode-driven |

**Prompt per agent:**
```
Domain: "$ARGUMENTS"
Landscape (solved / shaky / absent): [paste Step-1 findings]
Your lens: [LENS] — [BRIEF]

Generate 4-6 candidate research directions through your lens. Each = ONE line:
  "<one-line contribution claim>" — <2-sentence why it might be novel/winnable>
Contribution claim format: "First to X" or "X beats Y because Z".
Bias toward specific, falsifiable directions over vague themes. No pruning — include the speculative ones.
No preamble. Just the lines.
```

## Step 3 — Dedup and present

Collect all 4 outputs. Merge near-duplicates (same idea, different framing → keep the sharpest phrasing). Present grouped by lens, then a flat deduplicated master list numbered for reference.

Target **≥10 candidates** after dedup. If fewer, dispatch a second round with sharpened lens briefs.

End with:
> **{N} candidate directions generated.** None are vetted — run `research-gate` to converge: cheap literature filters first, then MVP falsifiers and metric-first kill gates.

## Rules

- Do NOT prune, rank by quality, or kill candidates — that biases toward the obvious and is `research-gate`'s job.
- Do NOT start designing experiments — that's gating/building.
- Keep claims one line each; a candidate that needs a paragraph to state isn't sharp enough yet.
- Speculative/weird candidates are wanted — the gate kills cheaply later, so cost of a bad candidate here is ~zero.
