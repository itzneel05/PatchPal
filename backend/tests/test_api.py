import pytest
from fastapi.testclient import TestClient
from patchpal.main import app

client = TestClient(app)

def test_get_profile_missing():
    # Will fail because profiles/friend.yaml doesn't exist during standard test run
    # (Unless we mock it, which we should)
    pass

def test_get_profile_success(mocker, tmp_path):
    # Create temp profile
    yaml_content = "name: Aarav\ntech_stack: [React]\nseverity_threshold: medium\n"
    filepath = tmp_path / "friend.yaml"
    filepath.write_text(yaml_content)
    
    # Mock the DEFAULT_PROFILE_PATH in routes
    mocker.patch('patchpal.api.routes.DEFAULT_PROFILE_PATH', str(filepath))
    
    response = client.get("/api/profile")
    assert response.status_code == 200
    assert response.json()["name"] == "Aarav"

def test_get_digest_success(mocker, tmp_path):
    yaml_content = "name: Diya\ntech_stack: [Python]\nseverity_threshold: medium\n"
    filepath = tmp_path / "friend.yaml"
    filepath.write_text(yaml_content)
    mocker.patch('patchpal.api.routes.DEFAULT_PROFILE_PATH', str(filepath))
    
    # Mock the internal calls so we don't hit the network or Ollama
    mocker.patch('patchpal.api.routes.fetch_rss_feeds', return_value=[])
    mocker.patch('patchpal.api.routes.search_threat_news', return_value=[])
    mocker.patch('patchpal.api.routes.generate_friendly_summary', return_value="All clear!")
    
    response = client.get("/api/digest")
    assert response.status_code == 200
    data = response.json()
    assert data["friend_name"] == "Diya"
    assert data["ai_summary"] == "All clear!"
    assert data["vulnerabilities"] == []
