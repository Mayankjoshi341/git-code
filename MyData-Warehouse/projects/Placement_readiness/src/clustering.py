import pandas as pd
from sklearn.cluster import KMeans
from kneed import KneeLocator

def optimal_kmeans_clusters(x_scaled, max_k=10):
    inertias = [
        KMeans(n_clusters=k, random_state=42, n_init=10)
        .fit(x_scaled)
        .inertia_
        for k in range(1, max_k + 1)
    ]

    kl = KneeLocator(
        x=range(1, max_k + 1),
        y=inertias,
        curve="convex",
        direction="decreasing"
    )

    return kl.elbow 
def train_kmeans_model(x_scaled, n_clusters=None):
    """
    Trains a KMeans clustering model on the provided data.

    Parameters:
    data (pd.DataFrame): The input data for clustering.
    n_clusters (int): The number of clusters to form.

    Returns:
    KMeans: The trained KMeans model.
    """
    model = KMeans(n_clusters=n_clusters, random_state=42 , n_init=10)
    clusters = model.fit_predict(x_scaled)

    return model , pd.Series(clusters, index=x_scaled.index, name='cluster')
