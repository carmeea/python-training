"""
Sales Report Processing
You are given the data for quarter sales: sales = [120, 150, 170, 100].
a. Calculate the total sales for the quarter.
b. Calculate the average sales per month.
c. Print both the total and the average, formatted to two decimal places.
"""

sales = [120, 150, 170, 100]
total_sales = 0
average_sales = 0

for i in sales:
    total_sales = total_sales + i

average_sales = total_sales / len(sales)

print(f"The sales for the whole quarter are: {total_sales:.2f}.")
print(f"For this quarter the average sales/month are: {average_sales:.2f}.")