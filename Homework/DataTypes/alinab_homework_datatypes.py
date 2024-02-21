"""
Sales Report Processing
You are given the data for quarter sales: sales = [120, 150, 170, 100].
a. Calculate the total sales for the quarter.
b. Calculate the average sales per month.
c. Print both the total and the average, formatted to two decimal places.
"""
sales = [120, 150, 170, 100]
i = 0
totalSales = 0
average = 0
for i in sales:
    totalSales += i
average = totalSales / len(sales)
print(totalSales)
print('%.2f' % average)



"""
Read from input a string with your name.
a. Create a dictionary for you as called 'employee' with department, 
b. Add a new field 'email' with the value 'alice.finance@example.com'.
c. Print the dictionary.
"""
name = input("your name is:" )
employee = {"department": "Finance", "name": name}
employee["email"] =  "alice.finance@example.com"
print(employee)



"""
Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
a. Print the entire tuple.
b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
c. Print a confirmation message including the name of the booked room.
"""
conference_room = ("Aspen", "Birch", "Cedar")
print(conference_room)
chosen = int(input("choose a room to book: "))
if chosen in [1, 2, 3]:
    room = conference_room[choosen-1]
    print(f"You booked the {room} room")
else:
    print("Please enter 1, 2 or 3")



"""
Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
b. Update the list and print the updated inventory.
c. Print the list
"""

#method 1
products = ["Laptop", "Phone", "Printer", "Headset", "Monitor"]
products.remove("Printer")
products.insert(2, "Tablet")
print(products)

#method 2
products = ["Laptop", "Phone", "Printer", "Headset", "Monitor"]
i = 0
while i < len(products):
    if products[i] == 'Printer':
        products[i] = 'Tablet'
    i += 1
print(products)
