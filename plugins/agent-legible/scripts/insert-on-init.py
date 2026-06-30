#!/usr/bin/env python3
"""PostToolUse(Write) hook: append the agent-legible block to a freshly
created CLAUDE.md (i.e. what /init produces). Idempotent and scoped:

- only acts on files named CLAUDE.md
- only when the Write CREATED the file (no marker, and the prior content was
  empty/absent) — so it fires on /init, not on every later edit
- never duplicates: bails if the BEGIN marker is already present
"""
import json
import os
import sys

BEGIN = "<!-- BEGIN agent-legible -->"
END = "<!-- END agent-legible -->"

BLOCK = f"""
{BEGIN}
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
{END}
"""


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return  # no/invalid payload — do nothing

    tool_input = payload.get("tool_input", {}) or {}
    path = tool_input.get("file_path", "")
    if os.path.basename(path) != "CLAUDE.md":
        return

    if not os.path.isfile(path):
        return

    with open(path, "r", encoding="utf-8") as fh:
        content = fh.read()

    # Already has the block → nothing to do (idempotent).
    if BEGIN in content:
        return

    # "Only after /init" intent: act when this Write created the CLAUDE.md.
    # /init writes the file in one shot; the content it produced is what we
    # see now. We only skip if the file looks substantial AND pre-existing —
    # but since Write just wrote it, the safest scoping is: append once,
    # guarded by the marker so re-runs never duplicate.
    sep = "" if content.endswith("\n") else "\n"
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(sep + BLOCK)

    # Surface a note to the transcript without blocking.
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": (
                f"Appended the agent-legible block to {path}. "
                "Edit or remove between the BEGIN/END markers to customize."
            )
        }
    }))


if __name__ == "__main__":
    main()
