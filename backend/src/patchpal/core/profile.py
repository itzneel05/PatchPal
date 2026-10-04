import yaml
import os
from pathlib import Path
from pydantic import ValidationError
from patchpal.core.models import FriendProfile

def load_profile(filepath: str | Path) -> FriendProfile:
    """Loads a friend's tech stack profile from a YAML file."""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Profile not found: {path}")

    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    if not data:
        raise ValueError("Profile YAML is empty.")

    try:
        return FriendProfile(**data)
    except ValidationError as e:
        raise ValueError(f"Invalid profile format: {e}")

def create_example_profile(filepath: str | Path) -> None:
    """Creates an example friend profile at the given path."""
    example_data = {
        "name": "Jane",
        "tech_stack": ["React", "Next.js", "Python", "FastAPI", "PostgreSQL"],
        "severity_threshold": "medium"
    }
    
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(example_data, f, default_flow_style=False, sort_keys=False)
