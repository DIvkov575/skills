---
name: hld
description: Use when the user asks for an HLD or high-level design for a system, tool, or feature. Grounds the design in the real environment before writing, scales each section to its complexity, writes the doc to disk, and ALWAYS echoes the full HLD back to the user at the end.
---

# HLD — High-Level Design

Turn a request into a tight, grounded High-Level Design document. The output is a
single Markdown file plus a full echo of its contents in the final message.

<HARD-RULE>
Never build the thing. An HLD describes; it does not implement. Do not write the
target code, scripts, or config — only the design doc. If the user later says
"build it," that is a separate task.
</HARD-RULE>

## Checklist

Create a TodoWrite item per step and do them in order:

1. **Ground in reality** — before designing, inspect what actually exists.
2. **Clarify the crux** — ask only the questions whose answers change the design.
3. **Draft the HLD** — write the doc, sections scaled to complexity.
4. **Self-review** — placeholder / consistency / scope / ambiguity scan; fix inline.
5. **Write to disk** — save and (if in a repo) commit.
6. **Echo the full HLD back** — reproduce the entire document inline in your reply.

## Step 1 — Ground in reality

An HLD built on assumptions is fiction. Before writing a word of design:

- Inspect the relevant code, config, file layouts, and existing scripts.
- **Verify every external command, flag, file format, or API the design leans
  on.** Do not trust your memory or a prior agent's claims — run `--help`, read
  the file, list the directory. If a primitive you assumed turns out not to
  exist, the design must change, not the facts.
- Note version numbers where they matter (a flag may exist in one version, not another).

Record what you verified in the doc (e.g. "verified, v2.1.187") so the reader
knows the design rests on observed reality, not guesswork.

## Step 2 — Clarify the crux

Ask questions **one at a time**, only when the answer would change the design.
Prefer multiple-choice. Skip anything you can settle yourself from Step 1. If the
request bundles several independent systems, say so and scope to one.

If you are weighing approaches, present 2-3 with trade-offs and a recommendation —
do not write an exhaustive survey of options the user didn't ask for.

## Step 3 — Draft the HLD

Write to `docs/HLD-<topic>.md` (or a path the user/project prefers). Default
sections — include what fits, scale each to its complexity (a sentence to a short
paragraph; this is a *high-level* design, not a spec):

- **Goal** — one or two sentences. What it does and for whom.
- **Approach / why this shape** — the core idea; why not the obvious alternative.
- **Verified facts** — the real commands/formats/versions the design rests on.
- **Architecture** — components and how they connect (an ASCII diagram earns its
  space when data flow is the point).
- **Interface / commands** — the surface the user or caller touches (a table works well).
- **Error handling** — what happens when things fail or are absent.
- **Tradeoffs** — what this design gives up, stated plainly.
- **Out of scope** — explicit non-goals.
- **Open questions** — what still needs confirming, especially anything that
  couldn't be tested in the current environment.

Keep it dense. Cut filler. The reader wants the shape of the system, fast.

## Step 4 — Self-review

Read the draft with fresh eyes and fix inline:
- **Placeholders:** no stray TODO/TBD/FIXME (an *intentional* open question is fine
  if it's named in Open Questions).
- **Consistency:** sections don't contradict each other; the diagram matches the
  command table.
- **Scope:** focused enough for one design; decompose if not.
- **Ambiguity:** if a statement reads two ways, pick one and make it explicit.

## Step 5 — Write to disk

Save the file. If inside a git repo, commit it (e.g.
`docs: HLD for <topic>`). Report the path and commit hash.

## Step 6 — Echo the full HLD back (REQUIRED)

End by reproducing the **entire** HLD inline in your reply — the complete document,
not a summary, not a section list, not "see the file." The user should be able to
read the whole design in the conversation without opening the file. After the echo,
a one-line pointer to the saved path is fine.

This step is mandatory every time, even if the user didn't ask for it explicitly.
