---
name: humanize
description: Rewrite AI-generated text to sound like a real human wrote it. Eliminates GPTisms — the overused words, phrases, structures, and patterns that instantly mark text as AI-generated. Use on drafts, emails, tweets, blog posts, or any text that needs to pass as authentically human.
---

# Humanize

Rewrite the provided text so it reads like a specific human wrote it — not a language model performing "helpfulness." Strip every GPTism. The output should be indistinguishable from something a competent human would actually write in that context.

## Process

1. **Identify the text.** If pasted, use it. If a file is referenced, read it. If ambiguous, ask.

2. **Identify the voice target.** If the user has provided writing samples or specified a tone ("casual", "like a tweet", "professional email"), match that. If not, default to: direct, slightly informal, zero filler, varied sentence length, personality allowed.

3. **Rewrite.** Apply the GPTism elimination rules below. Output the rewritten version in a fenced code block.

4. **Report.** One line after: list the top 3–5 GPTisms you killed and what you replaced them with.

## The GPTism Catalog

### Tier 1: Dead Giveaway Words (always eliminate)

| GPTism | Why it's a tell | Human alternative |
|--------|----------------|-------------------|
| delve | Nobody says this in real life | dig into, explore, look at, examine |
| utilize | Almost always just means "use" | use |
| leverage (as verb) | Corporate AI slop | use, take advantage of, lean on |
| facilitate | Bureaucratic filler | help, enable, make possible, run |
| streamline | Vague AI buzzword | speed up, simplify, cut steps from |
| landscape (metaphorical) | "The AI landscape" — instant AI smell | space, world, field, scene |
| tapestry | AI's favorite pretentious metaphor | mix, combination, web |
| multifaceted | Over-literary filler | complex, layered, has a lot of angles |
| nuanced | AI uses this to sound smart without saying anything | specific, subtle, complicated |
| paradigm | Nobody uses this in natural speech | model, approach, way of thinking |
| synergy | Corporate AI cringe | working together, combination, overlap |
| holistic | Vague, adds nothing | full, complete, big-picture |
| robust | AI's favorite adjective | strong, solid, reliable, thorough |
| comprehensive | Overused to the point of meaninglessness | full, complete, thorough, covers everything |
| cutting-edge | Generic hype | new, latest, modern, advanced |
| game-changer | Content mill language | big deal, breakthrough, shift |
| pivotal | AI loves this word disproportionately | key, important, critical, turning point |
| foster | Nobody talks like this casually | encourage, grow, build, support |
| moreover | Stiff transition | also, plus, and, on top of that |
| furthermore | Same energy | also, and, beyond that |
| nonetheless | AI overuses formal transitions | still, but, even so |
| henceforth | Archaic AI filler | from now on, going forward |
| thereby | Legalese in casual text | so, which means |
| thus | AI uses 10x more than humans do | so |
| indeed | Filler that adds nothing | (just delete it) |
| arguably | AI hedge word | (make the claim or don't) |
| notably | AI's way of saying "here's the next bullet" | (just state the thing) |
| interestingly | Tells the reader to be interested instead of being interesting | (delete — show don't tell) |
| essentially | Usually means "I'm about to repeat myself" | (delete or rephrase) |
| fundamentally | Same as essentially | at its core, basically, really |

### Tier 2: Structural Tells (patterns, not just words)

| Pattern | What AI does | What humans do |
|---------|-------------|----------------|
| **The triple adjective** | "a robust, comprehensive, and scalable solution" | Pick one. Maybe two. |
| **The colon-into-list** | "Here are three key considerations:" + bullet list | Just... say the things. Or use a paragraph. |
| **The summary opener** | "Great question! Let me break this down." | Skip the preamble. Start with the answer. |
| **The empathy prefix** | "I understand your concern about..." | (delete — just address the concern) |
| **The hedge sandwich** | "While X, it's important to note that Y, though Z" | Pick a position. State it. |
| **The five-paragraph essay** | Intro → 3 body → conclusion in EVERY response | Match the format to the content |
| **Uniform bullet length** | Every bullet is exactly 1–2 sentences | Vary it. Some bullets are 3 words. Some are a paragraph. |
| **The echoed question** | "You asked about X. X is..." | Just answer. |
| **Perfect parallelism in lists** | Every item starts with a gerund or follows identical grammar | Mix it up. Real lists are messier. |
| **Bolded key terms** | **every** **important** **word** gets **bolded** | Bold sparingly or not at all |
| **The signpost transition** | "Now, let's move on to..." / "With that in mind..." | (delete — the next sentence speaks for itself) |
| **Numbered everything** | Steps 1, 2, 3 even when order doesn't matter | Bullets or prose when sequence is irrelevant |
| **The false balance** | "On one hand X, on the other hand Y" when one side is clearly right | Just say what's true |

### Tier 3: Filler Phrases (delete entirely)

These add zero information. Cut them and the sentence improves:

- "It's worth noting that..."
- "It's important to remember that..."
- "It should be noted that..."
- "As mentioned earlier..."
- "In today's rapidly evolving..."
- "In the ever-changing landscape of..."
- "At the end of the day..."
- "When it comes to..."
- "In terms of..."
- "The reality is that..."
- "It goes without saying that..." (then why say it?)
- "This is a testament to..."
- "Let's take a closer look at..."
- "Without further ado..."
- "In conclusion..."
- "To summarize..."
- "All in all..."
- "That being said..."
- "Having said that..."
- "With that being said..."
- "Moving forward..."
- "Going forward..."
- "At its core..."
- "When all is said and done..."
- "In a nutshell..."
- "The bottom line is..."
- "Last but not least..."
- "First and foremost..."
- "Each and every..."
- "In order to..." (just say "to")
- "Due to the fact that..." (just say "because")
- "A wide range of..." (just say "many" or "various")
- "On a daily basis..." (just say "daily")
- "At this point in time..." (just say "now")
- "In light of the fact that..." (just say "since" or "because")
- "Serves as a..." (just say "is a")

### Tier 4: Tone Tells

| AI habit | Human equivalent |
|----------|-----------------|
| Always polite, never blunt | Sometimes blunt. Sometimes funny. Sometimes curt. |
| Never uses contractions in formal-ish text | Humans almost always use contractions |
| Never starts sentences with "And" or "But" | Humans do this constantly |
| Never uses sentence fragments | Fragments are fine. Good, even. |
| Always qualifies claims ("may", "might", "could potentially") | Just say it. Add caveats only when genuinely uncertain. |
| Never uses slang or colloquialisms | Use them when the register fits |
| Overly balanced — presents all sides equally | Humans have opinions and state them |
| Ends on an upbeat/encouraging note always | Sometimes things just end. |
| Uses "!" for enthusiasm | Real enthusiasm shows in word choice, not punctuation |

### Tier 5: Emoji & Formatting Tells

- AI overuses 🚀 ✨ 💡 🎯 🔑 in informal contexts
- AI adds emojis at predictable intervals (every 2–3 sentences)
- AI uses headers and sub-headers for everything, even short responses
- AI bolds every "key term" on first mention

## Rewrite Rules

1. **Vary sentence length aggressively.** 4-word sentences next to 30-word sentences. AI loves uniform medium-length.
2. **Use contractions.** "It's", "don't", "won't", "that's" — unless the context is extremely formal.
3. **Start some sentences with "And", "But", "So", "Or".** AI almost never does this.
4. **Use sentence fragments.** Not every sentence needs a subject and verb.
5. **Have an opinion.** Don't present all sides equally. Pick the right answer and say it.
6. **Delete your first sentence.** AI opening lines are almost always deletable filler.
7. **Delete your last sentence.** AI closing lines are almost always summary/encouragement fluff.
8. **Use specific details** over generic descriptors. "17ms p99 latency" not "excellent performance."
9. **Let some things be implicit.** Humans don't spell out every logical connection.
10. **Introduce slight imperfection.** A dash where a comma would do. A parenthetical aside. A one-word paragraph.
11. **Match the register to the audience.** A tweet sounds different from an email sounds different from a blog post. AI tends to write everything at the same "professional blog post" register.
12. **Cut 30% of the words.** After rewriting, go back and cut more. Humans writing well are tighter than AI.

## Context-Specific Guidance

### For tweets/short social posts:
- Max 1-2 sentences. No headers. No bullets.
- Personality > information density
- Hot takes are fine. Incomplete thoughts are fine.
- Lowercase is fine. Fragments are fine.

### For emails/DMs:
- No greeting filler ("I hope this finds you well")
- Get to the point in sentence 1
- End with a clear ask, not a pleasantry
- Write like you're texting a colleague, not drafting a letter

### For blog posts:
- Strong opening line that makes a claim or tells a story
- Personal anecdotes and opinions mixed with facts
- Don't summarize at the end — trust the reader
- Irregular paragraph lengths (1-sentence paragraphs are powerful)

### For professional/technical writing:
- Active voice always
- Name the actor ("we decided" not "it was decided")
- Concrete over abstract ("3 API calls" not "multiple interactions")
- Short paragraphs (2-4 sentences max)

## Rules

- Do NOT ask for confirmation. Just rewrite.
- Do NOT explain what you changed (the report line handles it).
- Do NOT add content not in the original — only rephrase and cut.
- Do NOT make the text less clear in pursuit of sounding human. Clarity always wins.
- If the text is already human-sounding, say so and return it unchanged.
- If you need to know the target voice/audience and it's ambiguous, ask ONCE, then rewrite.
- Aggressive is good. Kill every GPTism even if the sentence needs restructuring to accommodate it.
