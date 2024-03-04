"""
Read from input a string with your name.
a. Create a dictionary for you as called 'employee' with department, 
b. Add a new field 'email' with the value 'alice.finance@example.com'.
c. Print the dictionary.
"""

import pprint

myName = input("Please enter your name: ")
employee = {"name": myName, "department": "div 5-6"}
employee["email"] = "alice.finance@example.com"
# print("The dictionary is: ", employee)
pprint.pprint(employee)
