---
name: atomize
description: Use when decomposing large unstructured text (notes, transcripts, docs, chat logs) into atomic semantic units — standalone facts with noise removed — e.g. for agent memories, skill facts, knowledge bases, or RAG chunks. Use when you need "one fact per unit", deduplicated and verified against the source.
---

# Atomize

Decompose messy text into **atomic semantic units**: minimal, self-contained, source-verified facts. Each unit states exactly one thing, stands alone with no reference to its source, and is provably backed by the original text.

A unit is "pure" only if it survives all four passes. Run them in order — do not skip.

## What a unit must be

- **Atomic** — one predicate, one assertion. No "and"/"but"/lists joining two facts.
- **Standalone** — readable in isolation. No "the approach", "he", "this", "as mentioned".
- **Source-backed** — entailed by the source text alone, not by your world-knowledge.
- **Non-redundant** — each fact appears once across the whole output.

## The four passes

### 1. Segment
Split the text into candidate propositions. Drop everything that is not a factual assertion: pleasantries, throat-clearing ("honestly", "anyway"), meta-talk ("as I said"), questions, opinions-as-filler. Split conjunctions into separate candidates.

### 2. Decontextualize
Rewrite each candidate to stand alone, resolving references **using only the source text**:
- Pronouns/anaphora → the named entity ("he" → "Dmitriy").
- Definite refs ("the approach", "that bug") → the specific thing.
- Discourse deixis ("this is why", "the former") → spell out the referent.
- **Relative time → absolute.** "yesterday"/"now"/"recently" → the actual date if derivable, else keep relative ONLY if the source gives no anchor.

**Disambiguate-or-drop (the purity rule):** if a reference cannot be resolved unambiguously *from the source*, DROP the candidate. Never guess a referent from outside knowledge — a confidently-wrong unit is worse than a missing one.

### 3. Verify (LLM entailment — automatic)
For each surviving unit, check it against its source span: **"Does the source text alone prove this exact statement?"**
- Mark hedged claims as hedged. Source says "probably X" → unit must say "X was likely…", not "X". A flat fact that the source only suggested is **not entailed → drop or re-hedge**.
- Any detail in the unit not present in the source (a name, number, date you filled in) → **not entailed → drop the unit**.
- This is your fabrication guard. When in doubt, drop.

### 4. Dedup
Merge units that state the same fact (including against any existing target corpus, e.g. `MEMORY.md`). Keep the clearest phrasing. One fact, once.

## Output

Default: a flat list of units, each with the source span it was verified against.

```
- <atomic unit>   ⟵ "<source span>"
```

**Memory-format mode** (when targeting agent memory / `MEMORY.md`): after the four passes, map each unit to frontmatter — `name` (kebab slug), `description` (one line), `metadata.type` (user/feedback/project/reference), body = the unit. Dedup against existing `MEMORY.md` entries in pass 4.

## Quick reference

| Pass | Action | Drop rule |
|---|---|---|
| 1 Segment | split into assertions | drop non-facts, filler, questions |
| 2 Decontextualize | resolve all references from source | drop if referent ambiguous |
| 3 Verify | LLM entailment vs source span | drop if not provably entailed |
| 4 Dedup | merge same-fact units | drop duplicates |

## Common mistakes

- **Guessing referents** → "the approach" resolved to a name not in the source = fabrication. Drop instead.
- **Flattening hedges** → source "I'm pretty sure X" became unit "X". Keep the uncertainty or drop.
- **Leaving relative time** → "yesterday" with no absolute anchor is not standalone. Anchor it or flag it.
- **Skipping verify** → without the entailment pass, decontextualization silently invents facts. The pass is not optional.
- **Splitting too far** → "X happened" + "X was on Tuesday" when one unit "X happened on Tuesday" is still atomic. One assertion, not one token.
