import pandas as pd
from data_perparation import data_preparation
from preprocessing import fit_scaler
from clustering import train_kmeans_model, optimal_kmeans_clusters
from profiling import profile_clusters, map_readliness_levels
from joblib import dump
from pathlib import Path

base_dir = Path(__file__).resolve().parents[1]  


model_DIR = base_dir / "Models"
preprosed_DIR = base_dir / "data" / "processed"
synthetic_DIR = base_dir / "data" / "synthetic"
model_DIR.mkdir(parents=True, exist_ok=True)
preprosed_DIR.mkdir(parents=True, exist_ok=True)

# 1. Generate synthetic data
df = data_preparation(800)

features = [

    "cgpa",
    "aptitude_level",
    "domain_skill_level",
    "english_level",
    "applied_work_count",
    "internships_count"
]

x = df[features]
print("Data preparation completed.")
# 2. Scale the data

scaler, x_scaled = fit_scaler(x)
print("Data scaling completed.")
# 3. Train KMeans model
n_clusters = optimal_kmeans_clusters(x_scaled)
kmeans_model, clusters = train_kmeans_model(x_scaled, n_clusters=3)
df['cluster'] = clusters
print("KMeans clustering completed.")

# 4. Save the scaler and model
dump(scaler, model_DIR / 'kmeans_scaler.pkl')
dump(kmeans_model, model_DIR / 'kmeans_model.pkl')
df.to_csv(synthetic_DIR / 'synthetic_data.csv', index=False)
x_scaled.to_csv(preprosed_DIR / 'x_scaled_data.csv', index=False)
print("Models and scaler saved.")

# 5. Profile clusters
cluster_profile = profile_clusters(df, features)
print("Cluster profiling completed.")

# 6. Map readiness levels
readiness_map, updated_profile = map_readliness_levels(cluster_profile)
df['readiness_level'] = df['cluster'].map(readiness_map)
print("Readiness levels mapped.")

# 7. Save the final data and profile
dump(cluster_profile ,model_DIR / 'Cluster_profile.pkl')
dump(readiness_map ,model_DIR / 'readiness_map.pkl')
df.to_csv(preprosed_DIR / 'final_clustered_data.csv', index=False)
updated_profile.to_csv(preprosed_DIR / 'updated_cluster_profile.csv', index=False)
print("Final data and cluster profile saved.")

