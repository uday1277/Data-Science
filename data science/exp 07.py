import pandas as pd


data = {
    'customer_id': [1, 2, 1, 3, 2, 1, 3],
    'order_date': ['2023-01-15', '2023-02-20', '2023-03-10', '2023-04-05', '2023-05-12', '2023-06-18', '2023-07-25'],
    'product_name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product A', 'Product C'],
    'order_quantity': [2, 3, 1, 4, 2, 1, 3]
}

order_data = pd.DataFrame(data)


total_orders_per_customer = order_data.groupby('customer_id')['order_date'].count()


average_order_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()

earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()

print("Total orders per customer:\n", total_orders_per_customer)
print("\nAverage order quantity per product:\n", average_order_quantity_per_product)
print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
  
