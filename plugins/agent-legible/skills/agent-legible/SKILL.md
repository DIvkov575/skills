---
name: agent-legible
description: Use when adding to or creating a project's CLAUDE.md, or when the user wants code written so the next AI agent can read, verify, and safely extend it. Inserts and maintains one canonical "write for the next agent" block in CLAUDE.md, idempotently.
---

# Agent-Legible CLAUDE.md

Insert (or refresh) a single canonical block in a project's `CLAUDE.md` that
tells any agent how to write code the *next* agent can navigate, verify, and
change without a human's held context.

This is the **code-craft** axis. It deliberately does NOT cover commands,
architecture maps, gotchas, currency, or conciseness — that documentation
axis belongs to `claude-md-improver` / `/init`. Do not duplicate those here.

## What to insert

Place this block in the project `CLAUDE.md`, wrapped in the markers so it
can be located and updated later. If the markers already exist, replace
what's between them. Never paste it twice.

```markdown
<!-- BEGIN agent-legible -->
## Writing for the next agent

You are rarely the last agent to touch this code. The next agent has no
memory of your session, reads only the files, and trusts the code over any
comment. Write for that reader.

- **Leave a runnable check.** Every change must be provable without you. If
  one `test`/`build`/`typecheck` command doesn't already gate it, add or
  extend one. An agent that can run pass/fail self-corrects; one that can't
  guesses. Make failures legible — assertions name the expectation. Type new
  signatures and public boundaries; types are a loop the next agent can run.
- **Keep meaning local.** A function should be understandable without opening
  five other files (agent accuracy degrades past ~5). Pass state explicitly;
  no hidden globals or side effects. If changing X silently breaks a distant
  Y, make the coupling visible at the call site or remove it. Name things so
  the identifier matches the behavior.
- **Be explicit where frameworks are magic.** Auto-registration, decorators,
  magic ORM behavior, convention-over-config — these need non-local knowledge
  the next agent lacks. Surface the wiring or flag the one gotcha at its use
  site. Keep queries traceable locally over deep ORM composition.
- **Leave a pattern, not a prose description.** When you establish something
  new (an endpoint, model, test), make your first instance clean enough to be
  copied 50× safely, then point to it ("follow the pattern in `X`"). One
  clean exemplar beats a paragraph of architecture.

Before finishing, ask: if a fresh agent opened this repo, ran the check
command, and read only the files I touched — could it extend my work and
know if it broke something? If not, you're not done.
<!-- END agent-legible -->
```

## Procedure

1. **Locate `CLAUDE.md`.** Default to the project root. If none exists, ask
   whether to create it or run `/init` first (don't silently create one).
2. **Check for markers.** Grep for `<!-- BEGIN agent-legible -->`.
   - Present → replace everything between BEGIN/END with the current block.
   - Absent → append the block (with markers) to the end of `CLAUDE.md`.
3. **Dedup against existing prose.** If the file already states one of these
   rules in its own words, don't leave both — the marked block is canonical;
   trim the redundant ad-hoc line.
4. **Don't touch the doc axis.** Leave commands/architecture/gotchas sections
   alone; this skill owns only the marked block.
5. Show the diff and confirm before writing if the file already has content.

## Automatic insertion (hook)

This plugin ships a `PostToolUse(Write)` hook (`scripts/insert-on-init.py`)
that fires when a `CLAUDE.md` is written — e.g. when `/init` creates one — and
appends the block if the marker is absent. The hook is idempotent (guarded by
the BEGIN marker) so it never duplicates and never blocks. Invoking the skill
manually does the same insertion plus the dedup/diff steps above; the hook is
the zero-touch path for newly created CLAUDE.md files.

## Notes

- The block is intentionally short. A bloated CLAUDE.md gets ignored, which
  defeats the purpose — resist adding more rules here.
- Markers make this idempotent: safe to re-run after the research updates.
- Keep the block text in the skill and in `scripts/insert-on-init.py` in sync.
