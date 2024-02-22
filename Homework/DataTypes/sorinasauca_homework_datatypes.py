"""
Sales Report Processing
You are given the data for quarter sales: sales = [120, 150, 170, 100].
"""
#a. Calculate the total sales for the quarter.
sales = [125,150,170,100]
totalsales = (sum(sales))
print(f"The total sales of the quarter are {totalsales}")

#b. Calculate the average sales per month.
monthaverage = totalsales/len(sales)
print("Average sales per month is ",(monthaverage))

#c. Print both the total and the average, formatted to two decimal places.
print("The total sales of the quarter are ")
print(round(totalsales, 2)) 
print("The average sales per month is: ")
print(round(monthaverage,2))

"""
Read from input a string with your name.
"""
#input is not working for me, the program do not stop to enter the name, don't know how to fix
name =  input ("Enter your name: ")
#a. Create a dictionary for you as called 'employee' with department
dictionary = {"employee" : name,"department": "QA"}
print (dictionary)
employee = {"name": "John Doe", "age": 28, "department": "IT"}

#b. Add a new field 'email' with the value 'alice.finance@example.com'.
dictionary["email"] = "alice.finance@example.com"

#c.Print the dictionary.
print (dictionary)


"""
Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
"""

conferenceRooms = ["Aspen","Birch","Cedar"]
#a. Print the entire tuple.
print (conferenceRooms)

#b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
#input is not working for me, the program do not stop to enter the name, don't know how to fix
roomToBook = input("Please enter the room you want to book (1, 2 or 3): ")
1
roomToBook = int(roomToBook)

#c. Print a confirmation message including the name of the booked room.
print ("The room " + conferenceRooms[roomToBook] + " was successfully booked")


"""
Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
"""

products = ["Laptop", "Printer", "Headset", "Monitor"]
inventory = products[0:4]
#a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
del inventory[0]

#b. Update the list and print the updated inventory.
inventory.append("Tablet")
print (f"The updated inventory is {inventory}")

#c. Print the list
print (f"The initial product list is {products}")