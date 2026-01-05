🎓 Placement Readiness Recommendation System

A machine-learning powered web application that evaluates a student’s placement readiness by comparing them with peer groups and provides actionable, personalized recommendations instead of generic labels.

🚀 Live Demo

(Add your Railway / Render link here once deployment finishes)

🧠 Problem Statement

Most placement tools:

Only label students as placed / not placed

Do not explain why

Do not tell students what to improve next

This project solves that gap by:

Clustering students based on readiness

Comparing a student with peer averages

Highlighting strengths, gaps, and focus areas

Providing career trajectory and salary estimation

🧩 Solution Overview

The system:

Takes academic, skill, and experience inputs from a student

Scales features and assigns the student to a peer cluster

Compares the student against the cluster profile

Generates a human-readable recommendation report

⚙️ Tech Stack

Backend: Python, Flask

ML: Scikit-learn (KMeans clustering)

Data: Pandas, NumPy

Model Persistence: Joblib

Frontend: HTML, CSS, Jinja2

Deployment: Railway (monorepo subdirectory deployment)

📊 Input Features
Feature	Description
CGPA	Academic performance
Aptitude Level	Logical & quantitative readiness (1–5)
Domain Skill Level	Core domain skill rating (1–5)
English Level	Communication proficiency (1–5)
Applied Work Count	Number of projects / applied works
Internship Count	Internship experience
🧠 ML Methodology

Algorithm: KMeans Clustering

Goal: Group students into readiness clusters

Cluster Labels:

Not Ready

Almost Ready

Ready

Why Clustering?

No predefined labels

Peer-based comparison

More realistic than rule-based scoring

🧾 Recommendation Output

Each student receives:

✅ Readiness Level

💪 Strengths (above peer average)

🎯 Top Focus Areas (highest impact improvements)

🚀 Estimated Impact of Improvements

💰 Expected Salary Range

📈 Career Growth Trajectory

🖥️ Application Flow

Student fills the form

Data is preprocessed and scaled

Cluster is predicted

Gaps vs peer cluster are calculated

Recommendation report is generated

Result is shown on the web page (and optionally emailed)

🧪 Running Locally

pip install -r requirements.txt
python app.py


Open:

http://127.0.0.1:5000

👤 Author

Mayank Joshi
Aspiring Data Scientist
Project built end-to-end with ML, backend, frontend, and deployment.