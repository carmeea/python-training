"""
Sales Report Processing
You are given the data for quarter sales: sales = [120, 150, 170, 100].
a. Calculate the total sales for the quarter.
b. Calculate the average sales per month.
c. Print both the total and the average, formatted to two decimal places.
"""

sales = [120, 150, 170, 100]
total_sales = sum(sales)
average_sales = total_sales / len(sales)
print(total_sales, 2)
print(average_sales, 2)

"""
Read from input a string with your name.
a. Create a dictionary for you as called 'employee' with department, 
b. Add a new field 'email' with the value 'alice.finance@example.com'.
c. Print the dictionary.
"""

employee = {"departmen" : "finance"}
employee["email"] = "alice.finance@example.com"
print(employee)

"""
Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
a. Print the entire tuple.
b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
c. Print a confirmation message including the name of the booked room.
"""

conference_rooms = ("Aspen", "Birch", "Cedar")
print("The list of rooms is:", conference_rooms)

book_room = int(input("Which room do you want to book from 1 to 3?: "))
try:
    booked_room = conference_rooms[booked_room]
    print("The room you booked: ", booked_room)
except KeyError:
    print("The room you want to book does not exist")

"""
Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
b. Update the list and print the updated inventory.
c. Print the list
"""

products = ["Laptop", "Phone", "Printer", "Headset", "Monitor"]
del products[2]
products.insert(2, "Tablet")
print(products)
