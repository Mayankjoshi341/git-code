# domain_score.py

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
    }
}


# ---------- helpers ----------
def _normalize_key(skill: str) -> str:
    return skill.lower().replace(" ", "_").replace("/", "_")


# ---------- public API ----------
def extract_user_ratings(domain: str, form_data: dict) -> dict:
    """
    Converts raw form input into {skill: rating}
    """
    skills = DOMAIN_SKILL_SCHEMA[domain]["skills"]
    ratings = {}

    for skill in skills:
        field = f"skill_{_normalize_key(skill)}"
        value = int(form_data.get(field, 0))

        if not 0 <= value <= 5:
            raise ValueError(f"Invalid rating for {skill}")

        ratings[skill] = value

    return ratings


def compute_domain_score(domain: str, user_ratings: dict) -> float:
    """
    Returns normalized domain score (0–1)
    """
    skills = DOMAIN_SKILL_SCHEMA[domain]["skills"]
    score = 0.0

    for skill, weight in skills.items():
        rating = user_ratings.get(skill, 0) / 5
        score += rating * weight

    return round(score, 3)


def compute_skill_gaps(domain: str,user_ratings: dict,threshold: float = 0.4) -> dict:
    """
    Returns missing skills sorted by severity
    """
    skills = DOMAIN_SKILL_SCHEMA[domain]["skills"]
    gaps = {}

    for skill, weight in skills.items():
        rating = user_ratings.get(skill, 0) / 5
        gap = weight * (1 - rating)

        if gap > threshold * weight:
            gaps[skill] = round(gap, 3)

    return dict(sorted(gaps.items(), key=lambda x: x[1], reverse=True))

form_data = {
    "skill_python": "3",
    "skill_statistics": "2",
    "skill_machine_learning": "1",
    "skill_sql": "2",
    "skill_communication": "4"
}

scores = extract_user_ratings("Data Scientist" , form_data)

print(compute_domain_score("Data Scientist" , scores))
print(compute_skill_gaps("Data Scientist" , scores))