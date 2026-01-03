from data_perparation import data_preparation
from preprocessing import fit_scaler
from clustering import train_kmeans_model, optimal_kmeans_clusters
from profiling import profile_clusters, map_readliness_levels
from joblib import dump

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

# 2. Scale the data

scaler, x_scaled = fit_scaler(x)

# 3. Train KMeans model
n_clusters = optimal_kmeans_clusters(x_scaled)
kmeans_model, clusters = train_kmeans_model(x_scaled, n_clusters=3)
df['cluster'] = clusters


# 4. Save the scaler and model
dump(scaler, 'MyData-Warehouse/projects/Placement_readiness/models/kmeans_scaler.joblib')
dump(kmeans_model, 'MyData-Warehouse/projects/Placement_readiness/models/kmeans_model.joblib')
dump(df, 'MyData-Warehouse/projects/Placement_readiness/data/synthetic/clustered_data.joblib')
dump(x_scaled, 'MyData-Warehouse/projects/Placement_readiness/data/processed/x_scaled.joblib')


# 5. Profile clusters
cluster_profile = profile_clusters(df, features)

# 6. Map readiness levels
readiness_map, updated_profile = map_readliness_levels(cluster_profile)
df['readiness_level'] = df['cluster'].map(readiness_map)

# 7. Save the final data and profile
dump(df, 'MyData-Warehouse/projects/Placement_readiness/data/processed/final_clustered_data.joblib')
dump(updated_profile, 'MyData-Warehouse/projects/Placement_readiness/data/processed/cluster_profile.joblib')