"""
Sales Report Processing
You are given the data for quarter sales: sales = [120, 150, 170, 100].
a. Calculate the total sales for the quarter.
b. Calculate the average sales per month.
c. Print both the total and the average, formatted to two decimal places.
"""
total=0
sales = [120, 150, 170, 100]
#a
for x in sales:
    total=total+x
print("Total sales:",total)
#b
print("/n")
average=total/len(sales)
print("Average sales: ",average)
#c
print("Total:",format(total,".2f"),"\nAverage",format(average,".2f"))

"""
Read from input a string with your name.
a. Create a dictionary for you as called 'employee' with department, 
b. Add a new field 'email' with the value 'alice.finance@example.com'.
c. Print the dictionary.
"""

name=input("Type your name: ")
#a
email="alice.finance@example.com"
employee={"name":name,"department":"Sales"}
#b
employee["email"]=email
#c
print(employee,"\n")

"""
Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
a. Print the entire tuple.
b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
c. Print a confirmation message including the name of the booked room.
"""
conferenceRoom=('Aspen', 'Birch', 'Cedar')
#a
print(conferenceRoom)
#b
room=input("Type the number of the room you want to book(0,1,2):")
#c
print("You selected room ", conferenceRoom[int(room)])

"""
Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
b. Update the list and print the updated inventory.
c. Print the list
"""

products=['Laptop', 'Phone', 'Printer', 'Headset', 'Monitor']
#a
i=products.index('Printer')
products.remove('Printer')
print(products)
#b
#products.append('Tablet')
products.insert(i,'Tablet')
print(products)
#c
print(products)