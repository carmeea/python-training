# tema
"""
Sales Report Processing
You are given the data for quarter sales: sales = [120, 150, 170, 100].
a. Calculate the total sales for the quarter.
b. Calculate the average sales per month.
c. Print both the total and the average, formatted to two decimal places.
"""
quarter_sales = [120, 150, 170, 100]
total_sales_for_quarter = sum(quarter_sales)
total_sales_period = len(quarter_sales)
average_sales_for_the_quarter = total_sales_for_quarter / total_sales_period

print(f"Total sales for the quarter is: {total_sales_for_quarter:.2f}")
print(f"Average sales for the quarter is: {average_sales_for_the_quarter:.2f}")

"""
Read from input a string with your name.
a. Create a dictionary for you as called 'employee' with department, 
b. Add a new field 'email' with the value 'alice.finance@example.com'.
c. Print the dictionary.
"""

name = input("Enter your name: ")

department = {"employee": name}
contact = {"email": "alice.finance@example.com"}
department.update(contact)

print(department)

"""
Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
a. Print the entire tuple.
b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
c. Print a confirmation message including the name of the booked room.
"""

conferenceRooms = (
    "Aspen",
    "Birch",
    "Cedar",
)
print("Available conference rooms: ", conferenceRooms)
print("Please enter 0 for Aspen,1 for Birch or 2 for Cedar, to book your desired room")
print("You have booked ", conferenceRooms[int(input())])


"""
Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
b. Update the list and print the updated inventory.
c. Print the list
"""

products = ["Laptop", "Phone", "Printer", "Headset", "Monitor"]
products.remove("Printer")
print(products)
products.append("Tablet")
print(products)
