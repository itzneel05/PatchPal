import pytest
from patchpal.core.summarizer import generate_friendly_summary, filter_relevant
from patchpal.core.models import FriendProfile, Vulnerability

def test_filter_relevant():
    vulns = [
        Vulnerability(
            title="Python critical flaw",
            severity="High",
            source_url="http://example.com/1",
            published="2026",
            raw_description="A flaw in Python standard library."
        ),
        Vulnerability(
            title="Random issue",
            severity="Low",
            source_url="http://example.com/2",
            published="2026",
            raw_description="Does not affect your stack."
        )
    ]
    tech_stack = ["Python", "React"]
    
    filtered = filter_relevant(vulns, tech_stack)
    
    assert len(filtered) == 1
    assert filtered[0].title == "Python critical flaw"
    assert "python" in filtered[0].affected_tech

def test_generate_summary_no_vulns():
    profile = FriendProfile(name="Aarav", tech_stack=["Python"])
    summary = generate_friendly_summary([], profile)
    
    assert "Aarav" in summary
    assert "No relevant threats" in summary

def test_generate_summary_with_ollama_fallback(mocker):
    profile = FriendProfile(name="Parth", tech_stack=["Python"])
    vulns = [
        Vulnerability(
            title="Python critical flaw",
            severity="High",
            source_url="http://example.com/1",
            published="2026",
            raw_description="A flaw in Python standard library."
        )
    ]
    
    # Mock Ollama throwing an exception
    mocker.patch('patchpal.core.summarizer.ollama.chat', side_effect=Exception("Ollama down"))
    
    summary = generate_friendly_summary(vulns, profile)
    
    assert "Parth" in summary
    assert "offline" in summary

def test_generate_summary_success(mocker):
    profile = FriendProfile(name="Diya", tech_stack=["Python"])
    vulns = [
        Vulnerability(
            title="Python critical flaw",
            severity="High",
            source_url="http://example.com/1",
            published="2026",
            raw_description="A flaw in Python standard library."
        )
    ]
    
    # Mock Ollama success
    mock_response = {
        'message': {
            'content': "Hey Diya! Be careful, there is a High severity issue in Python."
        }
    }
    mocker.patch('patchpal.core.summarizer.ollama.chat', return_value=mock_response)
    
    summary = generate_friendly_summary(vulns, profile)
    
    assert "Hey Diya" in summary
    assert "Python" in summary
