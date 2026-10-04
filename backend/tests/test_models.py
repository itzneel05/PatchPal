from patchpal.core.models import FriendProfile, Vulnerability, Digest
from datetime import date

def test_friend_profile_creation():
    profile = FriendProfile(name="Alice", tech_stack=["Python", "React"])
    assert profile.name == "Alice"
    assert profile.severity_threshold == "medium"
    assert "Python" in profile.tech_stack

def test_vulnerability_creation():
    vuln = Vulnerability(
        cve_id="CVE-2026-1234",
        title="Test Vulnerability",
        severity="High",
        affected_tech=["Python"],
        source_url="https://example.com/cve-2026-1234",
        published="2026-10-04T12:00:00Z",
        raw_description="A critical test vulnerability."
    )
    assert vuln.title == "Test Vulnerability"
    assert vuln.cve_id == "CVE-2026-1234"
    assert "Python" in vuln.affected_tech

def test_digest_creation():
    digest = Digest(
        friend_name="Alice",
        date_generated=date.today(),
        ai_summary="All good today, nothing critical in your stack."
    )
    assert digest.friend_name == "Alice"
    assert digest.vulnerabilities == []
    assert "All good" in digest.ai_summary
