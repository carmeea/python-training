import pprint

# INTEGERS
# Calculate the total number of sales in 3 reports with 30, 45, and 50 pages each.
report1_sales = 30
report2_sales = 45
report3_sales = 50
total_sales = report1_sales + report2_sales + report3_sales
print(f"The total number of pages in the reports is {total_sales}.")

# FLOAT
# Calculate the exchange rate from RON to EUR
amount_ron = 10
exchange_rate = 4.98
amount_eur = amount_ron / exchange_rate
print(amount_eur)  # too many decimals
print(round(amount_eur, 2))  # too many decimals

# STRING
# Create a variable 'product_name' and assign it the name of a product.
# Print a message stating that this product is now available.
product_name = "PRODUCT_1"
print("The " + product_name + " is now available for purchase")
print(f"The {product_name} is now available for purchase!")

# Combine a company name and the year of establishment into one string.
# E.g., company = "Fortech", year = 2003.
company = "Fortech"
year = 2003
message = company + " established in " + str(year)
print(message)

# TYPE CASTING
# Convert a string representing a number into an integer.
number_str = "2500"
converted_nb = int(number_str)
print(converted_nb, type(converted_nb))
converted_nb = float(number_str)
print(converted_nb, type(converted_nb))

# LIST
# Create a list of department names. Print the first and third department names.
departments = ["Human Resources", "Finance", "Marketing", "IT"]
print("First Department:", departments[0])
print("Third Department:", departments[2])

# Make a list of three office locations. Add another location
office_locations = ["Cluj-Napoca", "Brasov"]
office_locations.append("Iasi")
print("Updated Office Locations:", office_locations)

# Replace the second element within the list.
ingredients = ["Carrots", "Apples", "Cheese"]
ingredients[1] = "Chocolate"
print("Updated list:", ingredients)

# TUPLE
# Create a tuple containing the names of three conference rooms.
# Print the entire tuple and the name of the second conference room.
conference_rooms = ("ROOM_1", "ROOM_2", "ROOM_3")
print("Conference Rooms:", conference_rooms)
print("Second Conference Room:", conference_rooms[1])

# Create a tuple with the current year, month, and day (e.g., 2024, 1, 22).
# Print the tuple, then separately print the month.
current_date = (2024, 1, 22)
print("Current Date:", current_date)
print("Current Month:", current_date[1])

# DICTIONARY
# Create a dictionary for an employee with keys 'name', 'age', and 'department'.
# Add new keys and values and print the new dictionary.
employee = {"name": "John Doe", "age": 28, "department": "IT"}
print(employee)
employee["email"] = "john.doe@example.com"

pprint.pprint(employee)

# Change Jon's age
employee["age"] = 29
pprint.pprint(employee)

# Find out all the keys from the dictionary
print(employee.keys())

# Find out all the values from the dictionary
print(employee.values())
