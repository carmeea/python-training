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

print("Total Quarter Sales: {:.2f}".format(total_quarter_sales))
print("Average Sales per Month: {:.2f}".format(average_sales))

"""
Read from input a string with your name.
a. Create a dictionary for you as called 'employee' with department, name , age
b. Add a new field 'email' with the value 'alice.finance@example.com'.
c. Print the dictionary.
"""

# a. Create a dictionary for you as called 'employee' with department, name , age
employee = {"name": "Dan", "age": 21, "department": "IT"}

# b. Add a new field 'email' with the value 'alice.finance@example.com'.
employee["email"] = "alice.finance@example.com"

# c. Print the dictionary.
print(employee)

"""
Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
a. Print the entire tuple.
b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
c. Print a confirmation message including the name of the booked room.
"""

# a. Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'. Print the entire tuple.

conference_rooms = ('Aspen', 'Birch', 'Cedar')
print("Conference Rooms:", conference_rooms)

# b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book

room_number = input("Enter the room number you want to book (0-2):" )

# c. Print a confirmation message including the name of the booked room.
print("You have successfully booked the", conference_rooms[int(room_number)], "room.")


"""
Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
b. Update the list and print the updated inventory.
c. Print the list
"""

# List of products
products = ['Laptop', 'Phone', 'Printer', 'Headset', 'Monitor']

# a. Remove 'Printer' and add 'Tablet'
products.remove('Printer')
products.append('Tablet')

# b. Print the updated inventory
print("Updated inventory:", products)

# c. Print the list
print("List of products:", products)

