import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("MyData-Warehouse/projects/Placement_readiness/Data/processed/updated_cluster_profile.csv")

df.set_index('cluster', inplace=True)
df.plot(kind='bar', figsize=(10,6))
plt.title('Cluster Profiling')
plt.xlabel('Cluster')
plt.ylabel('Mean Feature Values')
plt.legend(title='Features', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

plt.scatter(df.index, df['readiness_score'])
plt.title('Readiness Score by Cluster')
plt.xlabel('Cluster')
plt.ylabel('Readiness Score')
plt.grid(True)
plt.show()  