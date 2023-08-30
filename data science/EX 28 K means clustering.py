import numpy as np
from sklearn.cluster import KMeans

# Sample customer data (replace this with your actual dataset)
customer_data = np.array([
    [10, 5, 3, 2],    # Customer 1
    [5, 8, 1, 6],    # Customer 2
    [2, 9, 4, 3],    # Customer 3
    [7, 3, 2, 9],    # Customer 4
    # Add more customer data here
])

# Number of clusters (segments)
num_clusters = 3

# Fit K-Means model
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(customer_data)

# Input shopping-related features of a new customer
new_customer_features = np.array([8, 4, 6, 3])  # Replace with actual new customer features

# Predict the segment for the new customer
predicted_segment = kmeans.predict(new_customer_features.reshape(1, -1))

print(f"The new customer belongs to segment {predicted_segment[0]}")
