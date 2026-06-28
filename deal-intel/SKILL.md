---
name: deal-intel
description: Deep-dives into a single Salesforce Opportunity from Org62. Given an opportunity name or ID, pulls full deal details, related contacts, recent activities with summaries, related open cases, and a deal health assessment.
---

# Deal Intel

Produces a comprehensive opportunity deep-dive from Org62. Use when the user wants to analyze a specific deal, prep for a deal review, or understand the full status of an opportunity.

## Trigger Phrases
- "deal intel for [opportunity name]"
- "deep dive on [opportunity]"
- "what's the status of the [opp name] deal"
- "analyze the [opp] opportunity"
- "/deal-intel [opportunity name or ID]"

## How to Execute

### Step 1 — Resolve the Opportunity

If the user provided a Salesforce Opportunity ID (starts with `006`), use it directly.

If the user provided a name or partial name, run:
```soql
SELECT Id, Name, StageName, Amount, CloseDate, ForecastCategoryName, AccountId, Account.Name
FROM Opportunity
WHERE Name LIKE '%<name>%' AND IsClosed = false
ORDER BY LastModifiedDate DESC
LIMIT 5
```

If multiple results, show the options and ask the user to confirm. Prefer exact or closest name matches.

### Step 2 — Run All Queries in Parallel

Once you have the Opportunity ID and Account ID, fire all queries simultaneously:

**Full Opportunity Detail:**
```soql
SELECT Id, Name, StageName, Amount, CloseDate, ForecastCategory, ForecastCategoryName,
       Type, Description, OwnerId, AccountId, Account.Name
FROM Opportunity
WHERE Id = '<opp_id>'
```

**Opportunity Contact Roles:**
```soql
SELECT ContactId, Contact.Name, Contact.Title, Contact.Email, Role, IsPrimary
FROM OpportunityContactRole
WHERE OpportunityId = '<opp_id>'
```

**Recent Activities on the Opportunity (last 15):**
```soql
SELECT Id, Subject, ActivityDate, Status, TaskSubtype, Description, OwnerId
FROM Task
WHERE WhatId = '<opp_id>'
ORDER BY LastModifiedDate DESC
LIMIT 15
```

**Open Cases on the Account:**
```soql
SELECT Id, CaseNumber, Subject, Status, Priority, LastModifiedDate
FROM Case
WHERE AccountId = '<account_id>' AND IsClosed = false
ORDER BY LastModifiedDate DESC
LIMIT 8
```

### Step 3 — Format the Deal Intel

Present using this structure:

---

## Deal Intel — [Opportunity Name]

**Account:** [Account Name]
**Stage:** [StageName] | **Forecast:** [ForecastCategoryName] | **Type:** [Type]
**Amount:** $[Amount] | **Close Date:** [CloseDate]

---

### Deal Summary
2-3 sentences on what this deal is, where it stands, and the key context from the description (if any).

---

### Contact Roles ([count])
| Name | Title | Email | Role | Primary |
|------|-------|-------|------|---------|
| ... | ... | ... | ... | ... |

If no contact roles found, note it as a risk — no contacts mapped to the deal.

---

### Activity Timeline ([count] recent activities)

Group and summarize activities by topic thread rather than listing every duplicate. For each distinct topic:
- **[Thread / Subject]** — [Date range] — [1-2 sentence summary of what's happening, who's involved, what's resolved or still pending]

For standalone tasks (Procurement Review, system calls, etc.), list them briefly.

---

### Related Open Cases ([count])
| Case # | Subject | Status | Last Updated |
|--------|---------|--------|--------------|
| ... | ... | ... | ... |

Flag any cases that could be blockers to closing (critical errors, unresolved technical issues, billing disputes).

---

### Deal Health Assessment

| Dimension | Status | Notes |
|-----------|--------|-------|
| **Engagement** | 🟢 / 🟡 / 🔴 | Last activity date, frequency |
| **Contacts** | 🟢 / 🟡 / 🔴 | Key roles mapped, economic buyer present |
| **Technical** | 🟢 / 🟡 / 🔴 | Open cases or known issues affecting deal |
| **Timeline** | 🟢 / 🟡 / 🔴 | Close date realism given current stage |
| **Forecast** | 🟢 / 🟡 / 🔴 | Forecast category vs. stage alignment |

**Risks:** Top 1-3 risks.
**Next Steps:** Most obvious next actions based on the data.

---

## Important Notes
- Email threads are often logged once per recipient — deduplicate by subject + date when summarizing activities
- A deal in stage 04+ with no activity in 14+ days should flag as 🔴 engagement risk
- If Amount is null or $0, flag it — missing ARR is a data quality issue
- If close date is in the past and deal is still open, flag it prominently
- For the health assessment: 🟢 healthy, 🟡 needs attention, 🔴 at risk
