"""
Sales Report Processing
You are given the data for quarter sales: sales = [120, 150, 170, 100].
a. Calculate the total sales for the quarter.
b. Calculate the average sales per month.
c. Print both the total and the average, formatted to two decimal places.
"""

# You are given the data for quarter sales: sales = [120, 150, 170, 100].
sales = [120, 150, 170, 100]
# a. Calculate the total sales for the quarter.
total_sales = sales[0] + sales[1] + sales[2] + sales[3]
# b. Calculate the average sales per month.
average_sales = total_sales / 4
# c. Print both the total and the average, formatted to two decimal places.
message = "The total sales for the quarter is {0:d} and the average sales per month is {1:.2f}".format(
    total_sales, average_sales
)
print(message)

"""
Read from input a string with your name.
a. Create a dictionary for you as called 'employee' with department, 
b. Add a new field 'email' with the value 'alice.finance@example.com'.
c. Print the dictionary.
"""
import pprint

# Read from input a string with your name.
myName = input("Please enter your name: ")
# a. Create a dictionary for you as called 'employee' with department,
employee = {"name": myName, "department": "div 5-6"}
# b. Add a new field 'email' with the value 'alice.finance@example.com'.
employee["email"] = "alice.finance@example.com"
# c. Print the dictionary.
# print("The dictionary is: ", employee)
pprint.pprint(employee)

"""
Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
a. Print the entire tuple.
b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
c. Print a confirmation message including the name of the booked room.
"""
# Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
conference_rooms = ("Aspen", "Birch", "Cedar")
# a. Print the entire tuple.
print("Conference Rooms:", conference_rooms)
# b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
roomBooked = input(
    "Please let us know what room do you want to book (input a number between 1 and 3): "
)
# c. Print a confirmation message including the name of the booked room.
print(f"The booked room rezerved is ${conference_rooms[int(roomBooked)-1]}.")

"""
Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
b. Update the list and print the updated inventory.
c. Print the list
"""
# Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
listProducts = ["Laptop", "Phone", "Printer", "Headset", "Monitor"]
# a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
inventory = []
inventory.extend(listProducts)
inventory.remove("Printer")
inventory.append("Tablet")
# b. Update the list and print the updated inventory.
listProducts = inventory
print("Updated inventory is: ", inventory)
# c. Print the list
print("Updated list is: ", listProducts)
