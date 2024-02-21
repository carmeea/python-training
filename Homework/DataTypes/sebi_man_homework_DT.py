# Sales Report Processing
sales = [120, 150, 170, 100]
# a.
total_sales = sum(sales)
# b.
number_months = len(sales)
average_sales_per_month = total_sales / number_months
# c.
print("Total Sales: ", total_sales, "\nAverage sales per month: ", average_sales_per_month)

# Read from input a string with your name.
# a. b.
employee = {
    "name": "Sebi Man",
    "department": "QA",
    "email": "alice.finance@example.com"
}
# c.
print(employee)

# Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
# a. 
conference_rooms = ('Aspen', 'Birch', 'Cedar')
print("Conference rooms ", conference_rooms)
# b.
user_choice = input("Please select a conference room(1/2/3): ")
# c.
selected_conference_room = conference_rooms[int(user_choice) - 1]
print("You select the", selected_conference_room, "room")

# Create a list of products: 'Laptop', 'Phone', 'Printer', 'Headset', 'Monitor'.
products = ["Laptop", "Phone", "Printer", "Headset", "Monitor"]
# a. b.
products.remove("Printer")
products.append("Tablet")
#c. 
print("Updated inventory: ", products)