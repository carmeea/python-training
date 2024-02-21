"""
Sales Report Processing
You are given the data for quarter sales: sales = [120, 150, 170, 100].
a. Calculate the total sales for the quarter.
b. Calculate the average sales per month.
c. Print both the total and the average, formatted to two decimal places.
"""

# a. Calculate the total sales for the quarter.


sales1 = 120
sales2 = 150
sales3 = 170
sales4 = 100
total_quarter_sales = sales1 + sales2 + sales3 + sales4
print(f"The total sales for the quarter are {total_quarter_sales}.")

sales = [120, 150, 170, 100]
total_quarter_sales = sum(sales)
print(f"The total sales for the quarter are {total_quarter_sales}.")

# b. Calculate the average sales per month.

average_sales = total_quarter_sales / 4
average_sales = total_quarter_sales / len(sales)
print(f"The average sales per month is {average_sales}")

# c. Print both the total and the average, formatted to two decimal places.

print("Total Sales: {:.2f}".format(total_quarter_sales))
print("Average Sales per Month: {:.2f}".format(average_sales))

"""
Read from input a string with your name.
a. Create a dictionary for you as called 'employee' with department, 
b. Add a new field 'email' with the value 'alice.finance@example.com'.
c. Print the dictionary.
"""

"""
Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
a. Print the entire tuple.
b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
c. Print a confirmation message including the name of the booked room.
"""

"""
Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
b. Update the list and print the updated inventory.
c. Print the list
"""
