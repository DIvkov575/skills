---
name: status
description: Use when the user wants a snapshot of current work state — today's progress, active tasks, recent sessions, and what's next. Reads .remember/ logs and task list.
---

# Status

Produce a concise status report of ongoing work. Output a structured report — no preamble.

## Sources to Read

Read these files in order (skip gracefully if missing):

1. `.remember/now.md` — current session buffer
2. `.remember/today-YYYY-MM-DD.md` — today's completed work (use current date)
3. `.remember/recent.md` — last 7 days context
4. TaskList tool — any active/pending tasks in this session

Also check:
- `~/.claude/projects/-Users-divkov-workplace/memory/MEMORY.md` — persistent memory index

## Output Format

```
## Status — YYYY-MM-DD HH:MM

### Today
- [bullet per distinct work item completed or in progress today]

### Active Tasks
- [any pending/in-progress tasks from TaskList, or "None tracked"]

### Recent Context (7d)
- [1-2 line summary per day that had activity]

### Next
- [inferred next steps from unfinished work, open threads, or stated plans]
```

## Rules

- Use the Read tool on each `.remember/` file. Do NOT guess contents.
- Call TaskList to check for tracked tasks.
- Keep each bullet to one line — dense, specific, no filler.
- If a section has nothing, write "—" and move on.
- Use `code formatting` for paths, commands, and tool names.
- Front-load the most actionable/important items in each section.
- Do NOT ask for confirmation. Just produce the report.
- Timestamps in "Today" section: include if multiple phases of work occurred.
