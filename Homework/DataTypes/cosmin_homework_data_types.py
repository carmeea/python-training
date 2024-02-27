"""
Sales Report Processing
You are given the data for quarter sales: sales = [120, 150, 170, 100].
a. Calculate the total sales for the quarter.
b. Calculate the average sales per month.
c. Print both the total and the average, formatted to two decimal places.
"""

sales = [120, 150, 170, 100]
total_sales = sum(sales)
average_sales_per_month = total_sales / len(sales)
print("Total sales: {:.2f}".format(total_sales))
print("Average sales per month: {:.2f}".format(average_sales_per_month))


"""
Read from input a string with your name.
a. Create a dictionary for you as called 'employee' with department, 
b. Add a new field 'email' with the value 'alice.finance@example.com'.
c. Print the dictionary.
"""

name = input("What's your name? ")
employee = {"name": name, "department": "qa"}
employee["email"] = "alice.finance@example.com"
print(employee)


"""
Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
a. Print the entire tuple.
b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
c. Print a confirmation message including the name of the booked room.
"""

conference_rooms = ("Aspen", "Birch", "Cedar")
print(conference_rooms)
room_number = int(input("Which room do you want to book: 1, 2 or 3? "))
if 1 <= room_number <= len(conference_rooms):
    booked_room = conference_rooms[room_number - 1]
    print(f"Room {room_number} ({booked_room}) has been booked.")
else:
    print("Invalid room number. Please enter a number between 1 and 3.")


"""
Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
b. Update the list and print the updated inventory.
c. Print the list
"""

products = ['Laptop', 'Phone', 'Printer', 'Headset', 'Monitor']
products[2] = "Tablet"
print(products)