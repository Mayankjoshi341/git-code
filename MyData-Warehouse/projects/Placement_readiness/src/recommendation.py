"""import pandas as pd
import numpy as np
from assignment.aptitude_score import aptitude_insights
from assignment.english_score import english_analysis
from schema.schemas import DOMAIN_SKILL_SCHEMA

def gap_analysis(student_row : pd.Series , cluster_profile : pd.DataFrame , feature_cols :list):
    cluster_id = student_row['cluster']
    cluster_mean = cluster_profile.loc[cluster_id , feature_cols][0]

    gaps= student_row[feature_cols] - cluster_mean
    return gaps

def categorize_gaps(gaps :pd.Series):
    strengths = gaps[gaps > 0.3].sort_values(ascending= False)
    weaknesses = gaps[gaps < -0.3].sort_values()

    return strengths, weaknesses

def focus_priorities(weaknesses : pd.Series, top_n = 2):
    return weaknesses.head(top_n)

def salary_estimate_band(student_row:pd.Series):
    readiness_level = student_row['readiness_level']

    if readiness_level == "Not Ready":
        base_min , base_max = 1.0 , 2.5
    elif readiness_level == "Almost Ready":
        base_min , base_max = 2.5 , 4.0
    else:
        base_min , base_max = 4.0 , 5.5

    bonus = 0.0

    if student_row["internships_count"] >= 1:
        bonus += 0.5
    if student_row["applied_work_count"] >= 3:
        bonus += 0.5
    if student_row["domain_skill_level"] >= 4:
        bonus += 0.5
    
    return round(base_min + bonus , 1) , round(base_max + bonus , 1)


def growth_trajectory(student_row: pd.Series):
    readiness_level = student_row["readiness_level"]

    if readiness_level == "Not Ready":
        return ["Skill Foundation Phase (0-8 months)",
                "Intern / trainee Roles",
                "Junior Role (1-2 years)"]
    elif readiness_level == "Almost Ready":
        return [
            "Junior Role / Graduate Trainee",
            "Mid-level Role (1-2 years)",
            "Specialist / Lead Track"]     
    else:  # Ready
        return [
            "Direct Entry-Level Role",
            "Strong Mid-level Role (1-2 years)",
            "Advanced / Specialized Track"]
    

def estimated_impact(focus_areas):
    impact = {}
    for area in focus_areas:
        if area in ["aptitude_level", "domain_skill_level"]:
            impact[area] = "High impact on shortlisting probability"
        elif area in ["applied_work_count", "internships_count"]:
            impact[area] = "Medium impact, improves profile strength"
        else:
            impact[area] = "Supportive improvement"

    return impact

def compute_readiness_percentage(student_vec , center_centorid , max_distance):
    distanace = np.linalg.norm(student_vec - center_centorid)
    readiness_score = 1- (distanace/max_distance)

    return round(max(0,min(readiness_score , 1))*100 , 1)

def skills_improtance(domain ,schema):
    return schema[domain]["skills"]

def job_probability_impact(current_distance , improved_distance):
    impact = (current_distance - improved_distance) / current_distance
    return round(max(0 , impact)*100 , 1)

def estimated_time(readiness_score):
    if readiness_score < 40:
        return "6-9 months"
    elif readiness_score < 70:
        return "4-6 months"
    else:
        return "1-3 months"

def ai_proof_score(aptitude, english , domain_skill):
    ai_weights = {
        "aptitude" : 0.3,
        "english" :0.3,
        "domain_skill" : 0.4
    }
    score = (aptitude * ai_weights["aptitude"] + english * ai_weights["english"] + domain_skill * ai_weights["domain_skill"])
    return round((score /5)*100 , 1)

def peer_benchmark(student_row , cluster_profile , feature_cols):

    cluster = student_row["cluster"]
    peer_avg = cluster_profile.loc[cluster , feature_cols]

    comparison = {}
    for f in feature_cols:
        if student_row[f] > peer_avg[f]:
            comparison[f] = "above average"
        elif student_row[f] < peer_avg[f]:
            comparison[f] = "Below average"
        else:
            comparison[f] = "Average"
    return comparison

def compute_aptitude_score(form):
    answers = [int(v) for k, v in form.items() if k.startswith("apt_")]
    score = sum(answers) / (len(answers) * 2)
    return round(score * 5, 2)

def aptitude_insights(score):
    if score < 2.5:
        return "Needs improvement in logical reasoning and speed"
    elif score < 4:
        return "Average reasoning, improve time-bound practice"
    else:
        return "Strong logical aptitude"


def generate_recommendation(student_row : pd.Series , cluster_profile : pd.DataFrame , feature_cols : list,
                            student_vec , ready_centroid , max_distance , domain : str , english_text :str):
    gaps = gap_analysis(student_row, cluster_profile, feature_cols)

    strengths, weaknesses = categorize_gaps(gaps)
    focus = focus_priorities(weaknesses)

    readiness_score = compute_readiness_percentage(student_vec , ready_centroid , max_distance)
    salary_min, salary_max = salary_estimate_band(student_row)
    trajectory = growth_trajectory(student_row)
    impact = estimated_impact(focus.keys())
    #user_rate = user_rating(domain ,form_d)

    return {
        "readiness_level": student_row["readiness_level"],
        "readiness_percentage" : readiness_score,
        "strengths": strengths.to_dict(),
        "weaknesses": weaknesses.to_dict(),
        "focus_areas": focus.to_dict(),
        #"missing_skills" : missing_skills(domain , user_rate, DOMAIN_SKILL_SCHEMA),
        "skill_importance" : skills_improtance(domain , DOMAIN_SKILL_SCHEMA),
        "time_to_job" : estimated_time(readiness_score),
        "ai_proof_score" : ai_proof_score(student_row["aptitude_level"] , student_row["english_level"] , student_row["domian_skill_score"]),
        "aptitude_insight" : aptitude_insights(student_row["aptitude_level"]),
        "english_analysis" : english_analysis(english_text),
        "peer_benchmark" : peer_benchmark(student_row , cluster_profile , feature_cols),
        "expected_salary_lpa": f"{salary_min} - {salary_max}",
        "growth_trajectory": trajectory,
        "estimated_impact": impact
    }  





FEATURE_COLS = [
    "cgpa",
    "aptitude_level",
    "domain_skill_level",
    "english_level",
    "applied_work_count",
    "internships_count"
]

def test_generate_recommendation():
    # -----------------------------
    # Dummy input data
    # -----------------------------
    student_row = pd.Series({
        "cgpa": 7.6,
        "aptitude_level": 2,
        "domain_skill_level": 3,
        "english_level": 4,
        "applied_work_count": 1,
        "internships_count": 0,
        "cluster": 1,
        "readiness_level": "Almost Ready",
        "domain_skill_score": 3
    })

    cluster_profile = pd.DataFrame({
        "cgpa": [6.2, 7.4, 8.1],
        "aptitude_level": [2.5, 3.2, 4.1],
        "domain_skill_level": [2.8, 3.5, 4.3],
        "english_level": [2.9, 3.6, 4.2],
        "applied_work_count": [0.8, 2.5, 4.0],
        "internships_count": [0.3, 1.2, 2.1]
    }, index=[0, 1, 2])

    FEATURE_COLS = [
        "cgpa",
        "aptitude_level",
        "domain_skill_level",
        "english_level",
        "applied_work_count",
        "internships_count"
    ]

    student_vector = np.array([7.6, 2, 3, 4, 1, 0])
    ready_centroid = np.array([8.1, 4.1, 4.3, 4.2, 4.0, 2.1])
    max_distance = np.linalg.norm(
        np.array([5.5, 1, 1, 1, 0, 0]) - ready_centroid
    )

    domain = "Software Engineer (Backend)"
    english_text = (
        "I am interested in backend development. "
        "I have worked on small APIs using Flask. "
        "I want to improve my communication and system design."
    )

    # -----------------------------
    # Fake form data (NO Flask)
    # -----------------------------
    form_data = {
        "skill_python": "3",
        "skill_sql": "2",
        "skill_dsa": "2",
        "skill_system_design": "1"
    }

    # -----------------------------
    # Call recommendation engine
    # -----------------------------
    result = generate_recommendation(
        student_row,
        cluster_profile,
        FEATURE_COLS,
        student_vector,
        ready_centroid,
        max_distance,
        domain,
        english_text
    )

    # -----------------------------
    # Output
    # -----------------------------
    print("\n===== RECOMMENDATION OUTPUT =====\n")
    for k, v in result.items():
        print(f"{k}: {v}")
"""
import pandas as pd
import numpy as np

