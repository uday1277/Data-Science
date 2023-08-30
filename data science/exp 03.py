import numpy as np
np.random.seed(42)  
num_houses = 100
bedrooms = np.random.randint(1, 7, size=num_houses)
sale_prices = np.random.randint(100000, 500000, size=num_houses)  

house_data = np.column_stack((bedrooms, sale_prices))


bedrooms = house_data[:, 0]
sale_prices = house_data[:, 1]


more_than_four_bedrooms_mask = bedrooms > 4


sale_prices_more_than_four_bedrooms = sale_prices[more_than_four_bedrooms_mask]

average_sale_price_more_than_four_bedrooms = np.mean(sale_prices_more_than_four_bedrooms)

print("Average sale price of houses with more than four bedrooms:", average_sale_price_more_than_four_bedrooms)
