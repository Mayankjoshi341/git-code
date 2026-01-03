import pandas as pd

def profile_clusters(df: pd.DataFrame, feature_cols : list):

    """
    Profiles clusters in the given DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing cluster assignments.
    cluster_col (str): The name of the column containing cluster labels.

    Returns:
    pd.DataFrame: A DataFrame summarizing the mean values of features for each cluster.
    """
    profiling_df = df.groupby('cluster')[feature_cols].mean().reset_index()
    return profiling_df

def map_readliness_levels(cluster_profile: pd.DataFrame) -> pd.DataFrame:
    """
    Maps clusters to readiness levels based on overvall readiness score.

    Returns:
    pd.DataFrame: Updated DataFrame with a new 'readiness_level' column.
    """

    cluster_profile = cluster_profile.copy()

    cluster_profile["readiness_score"] = cluster_profile.mean(axis=1)

    sorted_clusters = cluster_profile.sort_values(by="readiness_score").index.tolist()

    readiness_map = {
        sorted_clusters[0]: "Not Ready",
        sorted_clusters[1]: "Almost Ready",
        sorted_clusters[2]: "Ready"
    }   
    return readiness_map , cluster_profile