# ======================================================
# Core analysis helpers
# ======================================================

def gap_analysis(student_row: pd.Series, cluster_profile: pd.DataFrame, feature_cols: list):
    cluster_id = student_row["cluster"]
    cluster_mean = cluster_profile.loc[cluster_id, feature_cols][0]
    return student_row[feature_cols] - cluster_mean


def categorize_gaps(gaps: pd.Series):
    strengths = gaps[gaps > 0.3].sort_values(ascending=False)
    weaknesses = gaps[gaps < -0.3].sort_values()
    return strengths, weaknesses


def focus_priorities(weaknesses: pd.Series, top_n=2):
    return weaknesses.head(top_n)


# ======================================================
# Career & readiness logic
# ======================================================

def salary_estimate_band(student_row: pd.Series):
    level = student_row["readiness_level"]

    if level == "Not Ready":
        base_min, base_max = 1.0, 2.5
    elif level == "Almost Ready":
        base_min, base_max = 2.5, 4.0
    else:
        base_min, base_max = 4.0, 5.5

    bonus = 0.0
    if student_row["internships_count"] >= 1:
        bonus += 0.5
    if student_row["applied_work_count"] >= 3:
        bonus += 0.5
    if student_row["domain_skill_level"] >= 4:
        bonus += 0.5

    return round(base_min + bonus, 1), round(base_max + bonus, 1)


