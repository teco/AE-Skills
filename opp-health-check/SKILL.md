---
name: opp-health-check
description: Runs a structured MEDDPICC health assessment on a Salesforce opportunity and produces a prioritized action plan. Use this skill whenever the user asks how healthy a deal is, wants to assess pipeline risk before a forecast call or QBR, says "should I commit this deal," asks for a deal review, wants to sanity-check a close date, or asks what's missing on an opportunity. Also trigger when the user is preparing for a manager pipeline review and wants to know where each deal stands. This skill goes beyond a data pull — it scores MEDDPICC coverage, flags red flags, and tells the AE exactly what to do next.
---

# Opportunity Health Check

Produces a MEDDPICC-scored deal health assessment with a prioritized action plan. The output is an internal AE working document designed for pipeline reviews, forecast calls, and deal coaching sessions.

## When to Use

- Pre-pipeline review / QBR prep
- Deciding whether to commit or move a deal to Best Case
- Assessing whether a close date is realistic
- Identifying what's blocking a deal before escalating to management
- Any request to "review," "score," or "assess" an opportunity

## Step 1 — Resolve the Opportunity

If an Org62 Opportunity ID (starts with `006`) was provided, use it directly.

If a name was provided:
```soql
SELECT Id, Name, StageName, Amount, CloseDate, ForecastCategoryName, AccountId, Account.Name
FROM Opportunity
WHERE Name LIKE '%<name>%' AND IsClosed = false
ORDER BY LastModifiedDate DESC
LIMIT 5
```
If multiple results, show options and ask the user to confirm.

## Step 2 — Pull All Data in Parallel

Run all of the following simultaneously:

**Opportunity detail:**
```soql
SELECT Id, Name, StageName, Amount, CloseDate, ForecastCategoryName, ForecastCategory,
       Type, Description, OwnerId, AccountId, Account.Name, CreatedDate, LastModifiedDate
FROM Opportunity
WHERE Id = '<opp_id>'
```

**Contact roles:**
```soql
SELECT ContactId, Contact.Name, Contact.Title, Contact.Email, Role, IsPrimary
FROM OpportunityContactRole
WHERE OpportunityId = '<opp_id>'
```

**Recent activities (last 20):**
```soql
SELECT Id, Subject, ActivityDate, Status, TaskSubtype, Description, OwnerId
FROM Task
WHERE WhatId = '<opp_id>'
ORDER BY LastModifiedDate DESC
LIMIT 20
```

**Open cases on the account:**
```soql
SELECT Id, CaseNumber, Subject, Status, Priority, LastModifiedDate
FROM Case
WHERE AccountId = '<account_id>' AND IsClosed = false
ORDER BY LastModifiedDate DESC
LIMIT 10
```

**SAF record (to confirm specialist team membership and forecast):**
```soql
SELECT Id, Opportunity__c, ForecastAmount__c, ForecastCategory__c, StageName__c
FROM SpecialistForecast__c
WHERE Opportunity__c = '<opp_id>'
LIMIT 3
```

**Slack:** If the user provides a Slack channel, read the last 40–50 messages via `slack_read_channel`. Look for: blockers, objections, internal concerns, competitive mentions, customer signals, action items, sentiment. If no channel is provided, ask: *"Do you have an internal Slack channel for this account or deal? It often surfaces signals that aren't in Org62."*

## Step 3 — Score MEDDPICC Coverage

For each dimension, assign one of four ratings based on the evidence collected:

| Rating | Meaning |
|--------|---------|
| **Confirmed** | Explicitly established and documented |
| **Partial** | Some signal, not fully qualified |
| **Gap** | Unknown or unverified |
| **Red Flag** | Actively missing and likely blocking progress |

**Scoring heuristics by dimension:**

