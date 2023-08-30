import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

# Generate synthetic medical data
np.random.seed(0)
num_patients = 200
age = np.random.randint(18, 80, num_patients)
gender = np.random.choice(['Male', 'Female'], num_patients)
blood_pressure = np.random.randint(90, 180, num_patients)
cholesterol = np.random.randint(120, 280, num_patients)
treatment_outcomes = np.random.choice(['Good', 'Bad'], num_patients)

# Create a DataFrame with synthetic data
data = {'Age': age, 'Gender': gender, 'BloodPressure': blood_pressure, 'Cholesterol': cholesterol, 'Outcome': treatment_outcomes}
medical_df = pd.DataFrame(data)

# Convert categorical variables to numerical using one-hot encoding
medical_df = pd.get_dummies(medical_df, columns=['Gender'], drop_first=True)
medical_df['Outcome'] = medical_df['Outcome'].apply(lambda x: 1 if x == 'Good' else 0)

# Select features for modeling
features = ['Age', 'BloodPressure', 'Cholesterol', 'Gender_Male']
X = medical_df[features]
y = medical_df['Outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build a KNN classifier
k = 5  # Number of neighbors
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = knn.predict(X_test_scaled)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

# Display the classification report and confusion matrix
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
