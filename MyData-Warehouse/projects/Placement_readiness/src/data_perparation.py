import pandas as pd
import numpy as np 

np.random.seed(42) 

def data_preparation(n_students):
    tenth_percentile = np.clip(np.random.normal(loc = 70,scale= 10, size = n_students),
                               45,95)
    twelth_percentile = np.clip(np.random.normal(loc = 68 , scale = 11 , size = n_students),
                               45,95)
    
    cgpa = (6.5 + 0.15* (twelth_percentile - 65) + 0.15 * (tenth_percentile - 65))+ np.random.normal(0,0.5 , n_students)
    cgpa = np.clip(cgpa , 5, 9.5)

    applied_work_count = np.clip(np.random.poisson(lam = 1.6 , size= n_students) , 0 , 8)

    internship_count = np.clip(np.random.poisson(lam = 0.6 , size= n_students) , 0 , 3) 

    aptitude_score = (2.5+1.2*(cgpa -6)+ np.random.normal(0,0.8 , n_students))
    aptitude_level = np.clip(np.round(aptitude_score) , 1 , 5)

    english_score = (internship_count + np.random.normal(1.8,1.0 , n_students))
    english_level = np.clip(np.round(english_score) , 1, 5)

    domain_score = (applied_work_count + np.random.normal(1.2,1.1 , n_students))
    domain_skill_level = np.clip(np.round(domain_score) , 1 , 5)

    df = pd.DataFrame({
        "10th_pct": tenth_percentile,
        "12th_pct": twelth_percentile,
        "cgpa": cgpa,
        "aptitude_level": aptitude_level,
        "domain_skill_level": domain_skill_level,
        "english_level": english_level,
        "applied_work_count": applied_work_count,
        "internships_count": internship_count
        })
    return df

