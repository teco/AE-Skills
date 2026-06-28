---
name: news-digest
description: Fetches the latest news across Salesforce/Agentforce, Anthropic/Claude, MadTech/AdTech, OpenAI, Gemini, AI, and Data topics from ~40 RSS feeds and delivers a formatted digest as a Slack DM. Trigger whenever the user asks for a news digest, says "what's in the news," "send me the digest," "news update," or uses /news-digest. Trigger for both daily (last 24h) and weekly (last 7 days) requests.
---

# News Digest

Fetches ~40 RSS feeds across 7 topic sections, filters to the requested time window, deduplicates, and delivers a formatted digest as a Slack DM to Terence (`U01GF1EBDPW`).

## Trigger

- `/news-digest` — daily digest (last 24 hours)
- `/news-digest weekly` — weekly digest (last 7 days)
- Natural language: "send me the digest," "what's in the news," "news update," "weekly digest"

## Step 1 — Fetch the feeds

Run the bundled script. For daily:
```bash
python3 ~/.claude/skills/news-digest/scripts/fetch_digest.py --period 24h
```
For weekly:
```bash
python3 ~/.claude/skills/news-digest/scripts/fetch_digest.py --period 7d
```

The script outputs JSON:
```json
{
  "period": "24h",
  "sections": {
    "Salesforce & Agentforce": [
      {
        "source": "Salesforce Blog",
        "items": [
          {"title": "...", "url": "https://...", "date": "Jun 28, 09:15", "summary": "..."}
        ]
      }
    ]
  }
}
```

Feeds that had no new articles in the window are omitted automatically.

## Step 2 — Format as Slack mrkdwn

Build one message per section. Format:

```
*SALESFORCE & AGENTFORCE*

*Salesforce Blog*
• <https://...|Article title> · Jun 28, 09:15
  Short summary…

*VentureBeat — AI*
• <https://...|Article title> · Jun 28, 08:44
```

Rules:
- Section header in ALL CAPS bold
- Source name in bold, on its own line
- Each article as a bullet: linked title, then ` · date` if available
- Summary on the next line, indented with two spaces, only if non-empty
- Skip sources with no items

## Step 3 — Send as Slack DM

Send to `U01GF1EBDPW` (Terence).

For **daily digests**: send all sections as a single message if the total content is under ~3,000 characters. If longer, send one message per section.

For **weekly digests**: always send one message per section — weekly content is too long for a single message.

Start each batch of messages with a brief header line:
```
*Daily Digest* — Jun 28, 2026
```
or
```
*Weekly Digest* — Jun 22–28, 2026
```

## Notes

- If the script returns no articles (all feeds empty for the window), report that to the user rather than sending an empty DM.
- Do not send articles with no title and no URL.
- If `python3` is unavailable, try `python`.
