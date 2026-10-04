import pytest
from patchpal.core.search import search_threat_news

def test_search_threat_news_no_api_key(monkeypatch):
    # Ensure no API key in env
    monkeypatch.delenv("SERPAPI_API_KEY", raising=False)
    
    # Should gracefully return empty list
    vulns = search_threat_news(tech_stack=["Python"])
    assert vulns == []

def test_search_threat_news_empty_stack():
    vulns = search_threat_news(tech_stack=[], api_key="dummy")
    assert vulns == []

def test_search_threat_news_success(mocker):
    mock_results = {
        "news_results": [
            {
                "title": "New zero-day discovered in Python",
                "snippet": "Hackers are exploiting a new flaw in Python's standard library.",
                "link": "https://news.example.com/python-flaw",
                "date": "2 hours ago"
            }
        ]
    }
    
    # Mock the SerpApi GoogleSearch class
    mock_search_instance = mocker.MagicMock()
    mock_search_instance.get_dict.return_value = mock_results
    mocker.patch('patchpal.core.search.GoogleSearch', return_value=mock_search_instance)

    vulns = search_threat_news(tech_stack=["Python"], api_key="dummy_key")
    
    assert len(vulns) == 1
    assert vulns[0].title == "New zero-day discovered in Python"
    assert "Hackers" in vulns[0].raw_description
    assert vulns[0].severity == "Unknown" # Evaluated by AI later
