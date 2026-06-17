---
name: namegen
description: Use when brainstorming company or product names for a concept, trait, or theme. Accepts a term and generates ~100 name candidates via parallel agents exploring different creative lenses.
---

# Namegen

Generate ~100 company/product name candidates for a given term by fanning out 6 parallel agents, each exploring a distinct naming lens. Output is a firehose — volume over curation.

## Input

`$ARGUMENTS` = the trait, concept, or theme to generate names for.

If `$ARGUMENTS` is empty, ask the user to provide a single term or short phrase before proceeding.

## Execution

### Step 1 — Dispatch 6 naming agents in parallel

In a **single message**, call the `Agent` tool six times in parallel. Each agent works independently and is blind to the others' output. Each produces 15-20 company names from its assigned lens.

**The 6 lenses:**

| Agent | Lens | Brief |
|-------|------|-------|
| 1 | Obscure Synonyms & Archaic Words | Deep thesaurus cuts, rare/obsolete English, unusual borrowings |
| 2 | Mythology & Folklore | Gods, heroes, creatures, artifacts across world cultures |
| 3 | Historical Figures | Real people renowned for embodying the trait |
| 4 | Literary & Fictional Characters | Novels, film, allegory, comics, folklore |
| 5 | Metaphor & Nature | Natural phenomena, animals, materials, processes that embody the trait |
| 6 | Etymology & Neologism | Latin/Greek/Sanskrit/Proto-IE roots, portmanteaus, invented words from roots |

**Prompt template for each agent:**

```
Generate 15-20 company names inspired by the concept: "$ARGUMENTS"

Your lens: [LENS NAME] — [LENS BRIEF]

Rules:
- Each name should sound like a plausible company (1-2 words, pronounceable, memorable)
- Draw from OBSCURE sources — skip anything a typical brainstormer would find in 5 minutes
- Vary structure: some standalone words, some compounds, some with suffixes (-io, -ly, -fy, Corp, Labs, etc.) but don't overdo suffixes
- Output format — one name per line, exactly like this:

Paladin                 — paladins exemplify unwavering loyalty; Old French "palatinus"
Aegis Works             — Zeus's shield; metaphor for divine protection

The name is left-aligned. The dash + rationale is separated by SPACES to column 25.
Rationale: max 12 words. Explain the obscure connection.

No preamble. No headers. No numbering. Just the lines.
```

### Step 2 — Combine and present

Collect all 6 agent outputs. Present them grouped by lens under short headers:

```
## Obscure Synonyms & Archaic Words

[agent 1 output]

## Mythology & Folklore

[agent 2 output]

## Historical Figures

[agent 3 output]

## Literary & Fictional Characters

[agent 4 output]

## Metaphor & Nature

[agent 5 output]

## Etymology & Neologism

[agent 6 output]
```

After all sections, add a one-line closer:

> **~{total count} names generated.** Cherry-pick freely — or ask me to riff on any that catch your eye.

## Rules

- Do NOT editorialize, rank, or filter. This is a firehose.
- Do NOT add preamble before the first section.
- If an agent returns fewer than 10 names, note it but do not retry.
- If an agent fails entirely, retry once. If still failing, skip that lens and note it.
- Keep the visual format strict: names left-aligned, rationale right-shifted with ` — ` separator.