- **Metrics**: Confirmed = quantified ROI/savings/upside stated in activities or notes. Gap = no numbers anywhere.
- **Economic Buyer**: Confirmed = EB named in contact roles with recent engagement. Red Flag = no contact role mapped as Economic Buyer *and* no recent EB engagement in activities.
- **Decision Criteria**: Confirmed = specific evaluation criteria documented. Partial = general interest noted but no structured criteria.
- **Decision Process**: Confirmed = next steps, timeline, and decision-makers documented. Gap = activity notes only show demos or check-ins with no clear process mapped.
- **Paper Process**: Score only if stage ≥ 03. At stages 01–02, mark as N/A.
- **Identify Pain**: Confirmed = specific business problem with urgency documented. Partial = problem implied but not stated with urgency.
- **Champion**: Confirmed = a named internal advocate with influence, actively engaged. Red Flag = no champion identified and deal is stage 03+.
- **Competition**: Confirmed = competitors named and strategy documented. Gap = no competitive context anywhere.

## Step 4 — Generate the Health Check Output

Present the assessment in this structure:

---

## Opportunity Health Check — [Opportunity Name]

**Account:** [Account Name] | **Stage:** [StageName] | **Forecast:** [ForecastCategoryName]
**Amount:** $[Amount] | **Close Date:** [CloseDate] | **Days to Close:** [N]
**Last Activity:** [Date] — [Subject]

> [One-sentence overall deal health verdict. E.g.: "This deal is structurally weak at Stage 04 — no Economic Buyer mapped, Champion unconfirmed, and no activity in 3 weeks."]

---

### MEDDPICC Scorecard

| Dimension | Rating | Evidence |
|-----------|--------|----------|
| Metrics | [Confirmed / Partial / Gap / Red Flag] | [One-line summary of what's known or missing] |
| Economic Buyer | | |
| Decision Criteria | | |
| Decision Process | | |
| Paper Process | [N/A if stage < 03, else score] | |
| Identify Pain | | |
| Champion | | |
| Competition | | |

---

### Risk Summary

List only the dimensions rated **Gap** or **Red Flag**. For each, one sentence on why it matters at this stage and what it puts at risk (forecast accuracy, close date, deal loss).

---

### Action Plan

This is the core of the output — what to do next, in priority order.

Prioritize actions that address Red Flags first, then Gaps in the dimensions most likely to block this deal at its current stage (use the same stage-based prioritization as `sales-discovery-questions`). Each action should be:
- Specific and time-bound
- Tied to the MEDDPICC dimension it addresses
- Assigned an owner (AE, SE, Champion, Customer)

Format:

| # | Action | MEDDPICC Dimension | Owner | By When |
|---|--------|--------------------|-------|---------|
| 1 | [Specific action] | [Dimension] | AE | [Date or timeframe] |
| 2 | | | | |

Cap at 8 actions. If more gaps exist, prioritize the ones that, if unresolved, would prevent the deal from moving to the next stage.

---

### Forecast Confidence

Based on the MEDDPICC scorecard, state whether the current forecast category is:
- **Appropriate** — scorecard supports the category
- **Overstated** — deal is weaker than the forecast category implies; recommend downgrading
- **Understated** — deal is stronger; may be worth upgrading

One sentence of reasoning. If the close date is in the past or within 14 days and there are Red Flags, flag prominently: **⚠️ CLOSE DATE AT RISK**

---

## Step 5 — Offer Next Actions

After presenting the health check, offer:

> "Want me to generate discovery questions targeting the gaps above, or draft a close plan from here?"

If the user says yes to discovery questions, invoke the `sales-discovery-questions` skill using the gap analysis already completed — do not re-collect context.

If the user says yes to a close plan, invoke `close-plan` with the opportunity already resolved — do not re-query Org62.

## Constraints

- Do not fabricate MEDDPICC ratings. If evidence is genuinely ambiguous, default to Gap rather than Partial.
- Do not invent competitor names, contact details, or financial figures.
- The Action Plan must be grounded in the gaps identified — do not generate generic "schedule a follow-up" actions unless there's a specific reason.
- Forecast confidence assessment must reference specific scorecard findings, not general sentiment.
