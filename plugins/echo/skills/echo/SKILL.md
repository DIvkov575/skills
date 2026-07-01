---
name: echo
description: Read a file exactly as-is into the chat so the user can see its entire contents. Use when the user asks to echo, print, show, cat, or dump a file verbatim.
---

# Echo

Read file at given path w/ Read tool; output entire contents into chat verbatim.

## Rules

- Read whole file; no offset/limit — every line
- Output complete contents byte-for-byte; no truncation
- Do NOT summarize/paraphrase/reformat/reindent/fix
- Do NOT add commentary, preamble, or trailing note
- Wrap output in fenced code block (fence longer than any backtick run inside file) → renders literally
- Path missing/ambiguous → ask which file; file empty → say so
