import pytest
import tempfile
import os
from pathlib import Path
from patchpal.core.profile import load_profile, create_example_profile
from patchpal.core.models import FriendProfile

def test_load_valid_profile(tmp_path):
    # Create a temporary YAML file
    yaml_content = """
    name: Aarav
    tech_stack:
      - Go
      - Docker
      - Kubernetes
    severity_threshold: high
    """
    filepath = tmp_path / "aarav.yaml"
    filepath.write_text(yaml_content)

    profile = load_profile(filepath)
    assert profile.name == "Aarav"
    assert profile.severity_threshold == "high"
    assert "Docker" in profile.tech_stack
    assert len(profile.tech_stack) == 3

def test_load_missing_profile():
    with pytest.raises(FileNotFoundError):
        load_profile("nonexistent_file.yaml")

def test_load_invalid_profile(tmp_path):
    yaml_content = """
    # Missing name
    tech_stack:
      - Go
    """
    filepath = tmp_path / "invalid.yaml"
    filepath.write_text(yaml_content)

    with pytest.raises(ValueError, match="Invalid profile format"):
        load_profile(filepath)

def test_create_example_profile(tmp_path):
    filepath = tmp_path / "example.yaml"
    create_example_profile(filepath)
    
    assert filepath.exists()
    
    # Verify it can be loaded
    profile = load_profile(filepath)
    assert profile.name == "Parth"
    assert "FastAPI" in profile.tech_stack
