import pandas as pd

def gap_analysis(student_row : pd.Series , cluster_profile : pd.DataFrame , feature_cols :list):
    cluster_id = student_row['cluster']
    cluster_mean = cluster_profile.loc[cluster_id , feature_cols]

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

def generate_recommendation(student_row : pd.Series , cluster_profile : pd.DataFrame , feature_cols : list):
    gaps = gap_analysis(student_row, cluster_profile, feature_cols)

    strengths, weaknesses = categorize_gaps(gaps)
    focus = focus_priorities(weaknesses)

    salary_min, salary_max = salary_estimate_band(student_row)
    trajectory = growth_trajectory(student_row)
    impact = estimated_impact(focus.keys())

    return {
        "readiness_level": student_row["readiness_level"],
        "strengths": strengths.to_dict(),
        "weaknesses": weaknesses.to_dict(),
        "focus_areas": focus.to_dict(),
        "expected_salary_lpa": f"{salary_min} - {salary_max}",
        "growth_trajectory": trajectory,
        "estimated_impact": impact
    }  