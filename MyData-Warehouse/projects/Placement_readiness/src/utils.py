"""import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("MyData-Warehouse/projects/Placement_readiness/Data/processed/updated_cluster_profile.csv")

df.set_index('cluster', inplace=True)
df.plot(kind='bar', figsize=(10,6))
plt.title('Cluster Profiling')
plt.xlabel('Cluster')
plt.ylabel('Mean Feature Values')
plt.legend(title='Features', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

plt.scatter(df.index, df['readiness_score'])
plt.title('Readiness Score by Cluster')
plt.xlabel('Cluster')
plt.ylabel('Readiness Score')
plt.grid(True)
plt.show()  """

from generate_report import mail_generate

sample_recommendation = {
    "readiness_level": "Almost Ready",

    "strengths": {
        "cgpa": 0.42,
        "english_level": 0.35,
        "domain_skill_level": 0.28
    },

    "weaknesses": {
        "aptitude_level": -0.65,
        "applied_work_count": -0.40
    },

    "focus_areas": {
        "aptitude_level": -0.65,
        "applied_work_count": -0.40
    },

    "expected_salary_lpa": "3.0 - 4.5",

    "growth_trajectory": [
        "Graduate Trainee / Junior Role",
        "Mid-level Contributor (1–2 years)",
        "Specialized / Lead Track"
    ],

    "estimated_impact": {
        "aptitude_level": "High impact on shortlisting probability",
        "applied_work_count": "Medium impact, improves profile strength"
    }
}

mail_generate("mayankjoshi0341@gmail.com" , "mayank joshi" , sample_recommendation)