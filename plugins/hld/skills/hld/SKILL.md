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
5. **Write to disk** — save the doc (commit only if asked).
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

Write to `docs/HLD-<topic>.md` (or a path the user/project prefers). Fill in the
template below: **include the sections that fit, drop the ones that don't, scale
each to its complexity.** A small tool needs a Goal, Approach, Architecture, and
Tradeoffs — nothing more. A larger system earns the full numbered structure.
Match the formality to the stakes.

**Be brief.** This is a *high-level* design, not a spec — the reader wants the
shape of the system and the decisions behind it, fast. Favor bullets over prose;
one tight sentence beats a paragraph. Cut filler, drop empty tables and "N/A"
rows, and never pad a section to look complete. A good HLD is short.

````markdown
# HLD: <Title> (`<short-name>`)

**Date:** YYYY-MM-DD · **Author:** <alias> · **Status:** Draft | Design | Final

## 1. Overview
### 1.1 Background
<What exists today and the context a reader needs, in a few lines.>
### 1.2 Problem Statement
<The concrete gap or failure being solved — bullets of specifics.>
### 1.3 Goals
<Bulleted outcomes this design delivers.>

## 2. Requirements
### 2.1 Functional
<What the system must do. Put decision-driving detail — formulas, triggering
conditions, data sources — under the relevant requirement.>
### 2.2 Out of Scope
<Explicit non-goals.>

## 3. Solution Options
<Per major decision, list options with trade-offs; mark the chosen one with ★.
Drop this section if there was no real fork.>
**Option A — <name>.** <trade-offs as bullets.>
**Option B ★ — <name>.** <why it wins.>

## 4. Current State
```
<ASCII diagram of today's architecture when relevant.>
```
<What breaks today / why change is needed. Cite real incidents/tickets if any.>

## 5. Design Proposal
### 5.1 Architecture
```
<ASCII diagram: components and how they connect / data flow.>
```
### 5.x <Per-component / per-concern subsections>
<One short block each: the component, the algorithm/formula, the integration
contract, data-model changes (note backward compatibility), canary/test changes,
release safety. Add only the subsections this design needs.>

## 6. Design Analysis
### 6.1 Key Improvements
<What materially gets better, as bullets.>
### 6.2 Risks
| Risk | Mitigation |
|---|---|
````

### Verified-facts rule (applies throughout)
Wherever the design rests on a real command, flag, file format, schema, version,
or external deliverable, state it as observed in Step 1 — not from memory. Note
version numbers where they matter, and call out anything that turned out **not**
to exist so the design visibly accounts for it. State these inline where they
matter, or add a short **Verified facts** block after Approach.

## Step 4 — Self-review

Read the draft with fresh eyes and fix inline:
- **Placeholders:** no stray TODO/TBD/FIXME or unfilled `<…>` template slots.
- **Consistency:** sections don't contradict each other; diagrams match the prose.
- **Scope:** focused enough for one design; decompose if not.
- **Ambiguity:** if a statement reads two ways, pick one and make it explicit.

## Step 5 — Write to disk

Save the file and report the path. Do **not** commit unless the user asks; if
they do, use a message like `docs: HLD for <topic>` and report the commit hash.

## Step 6 — Echo the full HLD back (REQUIRED)

End by reproducing the **entire** HLD inline in your reply — the complete document,
not a summary, not a section list, not "see the file." The user should be able to
read the whole design in the conversation without opening the file. After the echo,
a one-line pointer to the saved path is fine.

This step is mandatory every time, even if the user didn't ask for it explicitly.
