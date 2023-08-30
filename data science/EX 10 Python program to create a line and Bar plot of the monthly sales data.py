import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [10000, 15000, 12000, 18000, 22000, 20000]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

ax1.plot(months, sales, marker='o')
ax1.set_title('Monthly Sales (Line Plot)')
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales')

ax2.bar(months, sales)
ax2.set_title('Monthly Sales (Bar Plot)')
ax2.set_xlabel('Month')
ax2.set_ylabel('Sales')

plt.tight_layout()

plt.show()
