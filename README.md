# AE Skills for Claude Code

A collection of Claude Code skills built for Enterprise Account Executives at Salesforce. Designed for specialist AEs covering Marketing Cloud, Data Cloud, and Agentforce in large enterprise accounts.

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Org62 MCP server connected (read access)
- Slack MCP server connected (authenticated as your user)

## Skills

| Skill | Description |
|-------|-------------|
| `account-brief` | Pre-meeting account snapshot from Org62 — opps, cases, contacts, activities |
| `account-360` | Full account intelligence combining Org62 data + internal Slack mentions |
| `deal-intel` | MEDDPICC-framed deep dive on a specific opportunity with contact roles and activity timeline |
| `pipeline-pulse` | At-risk pipeline digest using SpecialistForecast__c (SAF), delivered to your Slack DM |
| `close-plan` | Challenger-framed internal Mutual Close Plan combining Org62 + account Slack channel |
| `sales-discovery-questions` | MEDDPICC gap analysis → prioritized discovery questions for an upcoming call |
| `opp-health-check` | MEDDPICC scorecard + forecast confidence verdict + prioritized action plan |
| `news-digest` | On-demand RSS digest across Salesforce, AI, MadTech, OpenAI, Gemini, and Data topics — delivered as Slack DM |
| `salesforce-presentation` | Salesforce Brand Central-compliant .pptx decks — QBRs, proposals, event decks, internal readouts |

### Deal Workflow Chain

These skills are designed to chain together:

```
/opp-health-check → surfaces MEDDPICC gaps
/sales-discovery-questions → generates questions to fill those gaps
/close-plan → builds the close plan once qualification is solid
```

## Installation

```bash
# Install all skills globally
npx skills add teco/AE-Skills@account-brief -g -y
npx skills add teco/AE-Skills@account-360 -g -y
npx skills add teco/AE-Skills@deal-intel -g -y
npx skills add teco/AE-Skills@pipeline-pulse -g -y
npx skills add teco/AE-Skills@close-plan -g -y
npx skills add teco/AE-Skills@sales-discovery-questions -g -y
npx skills add teco/AE-Skills@opp-health-check -g -y
npx skills add teco/AE-Skills@news-digest -g -y
npx skills add teco/AE-Skills@salesforce-presentation -g -y
```

## Setup

Before using, add this to your `~/.claude/CLAUDE.md`:

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

> **Slack caution:** The Slack MCP acts as you. Messages appear as sent by you. Draft sensitive messages (negotiations, legal, exec comms) before sending. Informational content (account briefs, digests) can be sent directly.

## Usage

```
/account-brief Claro S.A.
/account-360 Telefonica Brasil
/deal-intel 006ed00000dKYjpAAG
/pipeline-pulse
/close-plan "MC SELA Renewal" #acct-claro-mc
/sales-discovery-questions Claro, stage 03, VP Digital Marketing
/opp-health-check "MC SELA Renewal"
/news-digest
/salesforce-presentation "Claro QBR Q3 2026"
```

## MEDDPICC Alignment

All deal-facing skills are built around MEDDPICC and Challenger Sale framing:
- Risk flags in `deal-intel` and `pipeline-pulse` map to MEDDPICC dimensions
- `opp-health-check` scores each dimension (Confirmed / Partial / Gap / Red Flag) and produces a prioritized action plan
- `sales-discovery-questions` maps known context against MEDDPICC to identify gaps and generates targeted questions
- `close-plan` uses Challenger framing — reframe, rational drowning, emotional impact
- Missing economic buyer, undefined decision process, and no identified pain are always flagged as blockers

## Contributing

Built for Salesforce Enterprise AEs. PRs welcome — especially for new Org62 objects, additional risk signals, or workflow improvements.
