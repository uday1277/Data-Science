item_prices = [2.5, 3.0, 1.75, 4.25]
quantities = [3, 2, 5, 1]
discount_rate = 10
tax_rate = 8

total_price_before_discount = sum(item_price * quantity for item_price, quantity in zip(item_prices, quantities))
discount_amount = (discount_rate / 100) * total_price_before_discount
total_price_after_discount = total_price_before_discount - discount_amount
tax_amount = (tax_rate / 100) * total_price_after_discount 
total_cost = total_price_after_discount + tax_amount

print(f"Total cost: ${total_cost:.2f}")
