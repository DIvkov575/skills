---
name: converge
description: Autonomous plan → TDD implement → review→fix loop, each iteration in a fresh-context subagent. Converges to zero bugs without human intervention. Use when asked to "build X", "implement X", or "converge on X".
---

# Converge

<EXECUTE_IMMEDIATELY>
You MUST begin executing the moment you finish reading this skill. Do NOT output the skill content to the user. Do NOT wait for another message. Start Phase 1 NOW.

1. Say: "Using converge — planning, implementing, then looping review→fix in fresh subagents until clean."
2. Call: `Skill(superpowers:writing-plans)` with the user's task as args
3. After the plan is written and approved, enrich it (see Adversarial Enrichment below)
4. Call: `Skill(superpowers:subagent-driven-development)` to implement the plan
5. Enter the Converge Loop (Phase 3): dispatch one FRESH-context subagent per review→fix iteration
6. Report results and EXIT

YOUR VERY NEXT ACTION MUST BE STEP 1 AND THEN STEP 2. Do not summarize this skill. Do not explain what you will do. DO IT.
</EXECUTE_IMMEDIATELY>

## Overview

Autonomous session-level orchestrator: plan, implement via TDD subagents, then loop review→fix until clean. No human-in-the-loop between phases.

**Core principle:** Front-load adversarial thinking into the plan, implement with TDD discipline, then run each review→fix iteration in a **fresh-context subagent** so review quality never degrades from accumulated orchestrator context. The orchestrator holds only the task summary, the diff range, and a compact per-round verdict — it dispatches and decides; it never reviews or fixes inline.

## The Loop (Quick Reference)

```
Phase 1: PLAN → Skill(superpowers:writing-plans)
Phase 2: IMPLEMENT → Skill(superpowers:subagent-driven-development)
Phase 3: CONVERGE LOOP → per round, ONE fresh subagent does review+fix+verify;
         orchestrator reads compact verdict, decides loop/exit. Max 3 rounds.
EXIT → report what was built, leave committed but NOT pushed
```

## Phase 1: PLAN

Invoke `Skill(superpowers:writing-plans)` with the user's task. The plan MUST include:
- TDD structure (failing test → implement → pass → commit per task)
- Exact file paths
- Complete code in every step

After the plan is written, scan it for adversarial enrichment (below). Carry enrichment as context when briefing subagents — do NOT rewrite the plan file.

## Phase 2: IMPLEMENT

Invoke `Skill(superpowers:subagent-driven-development)`. Execute continuously — do not pause between tasks. Each subagent gets:
- The full task text from the plan
- The adversarial enrichment notes for that task
- Context about what prior tasks produced (file paths, function signatures)

When implementation completes, record the **diff range** (e.g. `<base-sha>..HEAD`) — this is the review scope handed to every converge subagent. Note the base SHA before Phase 2 so it's known here.

## Phase 3: CONVERGE LOOP (fresh subagent per round, max 3 rounds)

Each round is ONE subagent launched with the Agent tool (fresh context, no inheritance of orchestrator history). The orchestrator passes only:
- The diff range to review (`<base>..HEAD`)
- The one-line task summary
- The adversarial enrichment notes
- The prior round's unresolved findings (round 1: none)

**The subagent's instructions (put this in the Agent prompt):**
1. Run `Skill(code-review)` with `--effort max` on the given diff range.
2. Triage findings: CONFIRMED/HIGH vs PLAUSIBLE/LOW.
3. Fix every CONFIRMED/HIGH finding directly in the working tree.
4. Verify: run the test suite; confirm fixes apply cleanly and introduce no regressions.
5. Commit the fixes.
6. Return ONLY a compact verdict (no narration, no diffs): `{round_status, fixed: [...], remaining: [{severity, file, one-line}], tests: pass/fail}`.

**Orchestrator decision (reads only the returned verdict):**
- `remaining` empty → EXIT
- Round 3 reached and only PLAUSIBLE/LOW remain → EXIT (report as caveats)
- CONFIRMED/HIGH remain and round < 3 → launch next round's fresh subagent, passing `remaining` forward

The orchestrator MUST NOT read the full diff or findings itself — that defeats the fresh-context purpose. It acts only on the compact verdict.

## EXIT

Report to the user:
- What was built (2-3 sentences)
- Commit count and what they cover
- Converge rounds taken
- Any remaining caveats
- Test suite status

Do NOT push. Do NOT create a PR.

---

## Reference: Adversarial Enrichment

Before dispatching implementation, scan each task and append:

- **None/null:** "What if this field is None, not just MISSING?"
- **Empty collections:** "What if the list has zero entries?"
- **Cross-file impacts:** "Does the change break any caller?"
- **Arithmetic/offsets:** "Verify against existing layout calculations"
- **Type boundaries:** "What types can this value actually be at runtime?"

## Reference: Model Selection

- Plan writing: most capable model
- Implementation subagents: standard model
- Converge-loop subagents (Phase 3): most capable model — each runs review + fix + verify in one fresh context

## Reference: Failure Modes

| Failure | Mitigation |
|---------|-----------|
| Plan too vague → bad code | Adversarial enrichment + writing-plans enforces specificity |
| 15+ bugs in round 1 | Plan quality issue. The round's subagent fixes all, returns verdict; orchestrator loops. |
| Fix introduces new bug | Next round's fresh subagent reviews the full diff range again and catches it |
| 3 rounds, still CONFIRMED | EXIT with report. Don't loop forever. |
| Subagent blocked/fails | Re-dispatch with escalated model tier or more context |
| Orchestrator context bloats across rounds | Fresh subagent per round + compact-verdict-only return keeps orchestrator lean |

## Reference: What This Does NOT Do

- Push to remote
- Create PRs
- Brainstorm/design (use `superpowers:brainstorming` first)
- Deploy
- Fix pre-existing bugs