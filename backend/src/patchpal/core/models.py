from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

class FriendProfile(BaseModel):
    name: str
    tech_stack: List[str]
    severity_threshold: str = "medium"

class Vulnerability(BaseModel):
    cve_id: Optional[str] = None
    title: str
    severity: str
    affected_tech: List[str] = Field(default_factory=list)
    source_url: str
    published: str
    raw_description: str

class Digest(BaseModel):
    friend_name: str
    date_generated: date
    vulnerabilities: List[Vulnerability] = Field(default_factory=list)
    ai_summary: str
