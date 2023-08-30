import numpy as np

# Example quarterly sales data for demonstration
sales_data = np.array([250000, 300000, 280000, 320000])

# Calculate total sales for the year
total_sales = np.sum(sales_data)

# Calculate percentage increase from the first quarter to the fourth quarter
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print("Total Sales for the Year:", total_sales)
print("Percentage Increase in Sales from Q1 to Q4:", percentage_increase, "%")
