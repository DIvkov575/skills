---
name: compress
description: Compress text to the fewest tokens possible while preserving 100% of actionable information. Use on system prompts, skills, CLAUDE.md files, or any text that persists across many requests.
---

# Compress

Rewrite the provided text into the densest possible representation that preserves all actionable meaning. The output should be usable as a drop-in replacement — another LLM reading only the compressed version must behave identically to one reading the original.

## Process

1. **Identify the text.** If the user pasted it, use it. If they reference a file, read it. If ambiguous, ask.

2. **Compress.** Apply the techniques below. Output the compressed version inside a fenced code block.

3. **Report.** One line after the code block: `{original_tokens} → {compressed_tokens} ({percent_reduction}% reduction)` — estimate token counts (1 token ≈ 4 chars for English).

## Techniques (apply all)

### Structural compression
- Strip articles (a, an, the) unless ambiguity results
- Strip filler ("please note that", "it is important to", "make sure to", "keep in mind")
- Strip meta-commentary about the instructions themselves ("this prompt tells you to...")
- Strip motivation/explanation IF the rule is already clear without it
- Collapse multi-sentence instructions into single directives
- Merge duplicate/overlapping rules into one

### Symbolic shorthand
- Use arrows: → (leads to, results in, maps to), ← (derived from), ↔ (bidirectional)
- Use symbols: = (equals/means), ≠ (not), ∈ (in/member of), ∉ (not in), > < (comparison)
- Use abbreviations: w/ (with), w/o (without), b/c (because), esp. (especially), e.g., i.e., vs, re: (regarding), approx (approximately)
- Use slash-lists: "JSON/YAML/TOML" not "JSON, YAML, or TOML"
- Use semicolons to join related short clauses instead of separate bullets

### Semantic compression
- Replace examples that illustrate a rule with just the rule (drop the example)
- Replace enumerated lists where a pattern is obvious with the pattern + "etc"
- Replace conditional chains (if X then Y, if A then B) with a compact table or `X→Y; A→B`
- Replace verbose descriptions with terse equivalents ("respond with a JSON object containing..." → "output JSON:")

### Preservation (never compress away)
- All factual claims and constraints
- All named entities, paths, URLs, commands
- All numbers, thresholds, limits
- All conditional logic and edge cases
- All format specifications
- The distinction between MUST/SHOULD/MAY if present
- XML tags and structural markers that delimit sections

## Output format

The compressed text should:
- Use bullet points or semicolons, not paragraphs
- Use consistent indentation for hierarchy
- Use `code formatting` for literals (paths, commands, values)
- Omit trailing periods on bullets
- Be immediately usable as a system prompt, skill, or instruction block

## Rules

- Do NOT ask for confirmation. Just compress.
- Do NOT explain what you removed. The report line is sufficient.
- Do NOT change the meaning, intent, or behavior the text would produce.
- Do NOT add information not in the original.
- If the text is already terse (e.g. a config file, a schema), say so and return it unchanged.
- Aggressive is good. Target ≥40% reduction. If you can only achieve <20%, the text was already dense — say so.
