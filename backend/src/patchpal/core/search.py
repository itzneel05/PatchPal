import os
from typing import List
from serpapi import GoogleSearch
from patchpal.core.models import Vulnerability

def search_threat_news(tech_stack: List[str], api_key: str | None = None) -> List[Vulnerability]:
    """Searches SerpApi for recent vulnerabilities related to the tech stack."""
    
    if not api_key:
        api_key = os.environ.get("SERPAPI_API_KEY")
    
    # Graceful degradation if no API key
    if not api_key:
        return []

    if not tech_stack:
        return []

    # Build a combined search query
    tech_query = " OR ".join(f'"{tech}"' for tech in tech_stack)
    query = f"({tech_query}) (vulnerability OR exploit OR CVE OR zero-day) when:1d"

    params = {
        "engine": "google_news",
        "q": query,
        "api_key": api_key,
        "gl": "us",
        "hl": "en"
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
    except Exception:
        # Graceful degradation on network or API failure
        return []

    news_results = results.get("news_results", [])
    vulnerabilities = []

    for item in news_results[:10]: # Limit to top 10 news items
        vuln = Vulnerability(
            cve_id=None,
            title=item.get("title", "Unknown Threat News"),
            severity="Unknown", # News articles rarely have explicit severity labels, Gemma will refine
            source_url=item.get("link", ""),
            published=item.get("date", "Recent"),
            raw_description=item.get("snippet", "")
        )
        vulnerabilities.append(vuln)

    return vulnerabilities
