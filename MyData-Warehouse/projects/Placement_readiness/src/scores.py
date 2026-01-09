import pandas as pd
from flask import request
DOMAIN_SKILL_SCHEMA = {
    "Software Engineer (Backend)": {
        "tier": "high",
        "skills": {
            "Programming Fundamentals": 0.25,
            "Data Structures & Algorithms": 0.25,
            "Databases / SQL": 0.15,
            "Backend Frameworks": 0.20,
            "Communication": 0.15
        }
    },

    "Data Scientist": {
        "tier": "high",
        "skills": {
            "Python": 0.25,
            "Statistics": 0.20,
            "Machine Learning": 0.25,
            "SQL": 0.15,
            "Communication": 0.15
        }
    },

    "Frontend Developer": {
        "tier": "mid",
        "skills": {
            "HTML/CSS": 0.20,
            "JavaScript": 0.25,
            "Frontend Frameworks": 0.25,
            "UI/UX Understanding": 0.15,
            "Communication": 0.15
        }
    },

    "Business Analyst": {
        "tier": "mid",
        "skills": {
            "Excel / Spreadsheets": 0.25,
            "SQL": 0.20,
            "Business Understanding": 0.25,
            "Data Visualization": 0.15,
            "Communication": 0.15
        }
    },

    "Sales / Marketing": {
        "tier": "low",
        "skills": {
            "Communication": 0.30,
            "Negotiation": 0.20,
            "Market Understanding": 0.20,
            "CRM Tools": 0.15,
            "Analytical Thinking": 0.15
        }
    }
}
def user_rating(domain):
    domain = request.form["domain"]
    domain_skills = DOMAIN_SKILL_SCHEMA[domain]["skills"].keys()
    
    user_skill_ratings = {}
    
    for skill in domain_skills:
        field_name = f"skill_{skill}"
        rating = int(request.form[field_name])

        if not (1 <= rating <= 5):
            raise ValueError(f"Invalid rating for {skill}")

        user_skill_ratings[skill] = rating

    return user_skill_ratings

def compute_domain_skill_score(domain: str, user_ratings : dict, domain_schema: dict) -> float:
    skills = domain_schema[domain]["skills"]

    score = 0.0
    for skill, weight in skills.items():
        rating = user_ratings.get(skill, 0)
        normalized = rating / 5
        score += normalized * weight
        print(score)

    return round(score, 3)




