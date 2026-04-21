You are entering structured deep-thinking mode for the following request:

<request>
$ARGUMENTS
</request>

---

## Phase 1 — Multi-Perspective Analysis & Question Gathering

Analyze the request from exactly these 4 perspectives. For each, produce a **1-sentence headline insight** and **2–4 clarifying questions** that would materially change the design if answered differently.

**Perspective 1 — Product & User Experience**
End-user needs, success metrics, UX/DX implications, what "good" looks like in practice.

**Perspective 2 — Technical Architecture**
Components, data flow, technology choices, scalability, complexity vs. simplicity tradeoffs.

**Perspective 3 — Operational & Reliability**
Deployment, failure modes, monitoring/observability, maintenance burden, operational cost.

**Perspective 4 — Risk & Constraints**
Security, edge cases, resource/time/skill constraints, what could quietly go wrong.

---

After generating questions from all 4 perspectives:
1. Consolidate: remove duplicates, merge similar ones, reorder by impact on the final design.
2. Present a final **numbered list of 5–8 questions** to the user.

Format your response as:
- A brief framing sentence (what this request is really about)
- Four perspective blocks (headline insight + raw questions)
- A horizontal rule
- The consolidated question list under the heading **"Questions for you:"**

**Stop here. Wait for the user to answer before proceeding.**

---

## Phase 2 — Deep Design (execute after the user answers)

Once the user has responded to the questions, do the following in order:

### Synthesis
In 3–5 bullet points, state the key requirements and constraints you now understand, incorporating their answers.

### High-Level System Design
Present the recommended approach. Use named components, describe data flow between them, and call out the key interfaces. Be specific but stay high-level — no implementation code unless the user asks. Use a diagram in text/ASCII if it clarifies structure.

### Tradeoff Evaluation
Identify 2–3 alternative approaches or major design decisions. For each:
- **What it is** (one sentence)
- **Tradeoffs** evaluated across the 4 perspectives (product, technical, operational, risk)
- **When to prefer it**

### Decisions for You
Present 3–5 remaining open decisions the user must make. For each, give your recommended answer and a one-sentence rationale. Format as:

> **Decision**: [what to decide]
> **Recommendation**: [your call]
> **Why**: [reason]

Keep Phase 2 structured and dense — favor clarity over completeness.