def growth_trajectory(student_row: pd.Series):
    level = student_row["readiness_level"]

    if level == "Not Ready":
        return [
            "Skill Foundation Phase (0–8 months)",
            "Intern / Trainee Roles",
            "Junior Role (1–2 years)",
        ]
    elif level == "Almost Ready":
        return [
            "Junior / Graduate Trainee",
            "Mid-level Role (1–2 years)",
            "Specialist / Lead Track",
        ]
    else:
        return [
            "Direct Entry-Level Role",
            "Strong Mid-level Role (1–2 years)",
            "Advanced / Specialized Track",
        ]


def compute_readiness_percentage(student_vec, centroid, max_distance):
    dist = np.linalg.norm(student_vec - centroid)
    score = 1 - (dist / max_distance)
    return round(max(0, min(score, 1)) * 100, 1)


def estimated_time(readiness_score):
    if readiness_score < 40:
        return "6–9 months"
    elif readiness_score < 70:
        return "4–6 months"
    return "1–3 months"


def estimated_impact(focus_areas):
    impact = {}
    for area in focus_areas:
        if area in ["aptitude_level", "domain_skill_level"]:
            impact[area] = "High impact on shortlisting"
        elif area in ["internships_count", "applied_work_count"]:
            impact[area] = "Medium impact on profile"
        else:
            impact[area] = "Supportive improvement"
    return impact


def ai_proof_score(aptitude, english, domain_skill):
    weights = {"aptitude": 0.3, "english": 0.3, "domain": 0.4}
    score = (
        aptitude * weights["aptitude"]
        + english * weights["english"]
        + domain_skill * weights["domain"]
    )
    return round((score / 5) * 100, 1)


def peer_benchmark(student_row, cluster_profile, feature_cols):
    cluster = student_row["cluster"]
    peer_avg = cluster_profile.loc[cluster, feature_cols]

    comparison = {}
    for f in feature_cols:
        if student_row[f] > peer_avg[f]:
            comparison[f] = "Above average"
        elif student_row[f] < peer_avg[f]:
            comparison[f] = "Below average"
        else:
            comparison[f] = "Average"
    return comparison


