import numpy as np
import pandas as pd

# Generate synthetic temperature data
np.random.seed(0)
num_days = 365
cities = ['City A', 'City B', 'City C', 'City D']
temperature_data = {
    'City': np.random.choice(cities, num_days),
    'Temperature': np.random.uniform(-10, 40, num_days)
}

# Create a DataFrame with synthetic data
data = pd.DataFrame(temperature_data)

# Calculate the mean temperature for each city
mean_temperatures = data.groupby('City')['Temperature'].mean()

# Calculate the standard deviation of temperature for each city
std_dev_temperatures = data.groupby('City')['Temperature'].std()

# Determine the city with the highest temperature range
temperature_ranges = data.groupby('City')['Temperature'].apply(lambda x: x.max() - x.min())
city_with_highest_range = temperature_ranges.idxmax()

# Find the city with the most consistent temperature (lowest standard deviation)
city_with_lowest_std = std_dev_temperatures.idxmin()

print("Mean Temperatures:\n", mean_temperatures)
print("\nStandard Deviations of Temperatures:\n", std_dev_temperatures)
print("\nCity with Highest Temperature Range:", city_with_highest_range)
print("City with Most Consistent Temperature:", city_with_lowest_std)

