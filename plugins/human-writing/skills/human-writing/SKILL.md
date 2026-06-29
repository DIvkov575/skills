---
name: human-writing
description: Rewrite text to minimize em dashes and parentheticals. Em dashes and parenthetical asides are two of the strongest tells of AI-generated prose, and overusing them makes writing feel choppy and evasive. Use on drafts, emails, posts, docs, or any text that should read like a person wrote it cleanly.
---

# Human Writing

Rewrite the provided text so it relies on plain sentence structure instead of em dashes and parentheticals. Most em dashes and parentheses can be removed by restructuring the sentence, and the result reads cleaner and more confident. Keep the meaning identical.

## Process

1. **Identify the text.** If pasted, use it. If a file is referenced, read it. If ambiguous, ask once.

2. **Find every em dash and parenthetical.** Em dashes include `—`, ` - ` used as a dash, and `--`. Parentheticals include `( )` asides and dash-bracketed asides like `text — aside — text`.

3. **Restructure, do not just swap punctuation.** Replacing every em dash with a comma or every parenthesis with a comma is not the goal. The goal is sentences that never needed the interruption.

4. **Output** the rewritten text in a fenced code block.

5. **Report.** One line after: how many em dashes and parentheticals you removed, and how many you kept on purpose.

## Why these two tells matter

- **Em dashes** let a writer staple two half-thoughts together without committing to how they relate. AI does this constantly because it generates clauses faster than it decides on structure. A reader feels the hedge even if they cannot name it.
- **Parentheticals** signal that the writer could not decide whether a detail belonged in the sentence. Either it matters and earns a place in the main clause, or it does not and gets cut.

Strip both and the prose has to stand on actual sentence structure. That is what makes it read human.

## How to remove an em dash

Pick the rewrite that fits the relationship between the two halves:

| Em dash use | Fix |
|-------------|-----|
| Joining two related independent clauses | Split into two sentences. Or use a period, a semicolon, or "and"/"but"/"so". |
| Setting off an appositive or aside | Use commas, or fold the detail into the main clause. |
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

## How to remove a parenthetical

| Parenthetical use | Fix |
|-------------------|-----|
| A genuinely important detail | Promote it into the main sentence. |
| A minor clarification | Use a comma, or cut it. |
| A definition or example | Use "such as", "like", or a separate sentence. |
| A citation, unit, or reference | Keep it. These are fine in parentheses. |
| An aside the writer was unsure about | Cut it. If it mattered, it earns a clause. |

### Before and after

- Before: "The API (which we rewrote last quarter) handles auth now."
  After: "The API we rewrote last quarter handles auth now."
- Before: "Most users (around 80%) never change the default."
  After: "Around 80% of users never change the default."
- Before: "It works (most of the time)."
  After: "It works most of the time." Or, if the caveat matters: "It works, but not always."

## When to keep one

Do not zero them out mechanically. Keep an em dash or parenthetical when removing it genuinely hurts clarity or rhythm:

- One deliberate em dash for emphasis in a long piece is fine. A pattern of them is the problem.
- Parentheses around citations, units, abbreviations, and references stay. "(see Figure 2)", "(p99)", "(2024)".
- A short aside that is funnier or clearer in parentheses, used once, is human. Used every paragraph, it is a tell.

Target: cut at least 80% of em dashes and parentheticals. Keep the few that earn their place.

## Rules

- Restructure sentences. Do not just substitute punctuation.
- Preserve meaning exactly. Do not add or drop information beyond a cut aside that added nothing.
- Do not make the text less clear to hit the target. Clarity wins over the rule.
- Do not ask for confirmation unless the source text is ambiguous. Just rewrite.
- If the text already avoids both, say so and return it unchanged.
- Apply this to your own writing too, not only on request, when the user has this skill active.
