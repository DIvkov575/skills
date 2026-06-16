---
name: distill
description: Create a dense, expressive summary of the current conversation in 5-10 bullet points. Use when you want a snapshot of what happened, what was decided, and what matters.
---

# Distill

Produce a dense summary of this conversation. Output ONLY the bullet points — no preamble, no headers, no follow-up.

## Format

- 5-10 bullet points
- Each bullet: one complete thought, dense with specifics (names, paths, numbers, decisions)
- Front-load the most important/actionable items
- Use `code formatting` for files, commands, tools, and config values
- Capture: what was done, what was decided, what was discovered, what's unresolved
- Skip pleasantries, false starts, and dead ends unless the dead end itself is informative
- Write for someone picking this up cold — no pronouns without antecedents

## Style

Write like terse field notes, not prose. Prioritize signal density over readability. Each bullet should be independently useful — if you ripped one out and showed it to someone with no context, they should still learn something.

Good: `- Merged Lipschitz Functions.md → Lipschitz Continuity.md; updated backlinks in Contraction Mapping.md and Uniformly Continuous.md`

Bad: `- We cleaned up some duplicate files in the vault`

## Rules

- Do NOT ask for confirmation. Just output the bullets.
- Do NOT add a header or wrap in a code block.
- Do NOT summarize tool output — summarize outcomes and decisions.
- If the conversation is trivial (one question, one answer), 3 bullets is fine. Scale to substance.
- Include timestamps or sequence markers only if the conversation spans multiple distinct phases of work.
