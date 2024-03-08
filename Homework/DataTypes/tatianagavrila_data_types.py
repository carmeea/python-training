"""
Sales Report Processing
You are given the data for quarter sales: sales = [120, 150, 170, 100].
a. Calculate the total sales for the quarter.
b. Calculate the average sales per month.
c. Print both the total and the average, formatted to two decimal places.
"""
sales = [120, 150, 170, 100]
# a. Calculate the total sales for the quarter
total_sales = sum(sales)
print(total_sales)

# b. Calculate the average sales per month
average_sales = total_sales / len(sales)
print(average_sales)

# c. Print both the total and the average, formatted to two decimal places.
print(f"Total sales for the quarter: {total_sales:.2f}, \nAverage sales per month: {average_sales:.2f}")


"""
Read from input a string with your name.
a. Create a dictionary for you as called 'employee' with department, 
b. Add a new field 'email' with the value 'alice.finance@example.com'.
c. Print the dictionary.
"""

# a. Read from input a string with your name
your_name = input("Enter your name: ")

# b. Create a dictionary for you called 'employee' with department
employee = {'name': your_name, 'department': 'Finance'}

# c. Add a new field 'email' with the value 'alice.finance@example.com'
employee['email'] = f'{your_name.lower()}.finance@example.com'

# d. Print the dictionary
print(employee)

"""
Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
a. Print the entire tuple.
b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
c. Print a confirmation message including the name of the booked room.
"""
# a. Create a tuple with the names of three conference rooms
conference_rooms = ('Aspen', 'Birch', 'Cedar')

# b. Print the entire tuple
# print(f"Conference rooms: {conference_rooms}")
print("Conference rooms:", conference_rooms)

# c. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book
room_number = int(input("Enter the number (1, 2, or 3) of the room you want to book: "))

# Validate user input
if 1 <= room_number <= len(conference_rooms):
    # Print a confirmation message including the name of the booked room
    booked_room = conference_rooms[room_number - 1]
    print(f"Confirmation: You have booked room '{booked_room}'.")
else:
    print("Invalid room number. Please enter a number between 1 and 3.")


"""
Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
b. Update the list and print the updated inventory.
c. Print the list
"""
# a. Create a list of products
products = ['Laptop', 'Phone', 'Printer', 'Headset', 'Monitor']

# b. Update the list (remove 'Printer' and add 'Tablet')
products.remove('Printer')
products.append('Tablet')
print(products)

# c. Print the updated inventory
print("Updated list for Inventory:", products)
