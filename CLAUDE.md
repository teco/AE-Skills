# Claude Code — AE Skills Repo

This repo contains Claude Code skills for Enterprise Account Executives at Salesforce, built around Marketing Cloud, Data Cloud, and Agentforce specialist motions.

## What This Repo Provides

Seven skills for the day-to-day AE workflow:

| Skill | When to use |
|---|---|
| `/account-brief` | Before any customer meeting — pulls Org62 opps, cases, contacts, activities |
| `/account-360` | Full account picture combining Org62 + internal Slack mentions |
| `/deal-intel` | MEDDPICC-framed deep dive on a specific opportunity |
| `/pipeline-pulse` | SAF pipeline review with risk flags, delivered to Slack DM |
| `/close-plan` | Challenger-framed close plan grounded in Org62 + account Slack channel |
| `/sales-discovery-questions` | MEDDPICC gap analysis → targeted discovery questions for an upcoming call |
| `/opp-health-check` | MEDDPICC scorecard + forecast confidence assessment + prioritized action plan |

## Required Setup

### 1. MCP Servers
Connect these before using the skills:
- **Org62 MCP** — read-only SOQL access to internal Salesforce CRM
- **Slack MCP** — authenticated as your own user (messages send as you)

### 2. Your Identity in CLAUDE.md
Add this block to your `~/.claude/CLAUDE.md`:

```markdown
## My Identity
- Org62 User ID: YOUR_ORG62_USER_ID      # run getUserInfo via Org62 MCP
- Slack User ID: YOUR_SLACK_USER_ID      # run slack_search_users with your name

## Primary Accounts
- Account Name — Salesforce Account ID (products)

## Pipeline Source
Use SpecialistForecast__c (SAF) — not Opportunity.OwnerId.
As a specialist AE, deals are territory-AE-owned at stage 02+; you are a team member.
SAF query template:
  SELECT ... FROM SpecialistForecast__c WHERE SpecialistId = 'YOUR_ORG62_USER_ID'
```

### 3. Recommended Plugins to Install
Install these Claude Code plugins for the best experience:

```bash
# Core workflow plugins
claude plugins install superpowers@claude-plugins-official       # brainstorming, debugging, git workflows
claude plugins install slack@claude-plugins-official             # Slack read/write, canvas
claude plugins install remember@claude-plugins-official          # persistent memory across sessions

# Optional but useful
claude plugins install notion@claude-plugins-official            # Notion pages and databases
claude plugins install skill-creator@claude-plugins-official     # build your own skills
claude plugins install claude-md-management@claude-plugins-official  # manage CLAUDE.md
```

### 4. Recommended Skills from the Ecosystem
These Salesforce platform skills complement the AE workflow:

```bash
# SOQL and data access
npx skills add <source>@querying-soql -g -y

# Salesforce docs lookup
npx skills add <source>@fetching-salesforce-docs -g -y

# Data Cloud (if relevant to your accounts)
npx skills add <source>@retrieving-datacloud -g -y
npx skills add <source>@segmenting-datacloud -g -y

# Agentforce (if relevant to your accounts)
npx skills add <source>@developing-agentforce -g -y
```

## Sales Methodology

These skills are built around **MEDDPICC** and **Challenger Sale**:
- Risk flags in `deal-intel` and `pipeline-pulse` map to MEDDPICC dimensions
- `close-plan` uses Challenger framing (reframe, rational drowning, emotional impact)
- `sales-discovery-questions` maps known context against MEDDPICC to identify gaps and generate targeted questions
- `opp-health-check` scores each MEDDPICC dimension and produces a prioritized action plan — chains into discovery questions or close plan
- Missing economic buyer, undefined decision process, and no identified pain are always flagged as blockers

## Slack Caution

The Slack MCP acts as **you**. Messages appear as sent by your user.
- Informational content (account briefs, summaries) — send directly
- Sensitive content (negotiations, exec comms, legal) — review a draft before sending

## Usage Examples

```
/account-brief Claro S.A.
/account-360 Telefonica Brasil
/deal-intel 006ed00000dKYjpAAG
/pipeline-pulse
/close-plan "MC SELA Renewal" #acct-claro-mc
/sales-discovery-questions Claro, stage 03, VP Digital Marketing
/opp-health-check "MC SELA Renewal"
```
