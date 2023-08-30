import numpy as np
sales_data = np.array([250000, 280000, 320000, 350000])
total_sales = np.sum(sales_data)
first_quarter_sales = sales_data[0]
fourth_quarter_sales = sales_data[-1]
percentage_increase = ((fourth_quarter_sales - first_quarter_sales) / first_quarter_sales) * 100
print("Total Sales for the Year:", total_sales)
print("Percentage Increase from Q1 to Q4:", percentage_increase,"%")
