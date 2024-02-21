"""
Sales Report Processing
You are given the data for quarter sales: 
"""
sales = [120, 150, 170, 100]
""""
a. Calculate the total sales for the quarter."""
total_sales = sum(sales)
print(total_sales)
"""
b. Calculate the average sales per month.
"""
sales_length = len(sales)
sales_average = total_sales / sales_length
print(sales_average)

""""
c. Print both the total and the average, formatted to two decimal places.
"""
formattedSales = "Total sales: %6.2f, the average sales: %6.2f" % (total_sales,sales_average
)
print(formattedSales)
"""
"""

"""
Read from input a string with your name.
a. Create a dictionary for you as called 'employee' with department, 
"""
name = input("Enter your name:")
employee = {"name": name, "department": "Engineering"}
"""
b. Add a new field 'email' with the value 'alice.finance@example.com'.
"""
employee["email"]='alice.finance@example.com'
"""
c. Print the dictionary.
"""
print(employee)
"""
"""
"""
Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
a. Print the entire tuple.
"""
conference_rooms=(
    "Aspen",
    "Birch",
    "Cedar"
)
print(conference_rooms)
"""
b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
"""
room_number= input("Enter the number 1,2 or 3, corresponding to your room number")
"""
c. Print a confirmation message including the name of the booked room.
"""

"""
Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
"""
products= ['Laptop', 'Phone', 'Printer', 'Headset', 'Monitor']
"""
a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
"""
del products[2]
products.append("Tablet")

"""
b. Update the list and print the updated inventory.

c. Print the list
"""
print(products)
"""
"""
