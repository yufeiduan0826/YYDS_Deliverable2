# Re-import necessary libraries after reset
import pandas as pd

# Reload the clustered data
file_path = "d3.csv"
df_clustered = pd.read_csv(file_path)

# Get max cluster ID and define the number of output files
max_cluster_id = df_clustered['word2vec_cluster'].max()
num_files = max_cluster_id + 1

# Save each cluster to its own CSV file
output_paths = []
for cluster_id in range(num_files):
    cluster_df = df_clustered[df_clustered['word2vec_cluster'] == cluster_id]
    output_path = f"cluster_{cluster_id}.csv"
    cluster_df.to_csv(output_path, index=False)
    output_paths.append(output_path)

