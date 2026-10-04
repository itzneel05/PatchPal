from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import date

from patchpal.core.models import FriendProfile, Digest, Vulnerability
from patchpal.core.profile import load_profile
from patchpal.core.feeds import fetch_rss_feeds
from patchpal.core.search import search_threat_news
from patchpal.core.summarizer import filter_relevant, generate_friendly_summary

router = APIRouter()

# For a real app, this path would be injected or configured
DEFAULT_PROFILE_PATH = "profiles/friend.yaml"

@router.get("/profile", response_model=FriendProfile)
def get_profile():
    try:
        return load_profile(DEFAULT_PROFILE_PATH)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Profile not found. Please create profiles/friend.yaml")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/digest", response_model=Digest)
def get_digest():
    try:
        profile = load_profile(DEFAULT_PROFILE_PATH)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Could not load profile: {str(e)}")

    # Fetch raw data
    rss_vulns = fetch_rss_feeds()
    search_vulns = search_threat_news(profile.tech_stack)
    
    # Combine and filter
    all_vulns = rss_vulns + search_vulns
    relevant_vulns = filter_relevant(all_vulns, profile.tech_stack)
    
    # Summarize via AI
    ai_summary = generate_friendly_summary(relevant_vulns, profile)
    
    # Build digest
    digest = Digest(
        friend_name=profile.name,
        date_generated=date.today(),
        vulnerabilities=relevant_vulns,
        ai_summary=ai_summary
    )
    
    return digest
