---
name: shrink
description: Use when compressing text for token savings via the LLMLingua-2 algorithmic model (extractive token-dropping) rather than LLM rewriting — for prompts/context fed to another LLM where exact wording does not matter. Not for human-facing prose.
---

# Shrink

Compress text by calling the hosted LLMLingua-2 model, which drops low-information tokens via a trained classifier. Output is terser but less readable than the original — meant for *machine* consumption (context fed to another LLM), not humans.

## Shrink vs Compress

| | `shrink` (this) | `compress` |
|---|---|---|
| Method | LLMLingua-2 token classifier (extractive) | LLM rewrite (you) |
| Output | dropped tokens, fragmented grammar | clean, readable terse prose |
| Speed | one API call (~2-5s) | model inference |
| Best for | LLM-context, RAG chunks, few-shot examples | skills, system prompts, docs humans read |
| Risk | drops exact numbers/identifiers | none |

Use `compress` for anything a human reads. Use `shrink` for bulk context where only meaning matters.

## How to Run

The skill ships a script. Run it on the target text:

```bash
python3 scripts/shrink.py --rate 0.3 --file <path>
# or pipe:
cat prompt.md | python3 scripts/shrink.py --rate 0.3
```

**Zero dependencies** — pure stdlib (`urllib`), no `pip install` needed. Backend: `divkov/llmlingua-2` HF Space (free CPU tier; sleeps only after 48h idle, cold start ~30-60s handled automatically with a retry).

## Parameters

- `--rate` (0.1–0.9): fraction of tokens to KEEP. `0.3` = ~3.3x compression. Lower = more aggressive. Default `0.3`
- `--force "a,b,c"`: comma-separated tokens to NEVER drop — **always pass exact numbers, IDs, paths, API names, version strings here**, since the classifier drops digits as low-information
- `--file <path>`: read input from file (else stdin)

Compressed text → stdout. Stats (`orig → compressed tokens | ratio | % saved`) → stderr.

## Workflow

1. Identify the text (file or pasted). Confirm it's machine-bound, not human-facing — if human-facing, use `compress` instead.
2. Scan for exact values that must survive (numbers, identifiers, paths); collect them for `--force`.
3. Run the script with an appropriate `--rate` (start `0.3`; raise to `0.6–0.7` if precision matters).
4. Report the compressed output and the stats line.

## Common Mistakes

- **Using it on human-facing text** → output is fragmented and ugly. Use `compress`.
- **Not forcing numbers** → "2.1GB" becomes "1GB" because the classifier drops the "2." tokens. Always `--force` critical values.
- **Rate too low for dense text** → meaning loss. Technical/precise text needs `0.6+`; redundant prose tolerates `0.3–0.4`.
- **Expecting valid grammar** → it drops articles/connectives by design. That's fine for LLM input.
