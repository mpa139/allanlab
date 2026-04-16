#!/usr/bin/env python3
"""
Social media posting script.
Detects new entries added to _data/ YAML files via git diff, formats a message
per new item, and posts to Mastodon, Bluesky, X (Twitter), and LinkedIn.

Set the environment variable SOCIAL_DRY_RUN=true to log messages without posting.

Triggered by .github/workflows/social-media.yml on push to gh-pages.
"""

import os
import re
import subprocess
import textwrap
import yaml
import requests

DRY_RUN = os.environ.get("DRY_RUN", "").lower() == "true"
SITE_URL = "https://aicentre-csg.github.io"  # update to your actual GitHub Pages URL
HASHTAGS = "#AI #MachineLearning #Research #AICentre"

# ── Helpers ──────────────────────────────────────────────────────────────────

def git_diff_added_blocks(path):
    """Return lines added in HEAD vs HEAD~1 for the given file path."""
    result = subprocess.run(
        ["git", "diff", "HEAD~1", "HEAD", "--", path],
        capture_output=True, text=True
    )
    added = [l[1:] for l in result.stdout.splitlines() if l.startswith("+") and not l.startswith("+++")]
    return "\n".join(added)


def extract_new_entries(diff_text, all_entries, key_field):
    """
    Parse YAML diff lines to find new entries.
    Falls back to returning entries whose key_field value appears in the diff.
    """
    new = []
    for entry in (all_entries or []):
        val = str(entry.get(key_field, ""))
        if val and val in diff_text:
            new.append(entry)
    return new


def truncate(text, max_len):
    return text if len(text) <= max_len else text[:max_len - 1] + "…"


def format_event(item):
    title = item.get("title", "")
    date = item.get("date", "")
    location = item.get("location", "")
    speaker = item.get("speaker", "")
    link = item.get("link", "")
    parts = [f"📅 {title}", f"📆 {date}"]
    if speaker:
        parts.append(f"🎤 {speaker}")
    if location:
        parts.append(f"📍 {location}")
    if link:
        parts.append(link)
    parts.append(HASHTAGS)
    return "\n".join(parts)


def format_talk(item):
    title = item.get("title", "")
    date = item.get("date", "")
    speaker = item.get("speaker", "")
    affil = item.get("affiliation", "")
    speaker_str = f"{speaker} ({affil})" if affil else speaker
    parts = [f"🗣️ {title}", f"📆 {date}", f"👤 {speaker_str}", HASHTAGS]
    return "\n".join(parts)


def format_news(item):
    headline = item.get("headline", "")
    date = item.get("date", "")
    # strip markdown links to plain text
    plain = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', headline)
    plain = re.sub(r'\*\*([^*]+)\*\*', r'\1', plain)
    return f"📣 {plain}\n{date}\n{HASHTAGS}"


def format_grant(item):
    title = item.get("title", "")
    funder = item.get("funder", "")
    pi = item.get("pi", "")
    amount = item.get("amount", "")
    parts = [f"🏆 New grant: {title}", f"Funder: {funder}"]
    if amount:
        parts.append(f"Amount: {amount}")
    if pi:
        parts.append(f"PI: {pi}")
    parts.append(HASHTAGS)
    return "\n".join(parts)


def format_paper(item):
    title = item.get("title", "")
    authors = item.get("authors", "")
    venue = item.get("book") or item.get("journal") or item.get("conference") or ""
    url = (item.get("link") or {}).get("url", "")
    parts = [f"📄 New paper: {title}"]
    if authors:
        parts.append(authors)
    if venue:
        parts.append(venue)
    if url:
        parts.append(url)
    parts.append(HASHTAGS)
    return "\n".join(parts)


# ── Platform Posters ─────────────────────────────────────────────────────────

def post_mastodon(text):
    instance = os.environ.get("MASTODON_INSTANCE_URL", "").rstrip("/")
    token = os.environ.get("MASTODON_ACCESS_TOKEN", "")
    if not (instance and token):
        print("[Mastodon] Skipped — secrets not configured.")
        return
    msg = truncate(text, 500)
    if DRY_RUN:
        print(f"[DRY RUN Mastodon]\n{msg}\n")
        return
    resp = requests.post(
        f"{instance}/api/v1/statuses",
        headers={"Authorization": f"Bearer {token}"},
        data={"status": msg, "visibility": "public"},
    )
    resp.raise_for_status()
    print(f"[Mastodon] Posted: {resp.json().get('url')}")


