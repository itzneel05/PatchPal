import json
from typing import List
import ollama
from patchpal.core.models import Vulnerability, FriendProfile

# We'll use the 2b parameter model as our default for local inference
MODEL_NAME = "gemma2:2b"

def generate_friendly_summary(vulns: List[Vulnerability], profile: FriendProfile) -> str:
    """Uses Gemma to write a plain-language summary addressing the friend."""
    if not vulns:
        return f"Hey {profile.name}! No relevant threats found for your tech stack today. You're all good!"

    vuln_details = ""
    for idx, v in enumerate(vulns, 1):
        vuln_details += f"{idx}. {v.title} ({v.severity})\n"
        
    system_prompt = (
        "You are PatchPal, a friendly and defensive cybersecurity assistant. "
        "Your job is to summarize security vulnerabilities for a developer friend. "
        "Keep the tone friendly, helpful, and concise. "
        "Explain the risk defensively. Do NOT generate or suggest exploit code under any circumstances."
    )
    
    user_prompt = (
        f"Write a short, friendly message to {profile.name} summarizing these threats "
        f"that impact their stack ({', '.join(profile.tech_stack)}). Tell them what they need to watch out for:\n\n{vuln_details}"
    )

    try:
        response = ollama.chat(model=MODEL_NAME, messages=[
            {
                'role': 'system',
                'content': system_prompt
            },
            {
                'role': 'user',
                'content': user_prompt
            }
        ])
        return response['message']['content'].strip()
    except Exception as e:
        # Graceful degradation if Ollama is down or model missing
        print(f"Ollama AI generation failed: {e}")
        fallback_summary = f"Hey {profile.name}! I found {len(vulns)} issues relevant to your stack. (AI summarization is currently offline)."
        return fallback_summary

def filter_relevant(vulns: List[Vulnerability], tech_stack: List[str]) -> List[Vulnerability]:
    """
    Very basic filter to reduce noise before sending to AI,
    or we can use AI to do the filtering. 
    For speed and cost, we do a keyword filter first.
    """
    if not tech_stack or not vulns:
        return []
        
    stack_lower = [t.lower() for t in tech_stack]
    relevant_vulns = []
    
    for v in vulns:
        title_lower = v.title.lower()
        desc_lower = v.raw_description.lower()
        
        # Check if any tech in stack is mentioned in title or description
        affected = []
        for tech in stack_lower:
            if tech in title_lower or tech in desc_lower:
                affected.append(tech)
                
        if affected:
            v.affected_tech = list(set(affected))
            relevant_vulns.append(v)
            
    return relevant_vulns
