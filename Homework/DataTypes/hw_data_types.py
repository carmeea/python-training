"""
Sales Report Processing
You are given the data for quarter sales: sales = [120, 150, 170, 100].
a. Calculate the total sales for the quarter.
b. Calculate the average sales per month.
c. Print both the total and the average, formatted to two decimal places.
"""

sales = [120, 150, 170, 100]
total_sales = 0
average_sales = 0

for i in sales:
    total_sales = total_sales + i

average_sales = total_sales / len(sales)

print(f"The sales for the whole quarter are: {total_sales:.2f}.")
print(f"For this quarter the average sales/month are: {average_sales:.2f}.")

"""
Read from input a string with your name.
a. Create a dictionary for you as called 'employee' with department, 
b. Add a new field 'email' with the value 'alice.finance@example.com'.
c. Print the dictionary.
"""
employeeName = input("Please enter an employee name:")
employeeDict = {"name": employeeName}
employeeDict["email"] = "alice.finance@example.com"
print(employeeDict)

"""
Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
a. Print the entire tuple.
b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
c. Print a confirmation message including the name of the booked room.
"""

conferenceRooms = ("Aspen", "Birch", "Cedar")
print("Please give me the number of the room you wish to book, given the following:")

for i in conferenceRooms:
    print(
        f"number {conferenceRooms.index(i)+1} corresponds to room the following conference room: {i}"
    )

bookedRoom = input("Guest input: ")

while bookedRoom not in ["1", "2", "3"]:
    print("Error! Wrong conference room number, please try again!")
    bookedRoom = input("Guest input: ")

print(
    f"You selected room number {bookedRoom}, named {conferenceRooms[int(bookedRoom)-1]}"
)


"""
Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
b. Update the list and print the updated inventory.
c. Print the list
"""

devices = ["Laptop", "Phone", "Printer", "Headset", "Monitor"]
devices.remove("Printer")
devices.append("Tablet")

print("updated inventory is:")
for device in devices:
    print(device)

print(f"The list is:{devices}")
