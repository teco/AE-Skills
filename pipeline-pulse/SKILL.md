---
name: pipeline-pulse
description: At-risk pipeline digest for Salesforce specialist AEs. Uses the SpecialistForecast__c (SAF) object to pull the AE's involved opportunities, flags risk signals, and delivers a prioritized Canvas to Slack DM.
---

# Pipeline Pulse

Generates a prioritized at-risk pipeline digest based on the SAF (SpecialistForecast__c) object — the correct pipeline view for specialist AEs who are team members on deals rather than owners.

## Prerequisites

This skill uses the `SpecialistForecast__c` object which is specific to Salesforce's internal Org62. If you are using this outside of Salesforce, replace the SAF query with your own pipeline source (e.g. `OpportunityTeamMember` to find opps where you're a team member).

## Trigger Phrases
- "pipeline pulse"
- "what's at risk in my pipeline"
- "show me my pipeline"
- "/pipeline-pulse"

## How to Execute

### Step 1 — Get the AE's Org62 User ID

Use `getUserInfo` to retrieve the current user's Org62 User ID. Never hardcode a user ID.

### Step 2 — Fetch SAF Pipeline

```soql
SELECT Id, Name, ForecastAmount__c, ForecastCloseDate__c, ForecastStage__c,
       ForecastType__c, Opportunity__c, Opportunity__r.Name, Opportunity__r.IsClosed,
       Opportunity__r.CloseDate, Opportunity__r.AccountId,
       Opportunity__r.Account.Name, Opportunity__r.Account.ParentId,
       Opportunity__r.Account.Parent.Name, Account__c, Account_ID__c, OwnerId
FROM SpecialistForecast__c
WHERE OwnerId = '<user_id>'
AND IsDeleted = FALSE
AND Opportunity__r.IsClosed = false
AND ForecastCloseDate__c >= <CURRENT_DATE>
AND ForecastCloseDate__c <= <12_MONTHS_OUT>
AND ForecastStage__c NOT IN ('Dead - Lost', 'Dead - No Decision', 'Dead - Duplicate',
                              'Dead - No Opportunity', 'Dead - OEM', '08 - Closed Won',
                              '08 - Closed Lost', '08 - Closed')
```

### Step 3 — Fetch Activity Dates for Each Opportunity

```soql
SELECT WhatId, MAX(LastModifiedDate) lastActivity
FROM Task
WHERE WhatId IN ('<opp_id_1>', '<opp_id_2>', ...)
GROUP BY WhatId
```

### Step 4 — Fetch Open Critical Cases for Each Account

```soql
SELECT AccountId, COUNT(Id) caseCount
FROM Case
WHERE AccountId IN ('<acct_id_1>', '<acct_id_2>', ...)
AND IsClosed = false
AND (Subject LIKE '%CRITICAL%' OR Subject LIKE '%PROACTIVE MONITORING%' OR Subject LIKE '%Sev1%')
GROUP BY AccountId
```

### Step 5 — Score and Flag Each Deal

| Risk Flag | Condition |
|-----------|-----------|
| 🔴 **Stale** | No activity logged in 14+ days |
| 🔴 **Overdue** | Close date is in the past and deal is still open |
| 🟡 **Early stage, closing soon** | Stage 01–02 with close date within 60 days |
| 🟡 **No amount** | ForecastAmount__c is $0 or null |
| 🟡 **Critical cases on account** | Account has open CRITICAL/Sev1/Proactive Monitoring cases |
| 🟢 **On track** | No risk flags |

### Step 6 — Format the Digest

---

## Pipeline Pulse — [AE Name]
*[Date] | [N] active SAF records | Total forecast: $[sum]*

---

### 🔴 Needs Immediate Attention ([count])
| Account | Opportunity | Stage | Amount | Close Date | Risk |
|---------|-------------|-------|--------|------------|------|

### 🟡 Watch List ([count])
| Account | Opportunity | Stage | Amount | Close Date | Risk |
|---------|-------------|-------|--------|------------|------|

### 🟢 On Track ([count])
| Account | Opportunity | Stage | Amount | Close Date |
|---------|-------------|-------|--------|------------|

### Summary
- **Total pipeline:** $[sum of ForecastAmount__c]
- **Closing this month:** [count + total $]
- **Closing next 90 days:** [count + total $]
- **Top action:** One sentence on the single most important thing to do today.

---

### Step 7 — Deliver to Slack

1. Create a Slack Canvas (`slack_create_canvas`) with the full digest
2. Send as a DM to the AE (`slack_send_message` with their Slack User ID)
3. Message: brief summary (2-3 sentences) + Canvas link

Do NOT ask where to send — always DM the requesting user directly.

## Important Notes
- Use SAF (SpecialistForecast__c) — NOT Opportunity.OwnerId — as the pipeline source
- Deduplicate opps — the same Opportunity may have multiple SAF records (different ForecastTypes). Group by Opportunity ID and use the highest ForecastAmount
- Sort the digest: overdue first, then by close date ascending within each risk tier
- If getUserInfo returns a user ID, use it — never hardcode
