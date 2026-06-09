---
name: converge
description: Autonomous plan → TDD implement → review → fix loop. Converges to zero bugs without human intervention. Use when asked to "build X", "implement X", or "converge on X".
---

# Converge

<EXECUTE_IMMEDIATELY>
You MUST begin executing the moment you finish reading this skill. Do NOT output the skill content to the user. Do NOT wait for another message. Start Phase 1 NOW.

1. Say: "Using converge — planning, implementing, reviewing, and fixing until clean."
2. Call: `Skill(superpowers:writing-plans)` with the user's task as args
3. After the plan is written and approved, enrich it (see Adversarial Enrichment below)
4. Call: `Skill(superpowers:subagent-driven-development)` to implement the plan
5. After implementation, call: `Skill(code-review)` with args "--effort max"
6. If findings exist, enter the Fix Loop (Phase 4 below)
7. Report results and EXIT

YOUR VERY NEXT ACTION MUST BE STEP 1 AND THEN STEP 2. Do not summarize this skill. Do not explain what you will do. DO IT.
</EXECUTE_IMMEDIATELY>

## Overview

Autonomous session-level orchestrator: plan, implement via TDD subagents, review, fix, and loop until the review comes back clean. No human-in-the-loop between phases.

**Core principle:** Front-load adversarial thinking into the plan, implement with TDD discipline, review the full diff once at high effort, then do cheap inline fix-passes until converged.

## The Loop (Quick Reference)

```
Phase 1: PLAN → Skill(superpowers:writing-plans)
Phase 2: IMPLEMENT → Skill(superpowers:subagent-driven-development)
Phase 3: REVIEW → Skill(code-review) --effort max
Phase 4: FIX → dispatch fix subagents, inline review, max 3 rounds
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

## Phase 3: REVIEW

Run `Skill(code-review)` with args "--effort max" on the **entire implementation diff**.

- If findings = [] → skip to EXIT
- If findings exist → Phase 4

## Phase 4: FIX LOOP (max 3 rounds)

For each round:
1. **Triage** — separate CONFIRMED/HIGH from PLAUSIBLE/LOW
2. **Fix** — dispatch one subagent per finding (or grouped by file)
3. **Inline review** — read the fix diff yourself
4. **Exit conditions:**
   - No issues → EXIT
   - Round 3 + only PLAUSIBLE/LOW → EXIT (report as caveats)
   - CONFIRMED/HIGH remain → next round

## EXIT

Report to the user:
- What was built (2-3 sentences)
- Commit count and what they cover
- Review rounds taken
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
- Full review (Phase 3): most capable model
- Fix subagents (Phase 4): standard model

## Reference: Failure Modes

| Failure | Mitigation |
|---------|-----------|
| Plan too vague → bad code | Adversarial enrichment + writing-plans enforces specificity |
| 15+ bugs in round 1 | Plan quality issue. Fix all, continue. |
| Fix introduces new bug | Inline review catches it; next round if missed |
| 3 rounds, still CONFIRMED | EXIT with report. Don't loop forever. |
| Subagent blocked/fails | Escalate model tier or provide more context |

## Reference: What This Does NOT Do

- Push to remote
- Create PRs
- Brainstorm/design (use `superpowers:brainstorming` first)
- Deploy
- Fix pre-existing bugs