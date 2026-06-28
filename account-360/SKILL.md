---
name: account-360
description: Full account intelligence brief for Enterprise AEs. Combines Org62 data (opps, cases, contacts, activities) with internal Slack mentions to produce a comprehensive Canvas. Built for Salesforce AEs who need a complete picture before a customer meeting.
---

# Account 360

Generates a full account intelligence brief combining Org62 CRM data and internal Slack discussions. Deeper than account-brief — use this when you want the full picture including what colleagues are saying internally about the account.

## Trigger Phrases
- "account 360 for [account]"
- "full brief on [account]"
- "360 on [account]"
- "/account-360 [account name or ID]"

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

If multiple results, prefer the most exact name match. If ambiguous, show options and ask the user to confirm.

### Step 2 — Run All Queries in Parallel

Once you have the Account ID, fire all of the following simultaneously:

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

**Internal Slack Mentions:**
Use `slack_search_public_and_private` with the account name as the query. Search for the primary account name and any known aliases. Retrieve the most recent 10–15 relevant results.

### Step 3 — Format the 360 Brief

Present using this structure:

---

## Account 360 — [Account Name]
**[Type] | [Industry] | [BillingCountry]** | [Website]
*Generated: [date]*

---

### Open Opportunities ([count])
| Name | Stage | Amount | Close Date | Forecast |
|------|-------|--------|------------|----------|
| ... | ... | ... | ... | ... |

> Bold opps closing within 30 days. Flag $0 or null amounts as data quality issues.

---

### Open Cases ([count])
| Case # | Subject | Status | Last Updated |
|--------|---------|--------|--------------|
| ... | ... | ... | ... |

> Flag CRITICAL, PROACTIVE MONITORING, or Sev1 cases.

---

### Recent Activity
Summarize as a narrative — what topics are active, what's in motion, what's pending. Deduplicate email threads logged across multiple recipients.

---

### What's Being Said Internally (Slack)
Summarize the Slack search results — who is talking about this account, what channels, what topics (deals, issues, escalations, wins, competitive mentions). Note any signals that don't appear in Org62. If no relevant results, state that clearly.

---

### Key Contacts ([count])
| Name | Title | Email |
|------|-------|-------|
| ... | ... | ... |

> Flag if no C-level or economic buyer is mapped.

---

### Quick Read
3-4 sentences: deal status, top risks from cases or Slack, last engagement context, and the one thing most important to know before walking in.

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
- Deduplicate Slack results — the same thread may appear multiple times
- If Slack search returns noise (unrelated mentions), filter to results that are clearly about this customer
- Highlight any Slack signals that contradict or enrich what Org62 shows