def post_bluesky(text):
    handle = os.environ.get("BLUESKY_HANDLE", "")
    password = os.environ.get("BLUESKY_APP_PASSWORD", "")
    if not (handle and password):
        print("[Bluesky] Skipped — secrets not configured.")
        return
    msg = truncate(text, 300)
    if DRY_RUN:
        print(f"[DRY RUN Bluesky]\n{msg}\n")
        return
    # Authenticate
    auth = requests.post(
        "https://bsky.social/xrpc/com.atproto.server.createSession",
        json={"identifier": handle, "password": password},
    )
    auth.raise_for_status()
    session = auth.json()
    # Post
    resp = requests.post(
        "https://bsky.social/xrpc/com.atproto.repo.createRecord",
        headers={"Authorization": f"Bearer {session['accessJwt']}"},
        json={
            "repo": session["did"],
            "collection": "app.bsky.feed.post",
            "record": {
                "$type": "app.bsky.feed.post",
                "text": msg,
                "createdAt": __import__("datetime").datetime.utcnow().isoformat() + "Z",
            },
        },
    )
    resp.raise_for_status()
    print(f"[Bluesky] Posted: {resp.json().get('uri')}")


def post_twitter(text):
    try:
        import tweepy
    except ImportError:
        print("[X/Twitter] tweepy not installed.")
        return
    api_key = os.environ.get("TWITTER_API_KEY", "")
    api_secret = os.environ.get("TWITTER_API_SECRET", "")
    access_token = os.environ.get("TWITTER_ACCESS_TOKEN", "")
    access_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET", "")
    if not all([api_key, api_secret, access_token, access_secret]):
        print("[X/Twitter] Skipped — secrets not configured.")
        return
    msg = truncate(text, 280)
    if DRY_RUN:
        print(f"[DRY RUN X/Twitter]\n{msg}\n")
        return
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_secret,
    )
    resp = client.create_tweet(text=msg)
    print(f"[X/Twitter] Posted tweet ID: {resp.data['id']}")


def post_linkedin(text):
    token = os.environ.get("LINKEDIN_ACCESS_TOKEN", "")
    person_urn = os.environ.get("LINKEDIN_PERSON_URN", "")
    if not (token and person_urn):
        print("[LinkedIn] Skipped — secrets not configured.")
        return
    msg = truncate(text, 3000)
    if DRY_RUN:
        print(f"[DRY RUN LinkedIn]\n{msg}\n")
        return
    resp = requests.post(
        "https://api.linkedin.com/v2/ugcPosts",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0",
        },
        json={
            "author": person_urn,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": msg},
                    "shareMediaCategory": "NONE",
                }
            },
            "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
        },
    )
    resp.raise_for_status()
    print(f"[LinkedIn] Posted.")


def post_all(text):
    post_mastodon(text)
    post_bluesky(text)
    post_twitter(text)
    post_linkedin(text)


# ── Main ─────────────────────────────────────────────────────────────────────

FILE_CONFIG = [
    ("_data/events.yml",  "events.yml",  "title",    format_event),
    ("_data/talks.yml",   "talks.yml",   "title",    format_talk),
    ("_data/news.yml",    "news.yml",    "headline", format_news),
    ("_data/grants.yml",  "grants.yml",  "title",    format_grant),
    ("_data/publist.yml", "publist.yml", "title",    format_paper),
]


def load_yaml(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, encoding="utf-8") as f:
        return yaml.safe_load(f) or []


if __name__ == "__main__":
    print(f"DRY_RUN={DRY_RUN}")
    posted = 0
    for git_path, data_file, key_field, formatter in FILE_CONFIG:
        diff = git_diff_added_blocks(git_path)
        if not diff.strip():
            continue
        all_entries = load_yaml(os.path.join("_data", data_file))
        new_entries = extract_new_entries(diff, all_entries, key_field)
        if not new_entries:
            print(f"[{data_file}] No new entries detected.")
            continue
        # Batch multiple new entries from the same file into one message
        # to stay within X free-tier limits
        if len(new_entries) == 1:
            msg = formatter(new_entries[0])
            print(f"[{data_file}] Posting 1 new entry.")
            post_all(msg)
            posted += 1
        else:
            # Post a summary when multiple entries were added at once
            titles = [e.get(key_field, "") for e in new_entries]
            summary = f"📣 {len(new_entries)} new items added to {data_file.replace('.yml','')}:\n"
            summary += "\n".join(f"• {t}" for t in titles[:5])
            summary += f"\n{SITE_URL}\n{HASHTAGS}"
            print(f"[{data_file}] Posting summary of {len(new_entries)} new entries.")
            post_all(truncate(summary, 280))
            posted += 1

    if posted == 0:
        print("No new data entries detected — nothing to post.")
