"""
Sales Report Processing
You are given the data for quarter sales: sales = [120, 150, 170, 100].
a. Calculate the total sales for the quarter.
b. Calculate the average sales per month.
c. Print both the total and the average, formatted to two decimal places.
"""
sales = [120, 150, 170, 100]

totalSales = sum(sales)
avgSales = totalSales/12
print("%.2f" % totalSales)
print("%.2f" % avgSales)

"""
Read from input a string with your name.
a. Create a dictionary for you as called 'employee' with department, 
b. Add a new field 'email' with the value 'alice.finance@example.com'.
c. Print the dictionary.
"""
name = input ("Write your name: ")
employee = {"name" : name, "department" : ""}
employee["email"] = "alice.finance@example.com"
print(employee)
"""
Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
a. Print the entire tuple.
b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
c. Print a confirmation message including the name of the booked room.
"""
conferenceRooms = ("Aspen", "Birch", "Cedar")

print("The conference rooms are:", conferenceRooms)

chooseRoom = int(input("Choose one of the 3 rooms (0-2): "))

try:
    chosenRoom = conferenceRooms[chooseRoom]
    print("You chose the room:", chosenRoom)
except KeyError:
    print("The number you introduced doesn't exist")
"""
Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
b. Update the list and print the updated inventory.
c. Print the list
"""
productsList = ['Laptop', 'Phone', 'Printer', 'Headset', 'Monitor']
del productsList[2]
productsList.insert(2, 'Tablet')
print(productsList)