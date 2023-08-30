import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Generate synthetic customer data
np.random.seed(0)
num_customers = 300
purchase_history = np.random.randint(0, 100, num_customers)
browsing_behavior = np.random.randint(0, 100, num_customers)

# Create a DataFrame
data = pd.DataFrame({'purchase_history': purchase_history, 'browsing_behavior': browsing_behavior})

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(data)

# Determine the number of clusters (using the "elbow" method)
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot the elbow curve
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Based on the elbow curve, choose the optimal number of clusters
num_clusters = 3  # Replace with the chosen number of clusters

# Apply KMeans clustering
kmeans = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
cluster_labels = kmeans.fit_predict(X_scaled)

# Add cluster labels to the original data
data['Cluster'] = cluster_labels

# Perform PCA for visualization (if desired)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Plot the clusters in 2D space
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=cluster_labels, cmap='viridis')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.title('Customer Segmentation')
plt.show()

# Print the number of customers in each cluster
print(data['Cluster'].value_counts())


