# DATA TYPES
"""
Topics covered: 
Basic data types: integer, float, string. 
Type casting concept.
Advance data types: list, tuple, dictionary
REFERENCE https://www.w3schools.com/python/python_datatypes.asp
"""

# Integers
# Numbers with no decimals like -5, -3, 0, 1, 2, etc.
userAge = 20
mobileNumber = 123456789
print("User age:", userAge, "Mobile numer:", mobileNumber)

# Float
# Numbers with decimal parts like  1.234, -0.023, 12.01
userHeight = 1.82
userWeight = 67.2
print("User height:", userHeight, "User weight:", userWeight)

# String
# REFERENCE https://www.w3schools.com/python/python_strings.asp
# Refers to text
userName = "O'Brian"
userSurname = "Peter"
userAge2 = "30"
print("User name:", userName, "User surname:", userSurname)
print("User age:", userAge2)
print("Peter" + "Lee")

# Built-in String Functions
print("Peter".upper())
print("Peter".lower())
print(len("Peter"))

# FORMATTING TRINGS
# Formatting Strings using % Operator
"""
Control over how you want your string to be displayed and stored.
Syntax: "String to format" % (values or variables to be inserted into string, separated by commas)
%s, %d, %4,2f  formatters used as placehoders in string
%4,2f - %f used to format floats, 4 - total length, 2 - refers to 2 decimal places
ToDo: 
Replace %d with %5d - adds an extra space within the string, 5 length string replaced
Replace %4.2f with %7.2 for extra spaces
"""
brand = "Apple"
price = 1299
exchangeRate = 1.2352235445
message = "The price of this %s is %d USD and exchage rate is %4.2f USD to 1 EUR" % (
    brand,
    price,
    exchangeRate,
)
print(message)

# Formatting Strings using format() method
"""
Syntax:
message = "The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR".format('Apple',1299,1.2352235445)
format('Apple',1299,1.2352235445) - format method with 3 params
position of parameters start with 0
"""
messageFormat = "The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR".format(
    "Apple", 1299, 1.2352235445
)
print(messageFormat)
# Following example does not format string
messageNoFormat = "The price of this {} laptop is {} USD and the exchange rate is {} USD to 1 EUR".format(
    "Apple", 1299, 1.2352235445
)
print(messageNoFormat)

# Other Examples
message1 = "{0} is easier than {1}".format("Python", "Java")
print(message1)
message2 = "{1} is easier than {0}".format("Python", "Java")
print(message2)
message3 = "{:10.2f} and {:d}".format(1.2352235445, 12)
print(message3)
message4 = "{}".format(1.2352235445)
print(message4)

# TYPE CASTING
"""
Coverting one data to another known as type casting.
There are built-in functions for type casting int(), float(), str()
int() - converts float to integer / int("Hello"), int("4.22321") - returns error
float() - integer into float
str() - integer/float to string
"""
print(int(5.712987))
print(int("4"))
print(float(2))
print(float("2"))
print(float("2.09109"))
print(str(2.1))

# ADVANCE DATA TYPE
# LIST
"""
Store multiple values in a list, instead of using alocating memory for multiple variables
append() - add items to list
del listname[index] - remove from list
"""
listName = []  # declare an empty list
userAge = [21, 22, 23, 24, 25]
print(userAge[0], userAge[2])
# List last 2 items in list
print(userAge[-1], userAge[-2])
userAge2 = userAge
print(userAge2)
# Assign partial list (a slice), following example goes from index 2 to 4-1
userAge3 = userAge[2:4]
print(userAge3)

# 3rd value in slicer is called stepper
# in following example index 1 to index 5-1, every 2 numbers
userAge4 = userAge[1:5:2]
print(userAge4)
userAgeList = [16, 19, 20, 37, 39, 40, 42, 53, 66, 71]
userAge5 = userAgeList[2:11:3]
print(userAge5)

# Add to list
userAgeList.append(99)
print(userAgeList)
# Delete from list
del userAgeList[-1]
print(userAgeList)
# Deletes item with index 7, meaning item 8 in list, list always starts with index 0
del userAgeList[len(userAgeList) - 3]
print(userAgeList)

# OTHER LIST EXAMPLES
# List can have different values
myList = [1, 2, 3, 5, 0, "Hello"]
print(myList)
# Print 3rd item
print(myList[2])
# Print last item
print(myList[-1])
# Assign parial list to another list, from idex 1 to 4
myList2 = myList[1:5]
print(myList2)
# Modify second item in list
myList[1] = 20
print(myList)
# Add item to list
myList.append("Hello World")
print(myList)
# Remove 6th item
del myList[5]
print(myList)
