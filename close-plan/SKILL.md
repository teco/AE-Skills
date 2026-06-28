---
name: close-plan
description: Generates a data-grounded internal Mutual Close Plan for a stalled or in-flight deal. Combines Org62 opportunity data with the account's Slack channel activity to produce a realistic, actionable working document. Internal AE use only — not customer-facing.
---

# Close Plan Generator

Generates an internal Mutual Close Plan by combining Org62 deal data with Slack channel activity. The output is an AE working document — candid, data-grounded, and designed to unblock deals.

## Trigger Phrases
- "close plan for [opportunity] in [#channel]"
- "generate a close plan for [opportunity]"
- "/close-plan [opportunity name or ID] [#slack-channel]"

## Required Inputs
1. **Opportunity** — name or Salesforce ID (starts with `006`)
2. **Slack channel** — the account's internal Slack channel. Required. If not provided, ask for it before proceeding.

## How to Execute

### Step 1 — Resolve the Opportunity

If an ID was provided, use it directly. If a name:
```soql
SELECT Id, Name, StageName, Amount, CloseDate, ForecastCategoryName, AccountId,
       Account.Name, OwnerId, ForecastCategory
FROM Opportunity
WHERE Name LIKE '%<name>%' AND IsClosed = false
ORDER BY LastModifiedDate DESC
LIMIT 5
```

### Step 2 — Run All Data Queries in Parallel

**Full opportunity + contact roles:**
```soql
SELECT Id, Name, StageName, Amount, CloseDate, ForecastCategoryName,
       ForecastCategory, Type, Description, OwnerId, AccountId, Account.Name
FROM Opportunity
WHERE Id = '<opp_id>'
```

```soql
SELECT ContactId, Contact.Name, Contact.Title, Contact.Email, Role, IsPrimary
FROM OpportunityContactRole
WHERE OpportunityId = '<opp_id>'
```

**Recent activities (last 15):**
```soql
SELECT Id, Subject, ActivityDate, Status, TaskSubtype, Description, OwnerId
FROM Task
WHERE WhatId = '<opp_id>'
ORDER BY LastModifiedDate DESC
LIMIT 15
```

**Open cases on the account:**
```soql
SELECT Id, CaseNumber, Subject, Status, Priority, LastModifiedDate
FROM Case
WHERE AccountId = '<account_id>' AND IsClosed = false
ORDER BY LastModifiedDate DESC
LIMIT 8
```

**Slack channel activity:**
Use `slack_read_channel` to read the most recent 30–50 messages from the account channel. Look for: blockers, customer signals, internal concerns, action items, next steps.

### Step 3 — Generate the Close Plan

---

## Close Plan — [Opportunity Name]

**Account:** [Account Name] | **Stage:** [Stage] | **Forecast:** [ForecastCategoryName]
**Amount:** $[Amount] | **Close Date:** [CloseDate] | **Days to Close:** [N]

> ⚠️ CLOSE DATE OVERDUE — flag prominently if close date is in the past

---

### Urgency Narrative
Why does this deal need to close by [date]? Base on customer situation, business context, regulatory deadlines, fiscal year-end. Be candid — if there's no clear urgency, flag it as a risk.

---

### Milestone Timeline
| Milestone | Target Date | Owner | Status |
|-----------|-------------|-------|--------|
| Contract/legal review | [date] | Customer | Not started |
| Procurement approval | [date] | Customer | Not started |
| Executive sign-off | [date] | Customer | Not started |
| Technical sign-off | [date] | AE + SE | Not started |
| Pricing finalized | [date] | AE | Not started |
| Order Form sent | [date] | AE | Not started |

---

### Known Risks
Top risks derived from: missing contact roles (MEDDPICC gaps), open critical cases, activity gaps, stage vs. close date misalignment, Slack signals (objections, delays, competitive threats).

---

### AE Action Items
- [ ] [Action] — by [date]

---

### Customer Commitments
- [ ] [Commitment] — by [date]

---

### Next Steps (This Week)
2-3 most important actions in the next 7 days.

---

### Step 4 — Review Before Posting

Always present the close plan to the user first. Do not create a Canvas or post to Slack until the user approves.

Say: *"Here's the close plan based on Org62 data and [#channel] activity. Let me know if you'd like to adjust anything before I create the Canvas."*

### Step 5 — Create Canvas and Post

Once approved:
1. Create a Slack Canvas (`slack_create_canvas`) with the full close plan
2. Post the Canvas link to the account Slack channel
3. DM the Canvas link to the requesting AE

## Important Notes
- This is an **internal AE working document** — write in plain, direct language. Candid risk assessments. Not sanitized for customer viewing.
- Slack channel is required — ask if not provided
- If no contact roles are mapped, flag as a critical MEDDPICC risk (no Economic Buyer, no Champion mapped)
- After posting, remind the AE this is a living document — update weekly
