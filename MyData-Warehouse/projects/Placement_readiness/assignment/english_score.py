def english_analysis(text):
    words = len(text.split())

    if words < 40:
        return {
            "level": "Low",
            "issue": "Short responses, low clarity",
            "suggestion": "Practice structured answers"
        }
    elif words < 100:
        return {
            "level": "Medium",
            "issue": "Decent clarity, limited depth",
            "suggestion": "Expand examples and vocabulary"
        }
    else:
        return {
            "level": "High",
            "issue": "Minor improvements needed",
            "suggestion": "Polish grammar and flow"
        }
