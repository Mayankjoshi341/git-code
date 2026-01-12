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
