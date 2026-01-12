from datetime import datetime

def context_bias(degree, graduation_year, college_tier):
    bias = 0.0
    year_gap = datetime.now().year - int(graduation_year)

    if degree not in ["BTech CS", "BTech IT", "BSc CS"]:
        bias -= 0.3
    if year_gap > 3:
        bias -=0.3
    if college_tier == 1:
        bias += 0.2
    elif college_tier == 3:
        bias -=0.2

    return bias