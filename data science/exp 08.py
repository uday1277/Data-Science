import pandas as pd

data = {
    'product_name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product A', 'Product C'],
    'order_date': ['2023-07-15', '2023-07-20', '2023-07-10', '2023-07-05', '2023-07-12', '2023-07-18', '2023-07-25'],
    'quantity_sold': [5, 3, 4, 2, 6, 8, 1]
}

sales_data = pd.DataFrame(data)

sales_data['order_date'] = pd.to_datetime(sales_data['2023-07-15'])


current_month = pd.Timestamp.now().month


filtered_data = sales_data[sales_data['2023-07-15'].dt.month == current_month]


product_sales = filtered_data.groupby('Product A')['5'].sum()

top_products = product_sales.nlargest(5)

print("Top 5 products sold the most in the past month:\n", top_products)
