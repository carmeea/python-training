"""
Sales Report Processing
You are given the data for quarter sales: sales = [120, 150, 170, 100].
a. Calculate the total sales for the quarter.
b. Calculate the average sales per month.
c. Print both the total and the average, formatted to two decimal places.
"""

quarter1_sales = 120
quarter2_sales = 150
quarter3_sales = 170
quarter4_sales = 100


total_sales = quarter1_sales + quarter2_sales + quarter3_sales + quarter4_sales
average_sales = total_sales / 4
print(f"The the total sales {round(total_sales,2)}")


print(round(average_sales, 2))

"""
Read from input a string with your name.
a. Create a dictionary for you as called 'employee' with department, 
b. Add a new field 'email' with the value 'alice.finance@example.com'.
c. Print the dictionary.
"""
mydictionary = {"Employee": "Alice", "Department": "Finance"}
print(mydictionary)

mydictionary["email"] = "alice.finance@example.com"
print(mydictionary)

"""
Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
a. Print the entire tuple.
b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
c. Print a confirmation message including the name of the booked room.
"""

Rooms = (
    "Aspen",
    "Birch",
    "Cedar",
)

print(Rooms)


try:
    roomNumber = int(input("Enter the room number: "))
    print("The selected room is: ", Rooms[roomNumber - 1])
except Exception as e:
    print("Wrong room number ", e)

"""
Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
b. Update the list and print the updated inventory.
c. Print the list
"""

list = ["Laptop", "Phone", "Printer", "Headset", "Monitor"]
list.remove("Printer")
list.append("Tablet")
print(list)
