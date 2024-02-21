# Sales Report Processing
#   You are given the data for quarter sales: sales = [120, 150, 170, 100].
#       a. Calculate the total sales for the quarter.
#       b. Calculate the average sales per month.
#       c. Print both the total and the average, formatted to two decimal places.
sales = [120,150,170,100]
i=0
totalSales=0
avgSales=0
for i in sales:
    totalSales+=i
avgSales=totalSales/len(sales)
print ("Total sales for the quarter are "+str(totalSales))
print ("Average sales per month are "+str(avgSales))
print ("Total and average sales rounded with 2 decimal places are "+'%.2f'%totalSales +" and " +'%.2f'%avgSales)
###
###
###
# Read from input a string with your name.
# a. Create a dictionary for you as called 'employee' with department, 
# b. Add a new field 'email' with the value 'alice.finance@example.com'.
# c. Print the dictionary.
name=input("My name is ")
employee={"department":"My department","name":name}
employee["email"]="alice.finance@example.com"
employee ["phone"]= '07254685324', '06515915159' # optional, 2 numere de telefon asignate aceluiasi user
print (employee)
###
###
###
# Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
# a. Print the entire tuple.
# b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
# c. Print a confirmation message including the name of the booked room.
conferenceRoom = ("Aspen", "Birch", "Cedar")
print(conferenceRoom)
value = int(input("Choose a room to book: "))
if value in [1, 2, 3]:
    room = conferenceRoom[value-1]  #listele incep de la 0 nu de la 1, de asta e value-1
    print("You booked the "+room+" room.")
else:
    print("Please enter 1, 2 or 3")
###
###
###
# Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
# a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
# b. Update the list and print the updated inventory.
# c. Print the list
list = ["Laptop", "Phone", "Printer", "Headset", "Monitor"]
i=len(list)
list.remove("Printer")
list.insert(i-1,"Tablet")
print(list)

