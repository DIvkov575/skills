---
name: human-writing
description: Rewrite prose to minimize em dashes and strip all markdown-style formatting, two strong tells of AI-generated text. Parentheses are fine and stay. Use on drafts, emails, posts, docs, or any text that should read like a person typed it plainly.
---

# Human Writing

Rewrite the provided text so it relies on plain sentence structure and plain text. Remove em dashes by restructuring sentences, and strip every piece of markdown-style formatting so the result is clean prose. Parentheses are allowed and need no change. Keep the meaning identical.

## Process

1. **Identify the text.** If pasted, use it. If a file is referenced, read it. If ambiguous, ask once.

2. **Find every em dash and every markdown mark.** Em dashes include `—`, ` - ` used as a dash, and `--`. Markdown marks include bold, italics, headers, blockquotes, list markers, horizontal rules, and emphasis backticks.

3. **Restructure to kill em dashes, do not just swap punctuation.** Replacing every em dash with a comma is not the goal. The goal is sentences that never needed the interruption.

4. **Strip the formatting down to plain text.** The output should be something a person could type into a plain message box.

5. **Output** the rewritten text in a fenced code block.

6. **Report.** One line after: how many em dashes you removed, how many markdown marks you stripped, and how many em dashes you kept on purpose.

## Why em dashes are a tell

Em dashes let a writer staple two half-thoughts together without committing to how they relate. AI does this constantly because it generates clauses faster than it decides on structure. A reader feels the hedge even if they cannot name it. Strip them and the prose has to stand on actual sentence structure. That is what makes it read human.

## How to remove an em dash

Pick the rewrite that fits the relationship between the two halves:

| Em dash use | Fix |
|-------------|-----|
| Joining two related independent clauses | Split into two sentences. Or use a period, a semicolon, or "and"/"but"/"so". |
| Setting off an appositive or aside | Use commas, fold the detail into the main clause, or put it in parentheses (those are fine now). |
| Building to a punchline or reveal | A colon often does this job better and with less drama. |
| Tacking on an afterthought | Cut the afterthought, or promote it to its own sentence. |
| Showing a range or span | Use "to" or an en dash in numeric ranges (e.g. "3 to 5", "1990s"). |

### Before and after

- Before: "The plan was simple — ship fast and fix later."
  After: "The plan was simple: ship fast and fix later."
- Before: "She finished the draft — it took three days — and sent it off."
  After: "She finished the draft in three days and sent it off."
- Before: "We had one goal — growth."
  After: "We had one goal: growth."

## Markdown formatting to strip

Remove all of it so the output is plain text:

| Markdown | What to do |
|----------|-----------|
| Bold (`**x**`, `__x__`) | Remove the markers. If the emphasis mattered, carry it in word choice. |
| Italics (`*x*`, `_x_`) | Remove the markers. Use plain words or quotes if a term needs setting off. |
| Headers (`#`, `##`, ...) | Drop the `#` marks. Make it a plain line, or fold it into the prose. |
| Blockquotes (`>`) | Remove the `>` and write the quote inline or as plain lines. |
| List markers (`-`, `*`, `1.`) | If the text is meant as prose, flatten the items into sentences. If a list is genuinely the right shape, write plain lines without the markers. |
| Horizontal rules (`---`, `***`) | Delete them. |
| Emphasis backticks | Remove backticks used only for emphasis. Keep them only for real code, file names, or identifiers. |

Genuine fenced code blocks stay as code. The rule targets prose dressed up with formatting, not actual code.

## Parentheses

Parentheses are allowed. Leave existing parentheticals alone, and feel free to use them when removing an em dash. They are not a tell on their own.

## When to keep an em dash

Do not zero them out mechanically. Keep one when removing it genuinely hurts clarity or rhythm. One deliberate em dash for emphasis in a long piece is fine. A pattern of them is the problem. Target: cut at least 80% of em dashes, and strip 100% of the markdown formatting from prose.

## Rules

- Restructure sentences to remove em dashes. Do not just substitute punctuation.
- Strip all markdown-style formatting from prose. Leave real code untouched.
- Parentheses stay. Do not remove or rewrite them for being parentheses.
- Preserve meaning exactly. Do not add or drop information.
- Do not make the text less clear to hit a target. Clarity wins over the rule.
- Do not ask for confirmation unless the source text is ambiguous. Just rewrite.
- If the text already avoids em dashes and carries no markdown, say so and return it unchanged.
- Apply this to your own writing too, not only on request, when the user has this skill active.
