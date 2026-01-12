print(">>> domain_score.py START importing")
def user_rating(domain : str,form_data: dict):
    from schema.schemas import DOMAIN_SKILL_SCHEMA
    domain_skills = DOMAIN_SKILL_SCHEMA[domain]["skills"].keys()
    
    user_skill_ratings = {}
    
    for skill in domain_skills:
        field_name = f"skill_{skill}"
        rating = int(form_data[field_name])

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

def missing_skills(domain : str, user_ratings : dict, schema :dict, threshold=0.4):

    skills = schema[domain]["skills"]
    gaps = {}

    for skill, weight in skills.items():
        rating = user_ratings.get(skill, 0) / 5
        gap = weight * (1 - rating)
        if gap > threshold * weight:
            gaps[skill] = round(gap, 3)

    return dict(sorted(gaps.items(), key=lambda x: x[1], reverse=True))


print(">>> domain_score.py END importing")
print(">>> available names:", list(globals().keys()))
