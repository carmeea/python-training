sales = [120, 150, 170, 100]
total_sales = sales[0] + sales[1] + sales[2] + sales[3]    
print(f"The total number of sales is {total_sales}.")
average_sales = total_sales/4
print(f"The average number of sales per month is {round(average_sales,2)}.")


name = input("Enter your name: ")
print(f"Welcome {name}!")
employee = {"Department": 'IT'}
employee["email"] = 'alice.finance@example.com'
print(employee)


tuplelist = ("Aspen", "Birch", "Cedar")
print(tuplelist)
choice = input("Select room (1,2,3): ")
print("Camera este:",tuplelist[int(choice)-1])

products = ['Laptop', 'Phone', 'Printer', 'Headset', 'Monitor']
products.remove("Printer")
print(products)
products.append("Tablet")
print(products)