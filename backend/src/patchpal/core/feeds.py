import feedparser
from typing import List
from patchpal.core.models import Vulnerability

# Standard security feed (using cvefeed.io or similar as fallback/example)
DEFAULT_RSS_FEEDS = [
    "https://cvefeed.io/rssfeed/latest.xml"
]

def parse_severity_from_description(description: str) -> str:
    """Extract a rough severity from the text, defaulting to Unknown."""
    desc_lower = description.lower()
    if "critical" in desc_lower or "cvss: 9" in desc_lower or "cvss: 10" in desc_lower:
        return "Critical"
    elif "high" in desc_lower or "cvss: 7" in desc_lower or "cvss: 8" in desc_lower:
        return "High"
    elif "medium" in desc_lower or "cvss: 4" in desc_lower or "cvss: 5" in desc_lower or "cvss: 6" in desc_lower:
        return "Medium"
    elif "low" in desc_lower:
        return "Low"
    return "Unknown"

def fetch_rss_feeds(urls: List[str] = None) -> List[Vulnerability]:
    """Fetches security RSS feeds and parses them into Vulnerability models."""
    if urls is None:
        urls = DEFAULT_RSS_FEEDS

    vulnerabilities = []

    for url in urls:
        # feedparser handles network requests directly
        feed = feedparser.parse(url)
        
        # If feed fetching failed, feedparser sets 'bozo_exception' or 'status'
        if feed.bozo and getattr(feed.bozo_exception, 'code', None) != 200:
            continue # Skip failed feeds silently to gracefully degrade

        for entry in feed.entries[:20]: # Limit to latest 20 per feed
            cve_id = None
            if "cve" in entry.title.lower():
                # Extract first word that looks like CVE-XXXX-XXXXX
                words = entry.title.split()
                cve_words = [w for w in words if w.upper().startswith("CVE-")]
                if cve_words:
                    cve_id = cve_words[0].strip(":,.-")

            description = entry.description if hasattr(entry, 'description') else ""
            severity = parse_severity_from_description(description)

            vuln = Vulnerability(
                cve_id=cve_id,
                title=entry.title,
                severity=severity,
                source_url=entry.link,
                published=entry.published if hasattr(entry, 'published') else "Unknown",
                raw_description=description
            )
            vulnerabilities.append(vuln)

    return vulnerabilities
