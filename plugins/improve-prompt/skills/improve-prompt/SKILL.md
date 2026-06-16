---
name: improve-prompt
description: Analyze a prompt (system prompt, skill, or user message) and rewrite it applying documented best practices. Outputs the improved prompt plus a changelog explaining each change.
---

# Improve Prompt

Take the prompt the user provides (or the most recent system prompt / skill in context) and rewrite it to be more effective. Output the improved version first, then a short changelog.

## Process

1. **Identify the prompt.** If the user pasted one, use it. If they said "improve this" referencing a file, read it. If ambiguous, ask which prompt to improve.

2. **Diagnose.** Silently evaluate the prompt against the checklist below. Do NOT print the diagnosis — go straight to the rewrite.

3. **Rewrite.** Output the full improved prompt inside a fenced code block. Make it immediately copy-pasteable.

4. **Changelog.** After the code block, list each change as a bullet: what you changed and which principle it addresses. Keep bullets to one line each.

## Checklist (apply in order)

### Structure & Clarity
- Is the task stated in the first sentence? Move it there if not.
- Are instructions sequential? Use numbered steps when order matters, bullets when it doesn't.
- Is context separated from instructions? Wrap context in XML tags (`<context>`, `<documents>`, `<examples>`).
- Are variable inputs clearly delimited from fixed instructions?
- Could a colleague with no context follow this unambiguously?

### Specificity
- Replace vague verbs ("handle", "process", "deal with") with concrete actions ("extract", "classify", "rewrite as").
- Replace qualitative targets ("good", "detailed", "comprehensive") with measurable ones ("3-5 bullet points", "under 200 words", "include at least one example per section").
- Add constraints: format, length, tone, audience, what to include, what to omit.
- If the prompt says what NOT to do without saying what TO do instead — add the positive instruction.

### Examples
- If the output format is non-obvious, add 1-3 examples in `<example>` tags.
- Examples should cover the typical case and at least one edge case.
- If examples exist, verify they're diverse (not just variations of the same input).

### Role & Context
- Add a one-sentence role in the system prompt if absent and useful ("You are a senior backend engineer reviewing pull requests for correctness bugs.").
- Add motivation/context behind non-obvious instructions ("Your response will be read aloud by TTS, so avoid ellipses and parentheticals.").

### Output Control
- State the format explicitly (JSON, markdown, plain prose, bulleted list).
- If structured output: provide the schema or a concrete example of the shape.
- If the response should start a certain way: add a system instruction ("Respond directly without preamble. Do not start with 'Here is...' or 'Based on...'").
- Prefer positive formatting directives ("Write in flowing prose paragraphs") over negative ones ("Don't use markdown").

### For Tool-Use / Agent Prompts
- Tool descriptions: include WHEN to call (trigger condition), not just what it does.
- Remove aggressive language ("CRITICAL", "YOU MUST", "ALWAYS") — newer models follow instructions literally and this causes overtriggering. Use calm directives instead.
- If the prompt previously needed anti-laziness scaffolding ("be thorough", "don't skip steps"), consider removing it and testing without — newer models are more proactive by default.
- For parallel tool use: add explicit parallelism guidance if tools are independent.

### For Long/Agentic Prompts
- Add a progress/verification instruction if the task is multi-step ("After each phase, verify against [criteria] before proceeding.").
- Add boundaries: what the model should NOT do without asking (destructive actions, scope changes).
- Add autonomy grants: what it CAN decide without asking (naming, formatting, equivalent approaches).
- If context is large: put documents/data at the top, instructions and query at the bottom.
- If multi-turn: ensure the first message carries the full task spec (don't drip-feed across turns).

### Concision
- Remove filler ("I'd like you to", "Please note that", "It's important to remember").
- Remove duplicate instructions (same idea stated multiple ways).
- Remove instructions the model would follow by default (don't tell it to "be helpful" or "answer accurately").
- Collapse multi-sentence instructions into single clear directives where possible.

## Rules

- Do NOT ask for confirmation before rewriting. Just do it.
- Do NOT explain prompt engineering theory. The changelog is sufficient.
- Preserve the original intent exactly — improve the execution, not the goal.
- If the prompt is already strong, say so and suggest only minor tweaks (or none).
- If the prompt is a SKILL.md, preserve the frontmatter and section structure.
- Keep the rewrite in the same language as the original.
- The improved prompt should be shorter than or equal in length to the original unless adding examples or structure requires more space.
