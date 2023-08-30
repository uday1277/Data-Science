import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generate synthetic car data 
np.random.seed(0)
num_cars = 100
engine_sizes = np.random.uniform(1.0, 3.5, num_cars)  # Liters
horsepowers = np.random.randint(100, 400, num_cars)
fuel_efficiencies = np.random.uniform(10, 40, num_cars)  # MPG
car_prices = 15000 + 8000 * engine_sizes + 100 * horsepowers - 500 * fuel_efficiencies + np.random.normal(0, 5000, num_cars)

# Create a DataFrame with synthetic data
data = {'EngineSize': engine_sizes, 'Horsepower': horsepowers, 'FuelEfficiency': fuel_efficiencies, 'Price': car_prices}
car_df = pd.DataFrame(data)

# Select features for modeling
features = ['EngineSize', 'Horsepower', 'FuelEfficiency']
X = car_df[features]
y = car_df['Price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Build a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict car prices on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Get coefficients and feature names
coefficients = model.coef_
feature_names = features

# Print the coefficients for each feature
for feature_name, coefficient in zip(feature_names, coefficients):
    print(f"{feature_name}: {coefficient:.2f}")

# Plot predicted prices vs. actual prices
plt.scatter(y_test, y_pred, alpha=0.7)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs. Predicted Car Prices')
plt.show()
