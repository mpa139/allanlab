#!/usr/bin/env python3
"""
Weekly newsletter draft generator.
Reads _data/ YAML files, builds a Markdown digest, and creates a GitHub Issue.
Triggered by .github/workflows/newsletter.yml every Monday at 08:00 UTC.
"""

import os
import json
import datetime
import requests
import yaml
from dateutil import parser as dateparser

REPO = os.environ["GITHUB_REPOSITORY"]
GH_TOKEN = os.environ["GITHUB_TOKEN"]
SITE_URL = "https://aicentre-csg.github.io"  # update to your actual GitHub Pages URL

DATA_DIR = "_data"
LOOKAHEAD_DAYS = 14   # upcoming events/talks window
LOOKBACK_DAYS = 7     # recent news/papers window


def load_yaml(filename):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def parse_date(date_str):
    """Parse various date string formats into a date object. Returns None on failure."""
    if not date_str:
        return None
    try:
        return dateparser.parse(str(date_str)).date()
    except Exception:
        return None


def build_newsletter():
    today = datetime.date.today()
    lookahead = today + datetime.timedelta(days=LOOKAHEAD_DAYS)
    lookback = today - datetime.timedelta(days=LOOKBACK_DAYS)

    events = load_yaml("events.yml")
    talks = load_yaml("talks.yml")
    news = load_yaml("news.yml")
    publist = load_yaml("publist.yml")
    grants = load_yaml("grants.yml")

    lines = [
        f"# 📰 AI Centre@CSG — Newsletter Draft {today.strftime('%d %B %Y')}",
        "",
        "> *Auto-generated draft. Review and edit before sending.*",
        "",
    ]

    # ── Upcoming Events & Talks ──────────────────────────────────────────────
    upcoming = []
    for item in events:
        d = parse_date(item.get("date"))
        if d and today <= d <= lookahead:
            upcoming.append(("event", d, item))
    for item in talks:
        d = parse_date(item.get("date"))
        if d and today <= d <= lookahead:
            upcoming.append(("talk", d, item))
    upcoming.sort(key=lambda x: x[1])

    lines.append("## 📅 Upcoming Events & Talks (next 2 weeks)")
    lines.append("")
    if upcoming:
        for kind, d, item in upcoming:
            if kind == "event":
                title = item.get("title", "")
                link = item.get("link", "")
                loc = item.get("location", "")
                speaker = item.get("speaker", "")
                etype = item.get("type", "")
                label = f"**{d.strftime('%-d %B')}** — [{title}]({link})" if link else f"**{d.strftime('%-d %B')}** — {title}"
                detail = " | ".join(filter(None, [etype.capitalize() if etype else "", speaker, loc]))
                lines.append(f"- {label}")
                if detail:
                    lines.append(f"  *{detail}*")
            else:  # talk
                title = item.get("title", "")
                speaker = item.get("speaker", "")
                affil = item.get("affiliation", "")
                speaker_str = f"{speaker}, {affil}" if affil else speaker
                lines.append(f"- **{d.strftime('%-d %B')}** — {title}")
                lines.append(f"  *Talk by {speaker_str}*")
        lines.append("")
    else:
        lines.append("*No events or talks in the next two weeks.*")
        lines.append("")

    # ── Recent News ──────────────────────────────────────────────────────────
    recent_news = []
    for item in news:
        d = parse_date(item.get("date"))
        if d and lookback <= d <= today:
            recent_news.append((d, item.get("headline", "")))
    recent_news.sort(key=lambda x: x[0], reverse=True)

    lines.append("## 📢 Recent News (last 7 days)")
    lines.append("")
    if recent_news:
        for d, headline in recent_news:
            lines.append(f"- **{d.strftime('%-d %B')}** — {headline}")
        lines.append("")
    else:
        lines.append("*No news items in the last 7 days.*")
        lines.append("")

    # ── New Papers ───────────────────────────────────────────────────────────
    recent_papers = []
    for pub in publist:
        d = parse_date(pub.get("date"))
        if d and lookback <= d <= today:
            recent_papers.append((d, pub))
    recent_papers.sort(key=lambda x: x[0], reverse=True)

    lines.append("## 📄 New Papers (last 7 days)")
    lines.append("")
    if recent_papers:
        for d, pub in recent_papers:
            title = pub.get("title", "")
            authors = pub.get("authors", "")
            url = (pub.get("link") or {}).get("url", "")
            venue = pub.get("book") or pub.get("journal") or pub.get("conference") or ""
            title_str = f"[{title}]({url})" if url else title
            lines.append(f"- **{d.strftime('%-d %B')}** — {title_str}")
            if authors:
                lines.append(f"  *{authors}*")
            if venue:
                lines.append(f"  {venue}")
        lines.append("")
    else:
        lines.append("*No new papers in the last 7 days.*")
        lines.append("")

    # ── Active Grants ────────────────────────────────────────────────────────
    active_grants = [g for g in grants if g.get("status") == "active"]

    lines.append("## 💰 Active Grants")
    lines.append("")
    if active_grants:
        for g in active_grants:
            title = g.get("title", "")
            funder = g.get("funder", "")
            amount = g.get("amount", "")
            pi = g.get("pi", "")
            end = parse_date(g.get("end_date"))
            end_str = end.strftime("%B %Y") if end else ""
            detail = " | ".join(filter(None, [funder, amount, f"PI: {pi}" if pi else "", f"ends {end_str}" if end_str else ""]))
            lines.append(f"- **{title}**")
            if detail:
                lines.append(f"  {detail}")
        lines.append("")
    else:
        lines.append("*No active grants listed.*")
        lines.append("")

    lines.append("---")
    lines.append(f"*Draft generated automatically on {today.strftime('%A %-d %B %Y')}.*")
    lines.append(f"*Edit and send via your preferred email platform.*")

    return "\n".join(lines)


def ensure_label(headers):
    """Create the 'newsletter-draft' label if it doesn't exist."""
    url = f"https://api.github.com/repos/{REPO}/labels"
    resp = requests.get(url, headers=headers)
    existing = {l["name"] for l in resp.json()} if resp.ok else set()
    if "newsletter-draft" not in existing:
        requests.post(url, headers=headers, json={
            "name": "newsletter-draft",
            "color": "0075ca",
            "description": "Auto-generated weekly newsletter draft",
        })


def create_issue(title, body):
    headers = {
        "Authorization": f"Bearer {GH_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    ensure_label(headers)
    url = f"https://api.github.com/repos/{REPO}/issues"
    payload = {"title": title, "body": body, "labels": ["newsletter-draft"]}
    resp = requests.post(url, headers=headers, json=payload)
    resp.raise_for_status()
    issue = resp.json()
    print(f"Created issue #{issue['number']}: {issue['html_url']}")


if __name__ == "__main__":
    today = datetime.date.today()
    issue_title = f"📰 Newsletter Draft — {today.strftime('%Y-%m-%d')}"
    body = build_newsletter()
    create_issue(issue_title, body)
