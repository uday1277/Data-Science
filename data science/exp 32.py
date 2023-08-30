import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generate synthetic house data
np.random.seed(0)
num_houses = 100
house_sizes = np.random.randint(1000, 3000, num_houses)
house_prices = 50000 + 100 * house_sizes + np.random.normal(0, 5000, num_houses)

# Create a DataFrame with synthetic data
data = {'HouseSize': house_sizes, 'Price': house_prices}

# Select the feature for bivariate analysis and modeling
feature = 'HouseSize'

# Split the data into features (X) and target (y)
X = data[feature].reshape(-1, 1)
y = data['Price']

# Perform bivariate analysis: scatter plot
plt.scatter(X, y, alpha=0.7)
plt.xlabel(feature)
plt.ylabel('Price')
plt.title('Bivariate Analysis')
plt.show()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Build a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict house prices on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Plot the regression line and test data
plt.scatter(X_test, y_test, alpha=0.7, label='Test Data')
plt.plot(X_test, y_pred, color='red', label='Regression Line')
plt.xlabel(feature)
plt.ylabel('Price')
plt.title('Linear Regression Model')
plt.legend()
plt.show()
