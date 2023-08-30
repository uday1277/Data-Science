import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Generate synthetic transaction data
np.random.seed(0)
num_customers = 200
customer_ids = np.arange(1, num_customers + 1)
total_amounts = np.random.randint(50, 500, num_customers)
num_items = np.random.randint(1, 20, num_customers)

# Create a DataFrame with synthetic data
data = {'CustomerID': customer_ids, 'TotalAmount': total_amounts, 'NumItems': num_items}
transaction_df = pd.DataFrame(data)

# Select features for clustering
features = ['TotalAmount', 'NumItems']
X = transaction_df[features]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Build a K-Means clustering model
num_clusters = 4  # Number of clusters
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
cluster_labels = kmeans.fit_predict(X_scaled)

# Add cluster labels to the original data
transaction_df['Cluster'] = cluster_labels

# Plot the clusters using scatter plots
plt.figure(figsize=(10, 6))
colors = ['blue', 'green', 'red', 'purple']
for cluster_id, color in zip(range(num_clusters), colors):
    cluster_data = transaction_df[transaction_df['Cluster'] == cluster_id]
    plt.scatter(cluster_data['TotalAmount'], cluster_data['NumItems'], c=color, label=f'Cluster {cluster_id}')
plt.xlabel('Total Amount')
plt.ylabel('Number of Items')
plt.title('Customer Clusters')
plt.legend()
plt.show()
