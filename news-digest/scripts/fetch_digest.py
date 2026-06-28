#!/usr/bin/env python3
"""
Fetch RSS feeds for the news digest and output structured JSON.
Usage: python fetch_digest.py [--period 24h|7d]
"""

import argparse
import json
import re
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
import xml.etree.ElementTree as ET

FEEDS = [
    # SALESFORCE & AGENTFORCE
    {"section": "Salesforce & Agentforce", "name": "Salesforce Blog",         "url": "https://www.salesforce.com/blog/feed/"},
    {"section": "Salesforce & Agentforce", "name": "SaaS News — Salesforce",  "url": "https://thesaasnews.com/tag/salesforce/feed/"},
    {"section": "Salesforce & Agentforce", "name": "TechCrunch — Enterprise", "url": "https://techcrunch.com/category/enterprise/feed/"},
    {"section": "Salesforce & Agentforce", "name": "ZDNet — Enterprise AI",   "url": "https://www.zdnet.com/topic/artificial-intelligence/rss.xml"},
    {"section": "Salesforce & Agentforce", "name": "VentureBeat — AI",        "url": "https://venturebeat.com/category/ai/feed/"},
    # ANTHROPIC & CLAUDE
    {"section": "Anthropic & Claude", "name": "Hacker News — Anthropic",       "url": "https://hnrss.org/search?q=anthropic"},
    {"section": "Anthropic & Claude", "name": "MIT Technology Review — AI",    "url": "https://www.technologyreview.com/topic/artificial-intelligence/feed/"},
    {"section": "Anthropic & Claude", "name": "The Verge — Anthropic",         "url": "https://www.theverge.com/rss/anthropic/index.xml"},
    {"section": "Anthropic & Claude", "name": "Ars Technica — AI",             "url": "https://feeds.arstechnica.com/arstechnica/technology-lab"},
    # MADTECH / ADTECH
    {"section": "MadTech / AdTech", "name": "SaaS News — Marketing Tech",     "url": "https://thesaasnews.com/tag/marketing/feed/"},
    {"section": "MadTech / AdTech", "name": "Digiday — Marketing & AdTech",   "url": "https://digiday.com/category/marketing/feed/"},
    {"section": "MadTech / AdTech", "name": "AdExchanger",                    "url": "https://www.adexchanger.com/feed/"},
    # OPENAI
    {"section": "OpenAI", "name": "OpenAI Newsroom",              "url": "https://openai.com/news/rss.xml"},
    {"section": "OpenAI", "name": "Hacker News — OpenAI",         "url": "https://hnrss.org/search?q=openai"},
    {"section": "OpenAI", "name": "TechCrunch — OpenAI",          "url": "https://techcrunch.com/tag/openai/feed/"},
    {"section": "OpenAI", "name": "MIT Technology Review — OpenAI","url": "https://www.technologyreview.com/topic/artificial-intelligence/feed/"},
    # GEMINI
    {"section": "Gemini", "name": "Google Blog — AI",     "url": "https://blog.google/technology/ai/rss/"},
    {"section": "Gemini", "name": "9to5Google — Gemini",  "url": "https://9to5google.com/guides/gemini/feed/"},
    {"section": "Gemini", "name": "The Verge — Google",   "url": "https://www.theverge.com/google/rss/index.xml"},
    {"section": "Gemini", "name": "Hacker News — Gemini", "url": "https://hnrss.org/search?q=gemini"},
    # AI
    {"section": "AI", "name": "MIT Technology Review — Computing", "url": "https://www.technologyreview.com/topic/computing/feed/"},
    {"section": "AI", "name": "SaaS News — AI Startups",           "url": "https://thesaasnews.com/tag/ai/feed/"},
    {"section": "AI", "name": "Hacker News — AI",                  "url": "https://hnrss.org/search?q=ai"},
    {"section": "AI", "name": "TNW — Neural",                      "url": "https://thenextweb.com/category/neural/feed"},
    {"section": "AI", "name": "WSJ — Technology",                  "url": "https://feeds.a.dj.com/rss/RSSWSJD.xml"},
    {"section": "AI", "name": "Ars Technica — Tech Policy",        "url": "https://feeds.arstechnica.com/arstechnica/technology-lab"},
    {"section": "AI", "name": "Machine Learning Mastery",          "url": "https://machinelearningmastery.com/blog/feed/"},
    {"section": "AI", "name": "The Decoder",                       "url": "https://the-decoder.com/feed/"},
    {"section": "AI", "name": "NVIDIA Developer Blog",             "url": "https://developer.nvidia.com/blog/feed"},
    {"section": "AI", "name": "Berkeley BAIR Blog",                "url": "https://bair.berkeley.edu/blog/feed.xml"},
    {"section": "AI", "name": "404 Media",                         "url": "https://www.404media.co/rss", "max_items": 5},
    {"section": "AI", "name": "The New Stack",                     "url": "https://thenewstack.io/feed"},
    {"section": "AI", "name": "AI TechPark",                       "url": "https://ai-techpark.com/category/ai/feed/"},
    {"section": "AI", "name": "r/aipromptprogramming",             "url": "https://www.reddit.com/r/aipromptprogramming/.rss"},
    {"section": "AI", "name": "The Guardian — AI",                 "url": "https://www.theguardian.com/technology/artificialintelligenceai/rss"},
    {"section": "AI", "name": "Science Daily — AI",                "url": "https://www.sciencedaily.com/rss/computers_math/artificial_intelligence.xml"},
    {"section": "AI", "name": "TechRepublic — AI",                 "url": "https://www.techrepublic.com/rssfeeds/topic/artificial-intelligence/"},
    {"section": "AI", "name": "Chain of Thought (Every.to)",       "url": "https://every.to/chain-of-thought/feed.xml"},
    {"section": "AI", "name": "Artificial Intelligence Blog",      "url": "https://www.artificial-intelligence.blog/ai-news?format=rss"},
    # DATA
    {"section": "Data", "name": "Towards Data Science", "url": "https://towardsdatascience.com/feed"},
    {"section": "Data", "name": "Analytics Vidhya",     "url": "https://www.analyticsvidhya.com/feed/"},
    {"section": "Data", "name": "Databricks Blog",      "url": "https://www.databricks.com/feed"},
    {"section": "Data", "name": "Data Science at Home", "url": "https://datascienceathome.com/feed.xml"},
    {"section": "Data", "name": "Datafloq",             "url": "https://datafloq.com/feed/?post_type=post"},
    {"section": "Data", "name": "r/datascience",        "url": "https://www.reddit.com/r/datascience/.rss"},
]

