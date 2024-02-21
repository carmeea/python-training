
"""
Sales Report Processing
You are given the data for quarter sales: sales = [120, 150, 170, 100].
a. Calculate the total sales for the quarter.
b. Calculate the average sales per month.
c. Print both the total and the average, formatted to two decimal places.
"""
sales = [120, 150, 170, 100]
per_month = len(sales)
quarter_total_sales = sales[0] + sales[1] + sales[2] + sales[3]
quarter_average_sales = int(quarter_total_sales) / int(per_month)
print(f"Total sales for the quarter is: {quarter_total_sales}")
print(f"Average sales for the quarter is: {quarter_average_sales}")
# OR
quarter_total_sales2 = sum(sales)
quarter_average_sales2 = quarter_total_sales2 / int(per_month)
print(f"Total sales for the quarter is: {quarter_total_sales2}")
print(f"Average sales for the quarter is: {quarter_average_sales2}")
# OR
quarter_total_sales3 = sum(int(i) for i in sales)
quarter_average_sales3 = quarter_total_sales3 / per_month
print(f"Total sales for the quarter is: {quarter_total_sales3}")
print(f"Average sales for the quarter is: {quarter_average_sales3}")


"""
Read from input a string with your name.
a. Create a dictionary for you as called 'employee' with department, 
b. Add a new field 'email' with the value 'alice.finance@example.com'.
c. Print the dictionary.
"""
name = input("Enter your name: ")

department = {"employee": name}
department["email"] = "alice.finance@example.com"
# OR
# contact = {"email": "alice.finance@example.com"}
# department.update(contact)

print(department)


"""
Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
a. Print the entire tuple.
b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
c. Print a confirmation message including the name of the booked room.
"""
conference_rooms = ("Aspen", "Birch", "Cedar")
print("Available conference rooms: ", conference_rooms)
conference_room_number = input("Please enter 0 for Aspen, 1 for Birch or 2 for Cedar, to book your desired room: ")
print("You have booked ", conference_rooms[int(conference_room_number)])
# OR
# print("Please enter 0 for Aspen, 1 for Birch or 2 for Cedar, to book your desired room")
# print("You have booked ", conference_rooms[int(input())])


"""
Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
b. Update the list and print the updated inventory.
c. Print the list
"""

products = ['Laptop', 'Phone', 'Printer', 'Headset', 'Monitor']
# products.remove('Printer')
# OR
products.pop(2)
print(products)
# products.append('Tablet')
products.insert(2, 'Tablet')
print(products)