"""
Sales Report Processing
You are given the data for quarter sales: sales = [120, 150, 170, 100].
a. Calculate the total sales for the quarter.
b. Calculate the average sales per month.
c. Print both the total and the average, formatted to two decimal places.
"""

sales = [120, 150, 170, 100]
sum = 0
for sale in sales:
    sum += sale
total_sales = sum
average_sales = total_sales / len(sales)
message = "The total sales for the quarter is {0:d} and the average sales per month is {1:.2f}".format(
    total_sales, average_sales
)
print(message)
