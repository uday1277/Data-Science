import numpy as np

sales_data = np.array([250000, 300000, 280000, 320000])

total_sales = np.sum(sales_data) 

percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print("Total Sales for the Year:", total_sales)
print("Percentage Increase in Sales from Q1 to Q4:", percentage_increase, "%")
