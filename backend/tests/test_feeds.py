import pytest
from patchpal.core.feeds import fetch_rss_feeds, parse_severity_from_description

class MockFeedEntry:
    def __init__(self, title, description, link, published):
        self.title = title
        self.description = description
        self.link = link
        self.published = published

class MockFeed:
    def __init__(self, entries, bozo=0):
        self.entries = entries
        self.bozo = bozo

def test_parse_severity():
    assert parse_severity_from_description("This is a CRITICAL issue with CVSS: 9.8") == "Critical"
    assert parse_severity_from_description("A high severity bug") == "High"
    assert parse_severity_from_description("Minor low issue") == "Low"
    assert parse_severity_from_description("No severity mentioned") == "Unknown"

def test_fetch_rss_feeds(mocker):
    # Mock feedparser.parse
    mock_entries = [
        MockFeedEntry(
            title="CVE-2026-9999: Remote Code Execution in React",
            description="A critical vulnerability (CVSS: 9.8) in React allows RCE.",
            link="https://example.com/cve",
            published="2026-10-04T12:00:00Z"
        )
    ]
    mock_feed = MockFeed(entries=mock_entries)
    mocker.patch('feedparser.parse', return_value=mock_feed)

    vulns = fetch_rss_feeds(["http://dummy.url"])
    
    assert len(vulns) == 1
    assert vulns[0].cve_id == "CVE-2026-9999"
    assert vulns[0].title == "CVE-2026-9999: Remote Code Execution in React"
    assert vulns[0].severity == "Critical"
    assert vulns[0].source_url == "https://example.com/cve"
