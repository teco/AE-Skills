---
name: account-brief
description: Generates a structured pre-meeting account brief from Org62. Given an account name or Salesforce ID, pulls account info, open opportunities, top open cases, recent activities, and key contacts in one consolidated summary.
---

# Account Brief

Generates a pre-meeting account brief from Org62 data. Use when the user asks for an account brief, wants to prepare for a customer call, or needs a quick snapshot of an account.

## Trigger Phrases
- "account brief for [account]"
- "brief me on [account]"
- "prepare me for my call with [account]"
- "what's the status of [account]"
- "/account-brief [account name or ID]"

## How to Execute

### Step 1 — Resolve the Account

If the user provided a Salesforce Account ID (starts with `001`), use it directly.

If the user provided a name, run:
```soql
SELECT Id, Name, Type, Industry, BillingCountry, Website, OwnerId
FROM Account
WHERE Name LIKE '%<name>%'
ORDER BY LastModifiedDate DESC
LIMIT 5
```

If multiple results, pick the most exact name match (prefer records where Name = exact input). If still ambiguous, show the user the options and ask them to confirm.

### Step 2 — Run All Queries in Parallel

Once you have the Account ID, fire all of the following queries simultaneously:

**Open Opportunities:**
```soql
SELECT Id, Name, StageName, Amount, CloseDate, ForecastCategoryName, Type
FROM Opportunity
WHERE AccountId = '<id>' AND IsClosed = false
ORDER BY CloseDate ASC
LIMIT 10
```

**Open Cases (top 10 most recently modified):**
```soql
SELECT Id, CaseNumber, Subject, Status, Priority, LastModifiedDate
FROM Case
WHERE AccountId = '<id>' AND IsClosed = false
ORDER BY LastModifiedDate DESC
LIMIT 10
```

**Recent Activities (last 10):**
```soql
SELECT Id, Subject, ActivityDate, Status, TaskSubtype, Description
FROM Task
WHERE WhatId = '<id>'
ORDER BY LastModifiedDate DESC
LIMIT 10
```

**Key Contacts:**
```soql
SELECT Id, Name, Title, Email
FROM Contact
WHERE AccountId = '<id>'
ORDER BY LastModifiedDate DESC
LIMIT 8
```

### Step 3 — Format the Brief

Present the output as a clean, scannable brief using this structure:

---

## Account Brief — [Account Name]
**[Type] | [Industry] | [BillingCountry]** | [Website]

---

### Open Opportunities ([count])
| Name | Stage | Amount | Close Date | Forecast |
|------|-------|--------|------------|----------|
| ... | ... | ... | ... | ... |

---

### Open Cases ([count] shown, sorted by recent activity)
| Case # | Subject | Status | Last Updated |
|--------|---------|--------|--------------|
| ... | ... | ... | ... |

> Flag any cases with Status = New or critical/proactive monitoring subjects.

---

### Recent Activity (last [count])
Summarize the last 10 activities as a brief narrative — what topics are being discussed, what's in motion, any blockers or pending items visible in the thread subjects/descriptions.

---

### Key Contacts ([count])
| Name | Title | Email |
|------|-------|-------|
| ... | ... | ... |

---

### Quick Read
2-3 sentences synthesizing what's most important: deal status, any open risks from cases, last engagement context. This is the "walking into the room" paragraph.

---

### Step 4 — Ask Where to Send

After presenting the brief, ask:
> "Would you like me to post this to Slack? Tell me a channel (e.g. #acct-claro-mc) or a person to DM."

If destination provided:
1. Create a Slack Canvas (`slack_create_canvas`) with the full brief in Canvas-flavored Markdown
2. Resolve the destination with `slack_search_channels` or `slack_search_users` as needed
3. Send message with Canvas link and Quick Read summary via `slack_send_message`
4. Can post to channel AND DM simultaneously if requested

## Important Notes
- Always create the Canvas first, then send the message with the link — never paste the raw brief as a message
- If there are more than 10 open cases, note the total and show the 10 most recent
- Summarize email threads rather than listing each recipient copy as a separate entry
- Highlight any opportunities closing within 30 days in bold
- Flag cases with "CRITICAL", "PROACTIVE MONITORING", or "Sev1" in the subject
- If no activities are found on the Account directly, also check the most recent open Opportunity for tasks
