import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Generate synthetic transaction data
np.random.seed(0)
num_customers = 300
customer_ids = np.arange(1, num_customers + 1)
total_amounts = np.random.randint(10, 500, num_customers)
visit_frequencies = np.random.randint(1, 20, num_customers)

# Create a DataFrame with synthetic data
data = {'CustomerID': customer_ids, 'TotalAmount': total_amounts, 'VisitFrequency': visit_frequencies}
transaction_df = pd.DataFrame(data)

# Select features for clustering
features = ['TotalAmount', 'VisitFrequency']
X = transaction_df[features]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine the optimal number of clusters using silhouette score
silhouette_scores = []
for n_clusters in range(2, 11):
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
    cluster_labels = kmeans.fit_predict(X_scaled)
    silhouette_scores.append(silhouette_score(X_scaled, cluster_labels))

# Plot the silhouette scores
plt.plot(range(2, 11), silhouette_scores)
plt.title('Silhouette Score')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.show()

# Based on the silhouette score, choose the optimal number of clusters
num_clusters = 3  # Replace with the chosen number of clusters

# Apply KMeans clustering
kmeans = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
cluster_labels = kmeans.fit_predict(X_scaled)

# Add cluster labels to the original data
transaction_df['Cluster'] = cluster_labels

# Plot the clusters
plt.scatter(transaction_df['TotalAmount'], transaction_df['VisitFrequency'], c=cluster_labels, cmap='viridis')
plt.xlabel('Total Amount')
plt.ylabel('Visit Frequency')
plt.title('Customer Segmentation')
plt.show()

# Display the number of customers in each cluster
print(transaction_df['Cluster'].value_counts())
