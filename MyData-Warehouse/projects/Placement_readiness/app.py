from flask import Flask, render_template, request
import pandas as pd
from joblib import load
import os

# Import your modules
from src.preprocessing import transform_with_scaler
from src.recommendation import generate_recommendation
from src.generate_report import mail_generate

app = Flask(__name__ ,  template_folder="templates")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

scaler = load(os.path.join(BASE_DIR, "models", "scaler.pkl"))
kmeans = load(os.path.join(BASE_DIR, "models", "kmeans_model.pkl"))

FEATURE_COLS = [
    "cgpa",
    "aptitude_level",
    "domain_skill_level",
    "english_level",
    "applied_work_count",
    "internships_count"
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate-report", methods=["POST"])
def generate_report():
    # Read form data
    student_name = request.form["name"]
    email = request.form["email"]

    user_data = {
        "cgpa": float(request.form["cgpa"]),
        "aptitude_level": int(request.form["aptitude"]),
        "domain_skill_level": int(request.form["domain_skill"]),
        "english_level": int(request.form["english"]),
        "applied_work_count": int(request.form["applied_work"]),
        "internships_count": int(request.form["internships"])
    }

    # Convert to DataFrame
    user_df = pd.DataFrame([user_data])

    # Scale input
    user_scaled = transform_with_scaler(user_df, scaler)

    # Predict cluster
    cluster = kmeans.predict(user_scaled)[0]
    user_df["cluster"] = cluster

    # Readiness mapping
    cluster_profiles = load(os.path.join(BASE_DIR, "models", "cluster_profile.pkl"))
    readiness_map = load(os.path.join(BASE_DIR, "models", "readiness_map.pkl"))

    user_df["readiness_level"] = user_df["cluster"].map(readiness_map)

    # Generate recommendation

    recommendation = generate_recommendation(
        student_row=user_df.iloc[0],
        cluster_profile=cluster_profiles,
        feature_cols=FEATURE_COLS
    )

    # Send email
    try:
        mail_generate(email, student_name, recommendation)
    except Exception as e:
        print("EMAIL ERROR:", e)


    return render_template("result.html",name=student_name,recommendation=recommendation)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

