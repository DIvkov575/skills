---
name: status
description: Use when the user wants a snapshot of current work state — today's progress, active tasks, recent sessions, and what's next. Reads .remember/ logs and task list.
---

# Status

Produce structured status report. No preamble.

## Sources (read in order; skip if missing)

1. `.remember/now.md` — current session buffer
2. `.remember/today-YYYY-MM-DD.md` — today's log (use current date)
3. `.remember/recent.md` — 7-day context
4. TaskList tool — active/pending tasks
5. `~/.claude/projects/-Users-divkov-workplace/memory/MEMORY.md` — persistent memory index

## Output Format

```
## Status — YYYY-MM-DD HH:MM

### Today
- [one bullet per work item completed/in-progress]

### Active Tasks
- [pending/in-progress from TaskList, or "None tracked"]

### Recent Context (7d)
- [1-2 line summary per active day]

### Next
- [inferred next steps from unfinished work/open threads]
```

## Rules

- Read each `.remember/` file w/ Read tool — never guess contents
- Call TaskList for tracked tasks
- One line per bullet; dense, specific, no filler
- Empty section → "—"
- Use `code formatting` for paths/commands/tools
- Front-load most actionable items
- No confirmation — just produce report
- Include timestamps in Today only if multiple work phases occurred
