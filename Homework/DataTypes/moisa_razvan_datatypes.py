"""
Sales Report Processing
You are given the data for quarter sales: sales = [120, 150, 170, 100].
a. Calculate the total sales for the quarter.
b. Calculate the average sales per month.
c. Print both the total and the average, formatted to two decimal places.
"""
sales = [120, 150, 170, 100]
sales_per_year = 0
for i in sales:
    sales_per_year = sales_per_year+i
sales_per_month = sales_per_year/12
print(f"We have an average of {sales_per_month:.2f} per month, and {sales_per_year:.2f} annually on sales")


"""
Read from input a string with your name.
a. Create a dictionary for you as called 'employee' with department, 
b. Add a new field 'email' with the value 'alice.finance@example.com'.
c. Print the dictionary.
"""

name = input('Insert your name: ')
employee = {"name" : name}
print(employee)
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

select_room = int(input("Please select a room, between 1-3: "))
if select_room == 1:
    print(f'You have selected {conference_rooms[select_room-1]} room. Have a wonderful stay')
elif select_room == 2:
    print(f'You have selected {conference_rooms[select_room-1]} room. Have a wonderful stay')
elif select_room == 3:
    print(f'You have selected {conference_rooms[select_room-1]} room. Have a wonderful stay')


"""
Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
b. Update the list and print the updated inventory.
c. Print the list
"""

product_list = ["Laptop", "Phone", "Printer", "Headset", "Monitor"]
product_list.remove("Phone")
print(product_list)

product_list.append("Tablet")
print(product_list)