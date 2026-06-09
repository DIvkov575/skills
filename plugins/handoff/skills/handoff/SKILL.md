---
name: handoff
description: Generate a full-briefing handoff document for the next session — captures in-flight work, decisions, next steps, mental model, and blockers.
---

# Handoff

Generate a comprehensive handoff document so the next Claude Code session can pick up cold with full context.

## Steps

1. **Gather state** — run these commands in parallel:
   - `git status --short` (uncommitted changes)
   - `git log --oneline -10` (recent commits)
   - `git diff --stat HEAD @{upstream} 2>/dev/null` (unpushed work)
   - `git branch --show-current` (current branch)
   - Find open plans/specs: `find docs/superpowers -name "*.md" -newer .git/HEAD -mtime -7 2>/dev/null | head -10`
   - Find recently modified production files: `git diff --name-only HEAD~5 2>/dev/null | grep -v tests/ | grep -v docs/ | head -10`

2. **Check task state** — if TaskList is available, call it to get open/in-progress tasks.

3. **Synthesize the handoff** — using gathered state + conversation context, write a document with ALL of these sections:

```markdown
# Handoff — YYYY-MM-DD

## In-Flight
- Branch: `<branch>` (<clean/dirty>)
- Uncommitted: <list or "none">
- Unpushed commits: <count + one-liners>
- Open tasks: <list or "none">

## Next Steps
1. <most important action — be specific, name files/commands>
2. <second priority>
3. <third if applicable>

## Decisions This Session
- <decision>: <why> (rejected alternative: <what>)
- ...
(If no significant decisions were made, write "None — routine implementation.")

## Tried and Abandoned
- <approach>: <why it failed or was rejected>
(If nothing was abandoned, write "Nothing abandoned this session.")

## Mental Model
<3-8 sentences describing the system architecture as currently relevant to active work. Focus on non-obvious relationships, recent additions, and gotchas. Don't describe what's obvious from CLAUDE.md.>

## Key Files
- `<path>` — <one-line description of relevance>
- ...
(Include: active specs, plans, recently modified production files, test files that cover active work)

## Blockers / Caveats
- <anything that might trip up the next session>
- <known bugs not yet fixed>
- <external dependencies or waiting-on items>
(If none, write "No blockers.")

## Test Status
<"N passed, all green" or describe failures>
Run: `<exact test command that was last used>`
```

4. **Write the file** — save to `HANDOFF.md` in the project root. Overwrite any existing content.

5. **Print summary** — output a 3-line summary to terminal:
   - What was accomplished
   - What's next
   - Any blockers

## Rules

- Do NOT ask for confirmation. Just gather and write.
- Do NOT fabricate information. If you don't know what was tried/abandoned, check git reflog or say "Unknown — check git log."
- Be SPECIFIC in "Next Steps" — name exact files, commands, or test names. "Continue working on the feature" is useless.
- Keep "Mental Model" focused on what's CURRENTLY RELEVANT, not a full system overview.
- If the conversation is short (quick fix, single commit), the handoff can be short. Scale detail to session complexity.
- Every section must be present even if the content is "None" or "N/A".