# ======================================================
# English & aptitude analysis (mock logic)
# ======================================================

def aptitude_insights(score):
    if score < 2.5:
        return "Needs improvement in logical reasoning"
    elif score < 4:
        return "Average aptitude, practice timed questions"
    return "Strong aptitude"


def english_analysis(text: str):
    word_count = len(text.split())
    if word_count < 20:
        return "Very brief response, expand thoughts"
    elif word_count < 40:
        return "Decent communication, improve structure"
    return "Good clarity and expression"


# ======================================================
# Recommendation engine
# ======================================================

def generate_recommendation(
    student_row,
    cluster_profile,
    feature_cols,
    student_vec,
    ready_centroid,
    max_distance,
    domain,
    english_text,
):
    gaps = gap_analysis(student_row, cluster_profile, feature_cols)
    strengths, weaknesses = categorize_gaps(gaps)
    focus = focus_priorities(weaknesses)

    readiness_score = compute_readiness_percentage(
        student_vec, ready_centroid, max_distance
    )

    salary_min, salary_max = salary_estimate_band(student_row)

    return {
        "readiness_level": student_row["readiness_level"],
        "readiness_percentage": readiness_score,
        "strengths": strengths.to_dict(),
        "weaknesses": weaknesses.to_dict(),
        "focus_areas": focus.to_dict(),
        "time_to_job": estimated_time(readiness_score),
        "ai_proof_score": ai_proof_score(
            student_row["aptitude_level"],
            student_row["english_level"],
            student_row["domain_skill_level"],
        ),
        "aptitude_insight": aptitude_insights(student_row["aptitude_level"]),
        "english_analysis": english_analysis(english_text),
        "peer_benchmark": peer_benchmark(
            student_row, cluster_profile, feature_cols
        ),
        "expected_salary_lpa": f"{salary_min} – {salary_max}",
        "growth_trajectory": growth_trajectory(student_row),
        "estimated_impact": estimated_impact(focus.keys()),
    }


# ======================================================
# TEST RUN (AUTO EXECUTES)
# ======================================================

if __name__ == "__main__":
    FEATURE_COLS = [
        "cgpa",
        "aptitude_level",
        "domain_skill_level",
        "english_level",
        "applied_work_count",
        "internships_count",
    ]

    student_row = pd.Series(
        {
            "cgpa": 7.6,
            "aptitude_level": 2,
            "domain_skill_level": 3,
            "english_level": 4,
            "applied_work_count": 1,
            "internships_count": 0,
            "cluster": 1,
            "readiness_level": "Almost Ready",
        }
    )

    cluster_profile = pd.DataFrame(
        {
            "cgpa": [6.2, 7.4, 8.1],
            "aptitude_level": [2.5, 3.2, 4.1],
            "domain_skill_level": [2.8, 3.5, 4.3],
            "english_level": [2.9, 3.6, 4.2],
            "applied_work_count": [0.8, 2.5, 4.0],
            "internships_count": [0.3, 1.2, 2.1],
        },
        index=[0, 1, 2],
    )

    student_vector = np.array([7.6, 2, 3, 4, 1, 0])
    ready_centroid = np.array([8.1, 4.1, 4.3, 4.2, 4.0, 2.1])
    max_distance = np.linalg.norm(
        np.array([5.5, 1, 1, 1, 0, 0]) - ready_centroid
    )

    domain = "Software Engineer (Backend)"
    english_text = (
        "I am interested in backend development. "
        "I have worked on small APIs using Flask. "
        "I want to improve my communication and system design."
    )

    result = generate_recommendation(
        student_row,
        cluster_profile,
        FEATURE_COLS,
        student_vector,
        ready_centroid,
        max_distance,
        domain,
        english_text,
    )

    print("\n===== RECOMMENDATION OUTPUT =====\n")
    for k, v in result.items():
        print(f"{k}: {v}")
