"""Sales Report Processing
You are given the data for quarter sales: sales = [120, 150, 170, 100].
a. Calculate the total sales for the quarter.
b. Calculate the average sales per month.
c. Print both the total and the average, formatted to two decimal places.
"""

sales = [120, 150, 170, 100]
total_sales = sum(sales)
average_Sales = total_sales / len(sales)
print(total_sales, 2)
print(average_Sales, 2)


"""
Read from input a string with your name.
a. Create a dictionary for you as called 'employee' with department, 
b. Add a new field 'email' with the value 'alice.finance@example.com'.
c. Print the dictionary.
"""
name = input("Write your name: ")
employee = {"name" : name , "department" : ""}
employee["email"] = "alice.finance@example.com"
print(employee)


"""
Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
a. Print the entire tuple.
b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
c. Print a confirmation message including the name of the booked room.
"""

conference_rooms = ("Aspen", "Birch", "Cedar")

print("The conference rooms are:", conference_rooms)

choose_room = int(input("Choose one of the 3 rooms (1-3): "))

try:
    chosen_room = conference_rooms[choose_room]
    print("You chose the room:", chosen_room)
except KeyError:
    print("The number you introduced doesn't exist")




"""
Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
b. Update the list and print the updated inventory.
c. Print the list
"""

product_list = ['Laptop', 'Phone', 'Printer', 'Headset', 'Monitor']
del product_list[2]
product_list.insert(2, "Tablet")
print(product_list)
