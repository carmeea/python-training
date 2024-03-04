"""
Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
a. The company has decided to remove 'Printer' from the inventory and add 'Tablet'.
b. Update the list and print the updated inventory.
c. Print the list
"""

listProducts = ["Laptop", "Phone", "Printer", "Headset", "Monitor"]
inventory = []
inventory.extend(listProducts)
inventory.remove("Printer")
inventory.append("Tablet")
listProducts = inventory
print("Updated inventory is: ", inventory)
print("Updated list is: ", listProducts)
