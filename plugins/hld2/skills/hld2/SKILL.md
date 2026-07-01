---
name: hld2
description: Use when the user wants a design PRESENTED succinctly — a descriptive high-level design that maps what the system is and how it fits together WITHOUT proposing solutions, weighing options, or recommending an approach. Grounds every claim in the real environment, writes the doc to disk, and ALWAYS echoes it back. For a decision-driving design that evaluates options and recommends one, use `hld` instead.
---

# HLD2 — Design, Presented

Turn a request into a tight, descriptive High-Level Design. The output is a single
Markdown file plus a full echo of its contents in the final message.

<HARD-RULE>
Describe, do not decide. hld2 PRESENTS a design — it does not propose solutions,
compare options, recommend an approach, or argue for a choice. No "Option A vs B,"
no "★ recommended," no "we should," no pros/cons framing. If a design has genuine
open forks, state them neutrally as open questions and stop — do not resolve them.
</HARD-RULE>

<HARD-RULE>
Never build the thing. An HLD describes; it does not implement. Write only the
design doc — no target code, scripts, or config.
</HARD-RULE>

## Checklist

Create a TodoWrite item per step and do them in order:

1. **Ground in reality** — inspect what actually exists before describing anything.
2. **Clarify only blockers** — ask only questions whose answers you cannot observe and without which the design cannot be described.
3. **Draft the presentation** — write the doc, sections scaled to complexity, purely descriptive.
4. **Self-review** — placeholder / consistency / scope / neutrality scan; fix inline.
5. **Write to disk** — save the doc (commit only if asked).
6. **Echo the full doc back** — reproduce the entire document inline in your reply.

## Step 1 — Ground in reality

A design built on assumptions is fiction. Before writing a word:

- Inspect the relevant code, config, file layouts, and existing scripts.
- **Verify every external command, flag, file format, or API the design leans on.**
  Do not trust memory or a prior agent's claims — run `--help`, read the file, list
  the directory. If a primitive you assumed does not exist, the description must
  reflect that.
- Note version numbers where they matter.

Record what you verified in the doc (e.g. "verified, v2.1.187") so the reader knows
the description rests on observed reality.

## Step 2 — Clarify only blockers

Ask questions **one at a time**, and only when the answer is something you cannot
observe yourself AND the design cannot be described without it. Prefer
multiple-choice. Do not ask the user to *choose* a design — hld2 does not select;
it describes what is or what has been decided. If the request bundles several
independent systems, say so and scope to one.

## Step 3 — Draft the presentation

Write to `docs/HLD-<topic>.md` (or a path the user/project prefers). Fill in the
template below: **include the sections that fit, drop the ones that don't, scale
each to its complexity.**

**Be brief and neutral.** This is a *presentation* of a design — the reader wants
the shape of the system and how the pieces fit, fast. Favor bullets over prose; one
tight sentence beats a paragraph. Cut filler, drop empty tables and "N/A" rows.
State the design in the indicative ("The filter maps X to Y"), never the persuasive
("We should map X to Y because…"). No recommendations, no justifying one choice
over another.

````markdown
# HLD: <Title> (`<short-name>`)

**Date:** YYYY-MM-DD · **Author:** <alias> · **Status:** Draft | Design | Final

## 1. Overview
### 1.1 Background
<What exists today and the context a reader needs, in a few lines.>
### 1.2 Problem Statement
<The concrete gap the design addresses — bullets of specifics, stated as fact.>
### 1.3 Scope
<What this design covers; explicit non-goals as bullets.>

## 2. Behavior
<What the system does, described from the outside: inputs, outputs, triggering
conditions, data sources. Put decision-driving detail — formulas, thresholds,
formats — under the relevant item. Present tense, factual.>

## 3. Architecture
```
<ASCII diagram: components and how they connect / data flow.>
```
<One short block per component: what it is, its inputs/outputs, the algorithm or
contract it embodies, data-model or interface shape. Describe each as it stands —
not as one option among several.>

## 4. Data & Interfaces
<Schemas, message shapes, file formats, config surfaces the design exposes. Note
backward compatibility as a fact, not a recommendation.>

## 5. Open Questions
<Genuinely unresolved forks, stated neutrally as questions — no answer, no lean.
Drop this section if there are none.>
````

### Verified-facts rule (applies throughout)
Wherever the design rests on a real command, flag, file format, schema, version, or
external deliverable, state it as observed in Step 1 — not from memory. Note version
numbers where they matter, and call out anything that turned out **not** to exist.

## Step 4 — Self-review

Read the draft with fresh eyes and fix inline:
- **Neutrality:** no proposals, recommendations, option-weighing, "should/recommend/
  best/prefer" language, or ★ markers. Any fork lives only in Open Questions, unresolved.
- **Placeholders:** no stray TODO/TBD/FIXME or unfilled `<…>` template slots.
- **Consistency:** sections don't contradict each other; diagrams match the prose.
- **Scope:** focused enough for one design; decompose if not.

## Step 5 — Write to disk

Save the file and report the path. Do **not** commit unless the user asks; if they
do, use a message like `docs: HLD for <topic>` and report the commit hash.

## Step 6 — Echo the full doc back (REQUIRED)

End by reproducing the **entire** document inline in your reply — the complete
document, not a summary, not a section list, not "see the file." After the echo, a
one-line pointer to the saved path is fine. Mandatory every time.
