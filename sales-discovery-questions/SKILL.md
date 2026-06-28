---
name: sales-discovery-questions
description: Generates structured, account-specific discovery questions for sales calls, organized by MEDDPICC category. Use this skill whenever the user asks for discovery questions, wants to prep for a call with a stakeholder, says "what should I ask on this call," pastes notes from a prior call and wants to know what to probe next, or provides any combination of account name, deal stage, and contact role and asks for call preparation material. Trigger even if the request is phrased casually ("help me prep for tomorrow's call with Claro" or "I have a discovery with the IT director at Vivo, what do I ask?"). This skill should activate for any call-prep request where MEDDPICC gaps could inform the question set.
---

# Sales Discovery Questions

Generates a set of targeted, account-specific discovery questions organized by MEDDPICC gaps. The output is designed for a single upcoming call — not a generic question bank.

## When to Use

- User asks for discovery questions for a specific account or stakeholder
- User provides call-prep context (account, stage, contact role) and asks what to ask
- User pastes prior call notes and wants to know what to probe next
- Any pre-call preparation request that can be shaped by MEDDPICC gap analysis

## Step 1 — Collect Context

You need at minimum: account name and the stakeholder's role. Everything else improves specificity.

If the user hasn't provided enough context, ask for:
1. **Account name** (required)
2. **Deal stage** (required — shapes which MEDDPICC gaps are most urgent)
3. **Stakeholder name and title** (required — determines question angle)
4. **What's already confirmed** — any MEDDPICC elements already established, prior call summaries, CRM notes
5. **Competitive context** (optional — only include if provided)

Do not fabricate account details, stakeholder backgrounds, or competitor names. If context is sparse, say so explicitly and generate only the questions that can be grounded in what's known.

If the account is one of Terence's primary accounts (Claro, Telefonica/Vivo, Terra Networks, Banco Inter, Banco Mercantil), check Org62 first before asking — pull open opportunities and recent activity to populate context automatically.

Also ask whether there are any relevant Slack channels to check — account channels, deal channels, or internal AE/SE threads where recent discussions may have surfaced customer signals, objections, or competitive intelligence. If the user provides channel names, read them via Slack MCP before generating questions. Treat anything surfaced there as additional confirmed or partial context for the gap analysis.

## Step 2 — Map MEDDPICC Coverage

Before generating questions, do an explicit gap analysis. For each of the eight MEDDPICC dimensions, assess:

- **Confirmed**: already established from prior calls, CRM data, or user-provided context
- **Partial**: some signal but not fully qualified
- **Gap**: unknown or unverified

Only generate questions for Partial and Gap categories. Do not pad Confirmed categories with filler questions.

### MEDDPICC Dimensions

| Dimension | What it qualifies |
|-----------|-------------------|
| **Metrics** | Quantified business impact — ROI, cost savings, revenue upside, risk reduction |
| **Economic Buyer** | The person with budget authority and final sign-off |
| **Decision Criteria** | Explicit criteria the customer will use to evaluate and select a solution |
| **Decision Process** | The steps, stakeholders, and timeline from evaluation to signed contract |
| **Paper Process** | Legal, procurement, security, and contracting steps after verbal commitment |
| **Identify Pain** | The specific business problem that creates urgency to act |
| **Champion** | An internal advocate with influence who actively sells on your behalf |
| **Competition** | Who else is in the deal — incumbent, build-vs-buy, do-nothing |

## Step 3 — Generate Questions

For each Partial or Gap dimension:

- Write 3–5 open-ended questions specific to the account context and stakeholder role
- Under each question, include one line explaining which MEDDPICC element it surfaces and why it matters at this stage
- Questions must be open-ended (not yes/no, not leading)
- Questions must be anchored to the specific account context — not generic SaaS discovery phrasing
- If you cannot write a non-generic question for a category because context is insufficient, flag it explicitly rather than inventing one

**Cap the total output at 15–18 questions across all categories.** If more categories have gaps than that budget allows, prioritize the ones most likely to block the deal at the current stage:
- Early stages (01–02): prioritize Pain, Metrics, Economic Buyer — **skip Paper Process entirely**
- Mid stages (03–04): prioritize Decision Criteria, Decision Process, Champion — Paper Process is optional
- Late stages (05+): prioritize Paper Process, Competition, Metrics validation

## Output Format

```
## [MEDDPICC Category] — [GAP or PARTIAL]

**Q: [Question text]**
*Why: [One-line rationale tying this question to the MEDDPICC element and deal stage]*

**Q: [Question text]**
*Why: [Rationale]*
```

Skip Confirmed categories entirely — do not include them in the output even with a note.

If any categories could not be addressed due to insufficient context, add a section at the end:

```
## Categories Requiring More Context

**[Category]**: Not enough account-specific detail to write a non-generic question. To generate questions here, provide: [what's needed].
```

## Constraints

- Open-ended questions only — no yes/no, no leading questions
- No fabricated account facts, financials, headcount, or org structure
- No invented competitor names — only reference competitors the user mentioned
- No generic discovery questions ("What are your biggest challenges today?") unless they can be made specific to the account's context
- Do not exceed 15–18 questions total per call

## Example (abbreviated)

**Context provided**: Claro S.A., Stage 03, stakeholder is VP of Digital Marketing, prior call confirmed pain around fragmented customer journeys across WhatsApp and email. Economic Buyer and Decision Process unknown.

**Gap analysis output** (internal, not shown to user):
- Pain: Confirmed (fragmented journeys)
- Metrics: Gap
- Economic Buyer: Gap
- Decision Criteria: Partial (fragmented journeys mentioned as a driver)
- Decision Process: Gap
- Paper Process: Skipped (Stage 03 — not yet relevant)
- Champion: Partial (this VP may be the champion, unconfirmed)
- Competition: Gap

**Questions generated** (example):

## Metrics — GAP

**Q: When you think about the cost of running disconnected campaigns across WhatsApp and email today — coordination overhead, duplicated audiences, missed timing — have you tried to put a number on what that's costing you per quarter?**
*Why: Surfaces quantified pain. Without a Metrics anchor, the deal lacks urgency and the Economic Buyer has no financial case to approve.*

## Economic Buyer — GAP

**Q: When a decision like this moves to final approval — budget sign-off, procurement sign-off — who are the two or three people that need to be aligned before anything gets signed?**
*Why: Identifies the Economic Buyer and maps the approval chain. At Stage 03, not knowing this is a blocking risk.*

## Champion — PARTIAL

**Q: When you think about your peers in the business — the team running the WhatsApp channel, the data team — who in that group would be most invested in this problem getting solved?**
*Why: Probes whether this VP has internal allies who could advance the deal in rooms we're not in.*