SECTION_ORDER = [
    "Salesforce & Agentforce",
    "Anthropic & Claude",
    "MadTech / AdTech",
    "OpenAI",
    "Gemini",
    "AI",
    "Data",
]

MAX_ITEMS_DAILY  = 5
MAX_ITEMS_WEEKLY = 10


def strip_html(text):
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("&nbsp;", " ").replace("&amp;", "&") \
               .replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"')
    text = re.sub(r"\s+", " ", text).strip()
    return text[:200]


def parse_date(date_str):
    if not date_str:
        return None
    try:
        return parsedate_to_datetime(date_str).astimezone(timezone.utc)
    except Exception:
        pass
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(date_str.strip(), fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except Exception:
            pass
    return None


def format_date(date_str):
    dt = parse_date(date_str)
    if not dt:
        return ""
    # Convert to BRT (UTC-3)
    brt = dt.astimezone(timezone(timedelta(hours=-3)))
    return brt.strftime("%b %-d, %H:%M")


def fetch_feed(feed, cutoff, max_items):
    articles = []
    try:
        req = urllib.request.Request(
            feed["url"],
            headers={"User-Agent": "Mozilla/5.0 (compatible; NewsDigest/1.0)"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            raw = resp.read().decode("utf-8", errors="replace")

        # Skip HTML responses
        if raw.lstrip().startswith("<!DOCTYPE") or raw.lstrip().startswith("<html"):
            return articles

        # Fix bare ampersands
        raw = re.sub(r"&(?!(amp|lt|gt|quot|apos);)", "&amp;", raw)

        root = ET.fromstring(raw)
        ns = root.tag.split("}")[0].lstrip("{") if "}" in root.tag else ""
        ns_map = {"atom": ns} if ns else {}

        # RSS 2.0
        channel = root.find("channel")
        if channel is not None:
            items = channel.findall("item")
            for item in items:
                title   = item.findtext("title", "").strip()
                link    = item.findtext("link", "").strip()
                date_str = item.findtext("pubDate") or item.findtext("dc:date")
                summary = strip_html(item.findtext("description") or item.findtext("summary") or "")

                if cutoff and date_str:
                    pub = parse_date(date_str)
                    if pub and pub < cutoff:
                        continue

                if link and len(articles) < max_items:
                    articles.append({
                        "source": feed["name"],
                        "section": feed["section"],
                        "title": title or "(no title)",
                        "url": link,
                        "date": date_str or "",
                        "date_formatted": format_date(date_str),
                        "summary": summary,
                    })
        else:
            # Atom
            atom_ns = f"{{{ns}}}" if ns else ""
            entries = root.findall(f"{atom_ns}entry")
            for entry in entries:
                title_el = entry.find(f"{atom_ns}title")
                title = title_el.text.strip() if title_el is not None and title_el.text else ""

                link_el = entry.find(f"{atom_ns}link")
                link = ""
                if link_el is not None:
                    link = link_el.get("href", "") or link_el.text or ""
                link = link.strip()

                updated_el = entry.find(f"{atom_ns}updated") or entry.find(f"{atom_ns}published")
                date_str = updated_el.text.strip() if updated_el is not None and updated_el.text else ""

                if cutoff and date_str:
                    pub = parse_date(date_str)
                    if pub and pub < cutoff:
                        continue

                summary_el = entry.find(f"{atom_ns}summary") or entry.find(f"{atom_ns}content")
                summary = strip_html(summary_el.text if summary_el is not None else "")

                if link and len(articles) < max_items:
                    articles.append({
                        "source": feed["name"],
                        "section": feed["section"],
                        "title": title or "(no title)",
                        "url": link,
                        "date": date_str,
                        "date_formatted": format_date(date_str),
                        "summary": summary,
                    })

    except Exception as e:
        print(f"[WARN] {feed['name']}: {e}", file=sys.stderr)

    return articles


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--period", choices=["24h", "7d"], default="24h")
    args = parser.parse_args()

    period_hours = 24 if args.period == "24h" else 7 * 24
    max_items = MAX_ITEMS_DAILY if args.period == "24h" else MAX_ITEMS_WEEKLY
    cutoff = datetime.now(timezone.utc) - timedelta(hours=period_hours)

    seen_urls = set()
    # Build sections dict preserving display order
    sections = {s: [] for s in SECTION_ORDER}

    for feed in FEEDS:
        feed_max = feed.get("max_items", max_items)
        articles = fetch_feed(feed, cutoff, feed_max)
        section = feed["section"]
        if section not in sections:
            sections[section] = []

        source_group = next((g for g in sections[section] if g["source"] == feed["name"]), None)
        if source_group is None:
            source_group = {"source": feed["name"], "items": []}
            sections[section].append(source_group)

        for article in articles:
            if article["url"] not in seen_urls:
                seen_urls.add(article["url"])
                source_group["items"].append({
                    "title": article["title"],
                    "url": article["url"],
                    "date": article["date_formatted"],
                    "summary": article["summary"],
                })

    # Remove empty sections and empty source groups
    output = {}
    for section in SECTION_ORDER:
        groups = [g for g in sections.get(section, []) if g["items"]]
        if groups:
            output[section] = groups

    print(json.dumps({"period": args.period, "sections": output}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
