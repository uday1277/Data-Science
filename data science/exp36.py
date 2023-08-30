import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample stock data (replace with your own data)
dates = pd.date_range(start='2023-01-01', periods=30, freq='B')  # 30 business days
closing_prices = np.array([150.0, 152.5, 153.0, 151.5, 155.0, 157.5, 156.0, 155.5, 158.0, 159.5,
                           160.0, 159.0, 157.5, 155.0, 153.5, 152.0, 153.5, 155.0, 157.5, 156.0,
                           157.0, 155.5, 154.0, 153.5, 155.0, 156.5, 158.0, 157.0, 158.5, 159.0])

# Create a DataFrame with stock data
stock_data = pd.DataFrame({'Date': dates, 'ClosingPrice': closing_prices})
stock_data.set_index('Date', inplace=True)

# Calculate daily returns
daily_returns = stock_data['ClosingPrice'].pct_change().dropna()

# Calculate mean and standard deviation of daily returns
mean_return = daily_returns.mean()
std_deviation = daily_returns.std()

# Calculate annualized mean return and volatility
annual_mean_return = mean_return * 252  # Assuming 252 trading days in a year
annual_volatility = std_deviation * np.sqrt(252)

# Print insights
print("Daily Mean Return:", mean_return)
print("Daily Standard Deviation:", std_deviation)
print("\nAnnualized Mean Return:", annual_mean_return)
print("Annualized Volatility:", annual_volatility)

# Plot daily returns
plt.figure(figsize=(10, 6))
plt.plot(daily_returns, color='blue')
plt.xlabel('Trading Days')
plt.ylabel('Daily Returns')
plt.title('Stock Daily Returns')
plt.show()
