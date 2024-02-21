"""
Sales Report Processing
You are given the data for quarter sales: sales = [120, 150, 170, 100].
a. Calculate the total sales for the quarter.
b. Calculate the average sales per month.
c. Print both the total and the average, formatted to two decimal places.
"""
#a.
sales = [120, 150, 170, 100]
total_sales = sum(sales)
print(f"Total sales for the quarter: ${total_sales}.")

#b.
average_sales = total_sales / len(sales)
print(f"Average sales per month:  ${average_sales}.")

#c.
print(f"Total sales for the quarter: ${total_sales:.2f}.")
print(f"Average sales per month:  ${average_sales:.2f}.")


"""
Read from input a string with your name.
a. Create a dictionary for you as called 'employee' with department, 
b. Add a new field 'email' with the value 'alice.finance@example.com'.
c. Print the dictionary.
"""

name = input("Enter your name: ")

#a. 
employee = {
    'name': name,
    'department': 'Finance'
}


#b. 
employee['email'] = 'alice.finance@example.com'

#c.
print(employee)



"""
Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
a. Print the entire tuple.
b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
c. Print a confirmation message including the name of the booked room.
"""


conference_rooms = ('Aspen', 'Birch', 'Cedar')

#a. 
print("Available conference rooms:", conference_rooms)

#b.
selected_room_number = int(input("Enter the room number you want to book (1,2, or 3): "))

#c.
booked_room = conference_rooms[selected_room_number] 
print(f"Room {booked_room} has been booked.")
"""
Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
b. Update the list and print the updated inventory.
c. Print the list
"""

products = ['Laptop', 'Phone', 'Printer', 'Headset', 'Monitor']

#a.
products.remove('Printer')
products.append('Tablet')

#b. 
print("Updated Inventory:", products)

#c.
print("Current Inventory:", products)