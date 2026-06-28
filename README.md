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
| `deal-intel` | Deep opportunity analysis with contact roles, activity timeline, and health scorecard |
| `pipeline-pulse` | At-risk pipeline digest using SpecialistForecast__c (SAF), delivered to your Slack DM |
| `close-plan` | Data-grounded internal Mutual Close Plan combining Org62 + account Slack channel |

## Installation

```bash
# Install all skills globally
npx skills add teco/AE-Skills@account-brief -g -y
npx skills add teco/AE-Skills@account-360 -g -y
npx skills add teco/AE-Skills@deal-intel -g -y
npx skills add teco/AE-Skills@pipeline-pulse -g -y
npx skills add teco/AE-Skills@close-plan -g -y
```

## Setup

Before using, add this to your `~/.claude/CLAUDE.md`:

```markdown
## My Org62 Identity
- Org62 User ID: YOUR_ORG62_USER_ID   # find via getUserInfo MCP call
- Slack User ID: YOUR_SLACK_USER_ID   # find via slack_search_users with your name

## Primary Accounts
List your accounts with Salesforce Account IDs here.

## Pipeline Source
Use SpecialistForecast__c (SAF) for pipeline — not Opportunity.OwnerId.
Specialist AEs are team members, not opp owners at stage 02+.
```

> **Slack caution:** The Slack MCP acts as you. Messages appear as sent by you. Draft sensitive messages (negotiations, legal, exec comms) before sending.

## Usage

```
/account-brief Claro S.A.
/account-360 Telefonica Brasil
/deal-intel MC SELA Renewal
/pipeline-pulse
/close-plan "MC SELA Renewal" #acct-claro-mc
```

## MEDDPICC Alignment

The `deal-intel` and `close-plan` skills are designed around MEDDPICC qualification. Risk flags map to MEDDPICC dimensions — missing economic buyer, no decision process mapped, no identified pain, etc.

## Contributing

Built for Salesforce Enterprise AEs. PRs welcome — especially for new Org62 objects, additional risk signals, or workflow improvements.
