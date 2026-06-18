import os, json, sys

cwd = os.environ.get("PWD", os.getcwd())
found = []
d = cwd
while True:
    p = os.path.join(d, "AGENTS.md")
    if os.path.isfile(p):
        found.append(p)
    parent = os.path.dirname(d)
    if parent == d:
        break
    d = parent

if found:
    found.reverse()
    parts = []
    for f in found:
        with open(f) as fh:
            parts.append(f"Contents of {f}:\n{fh.read()}")
    ctx = "\n\n".join(parts)
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": ctx
        }
    }))
else:
    print(json.dumps({"suppressOutput": True}))
