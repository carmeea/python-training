# DATA TYPES
"""
Topics covered: 
Basic data types: integer, float, string. 
Type casting concept.
REFERENCE https://www.w3schools.com/python/python_datatypes.asp
"""

# INTEGER
# Numbers with no decimals like -5, -3, 0, 1, 2, etc.
userAge = 20
mobileNumber = 123456789
print("User age:", userAge, "Mobile numer:", mobileNumber)

# FLOAT
# Numbers with decimal parts like  1.234, -0.023, 12.01
userHeight = 1.82
userWeight = 67.2
print("User height:", userHeight, "User weight:", userWeight)

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

# WORKING WITH STRINGS
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

# COUNT(sub, [start,[end]]) - Case sensitive fnction. start & end are optional parameters
# retuns how many times the substring appears in string
string1 = "This is a string"
print(len(string1))  # 16
print(string1.count("s"))  # 3
print(string1.count("s", 4))  # 2
print(string1.count("s", 4, 10))  # 1

# STARTSWITH(prefix, [start,[end]])  - Returns true if string starts with prefix (case sensistive function)
# ENDSWITH(suffix, [start,[end]]) - Returns true if string ends with suffix (case sensistive function)
string2 = "Postman"
print(len(string2))  # 7
print(string2.endswith("man"))  # True
print(string2.endswith("man", 2, 7))  # True, checks from index 2 to 7-1
print(string2.endswith("man", 2, 6))  # False
print(string2.startswith("Post"))  # True
print(string2.startswith("POST"))  # False, case sensitive
print(string2.startswith("stm", 2, 6))  # True, checks from index 2 to 6-1
# Using a tuple of suffixes, check from index 2 to 6-1
print(string2.endswith(("man", "ma"), 2, 6))  # True
# Using a tuple of prefixes, check from index 3 to end of the string
print(string2.startswith(("Post", "tma"), 3))  # True

# FIND(sub, [start,[end]]) or INDEX(sub, [start,[end]])
string3 = "This is a another string"
print(len(string3))  # 24
print(string3.find("s"))  # 3
# returns -1 if not found
print(string3.find("p"))  # -1
# check from index 7 to end of the string
print(string3.find("s", 7))  # found on index number 18, index starts from 0
# check from index 4 to 19-1
print(string3.find("s", 4, 19))  # found on index 6
# find first ocurrance and retun index number
print(string3.index("s"))  # 3
# returns Value error if substring not found
print(string3.index("p"))  # ValueError: substring not found

# ISALNUM() - all chars in a string are alphanumeric
string4 = "abcd1234"
string5 = "a b c d 1 2 3 4"
string6 = "abcd"
print(string4.isalnum())  # True
print(string5.isalnum())  # False
print(string6.isalnum())  # True

# ISALPHA() - all chars in a string are alphabetic and there is at least 1 char
string7 = "abcd"
string8 = "a b c d"
string9 = "abcd1234"
print(string7.isalpha())  # True
print(string8.isalpha())  # False
print(string9.isalpha())  # False

# ISDIGIT() - all chars in a string are alphabetic and there is at least 1 char
string10 = "1234"
string11 = "1 2 3 4"
string12 = "abcd1234"
print(string10.isalpha())  # True
print(string11.isalpha())  # False
print(string12.isalpha())  # False

# ISLOWER() - true if all chars are lowercased and len>=1
# ISUPPER() - true if all chars are uppercased and len>=1
# ISTITLE() - true if all chars are titlecased and len>=1
string13 = "abcd"
string14 = "ABCD"
string15 = "Abcd Is A String"
print(string13.islower())  # True
print(string14.isupper())  # True
print(string15.islower())  # False
print(string15.isupper())  # False
print(string15.istitle())  # True

# ISSPACE() - True if string has only white space values & len>=1
string16 = "     "
string17 = "a   b"
print(string16.isspace())  # True
print(string17.isspace())  # False

# LOWER() - convert to lowercase
# UPPER() - convert to uppercase
string19 = "Abcd Is Another String"
print(string19.lower())  # abcd is another string
print(string19.upper())  # ABCD IS ANOTHER STRING

# JOIN() - returns a string
separ1 = "."
separ2 = "xxx"
myTupple = ("a", "b", "c")
myList = ["d", "e", "f"]
myString = "GHI"
print(separ1.join(myTupple))  # a.b.c
print(separ1.join(myList))  # d.e.f
print(separ2.join(myString))  # GxxxHxxxI

# REPLACE(old, new[,count]) - return a copy of the string with changes made
string20 = "Abcd Is Another Alphabetic String"
print(string20.replace(" ", "-"))  # Abcd-Is-Another-Alphabetic-String
# Replace first 2 occurences
print(string20.replace(" ", "-", 2))  # Abcd-Is-Another Alphabetic String

# SPLIT([step [,maxsplit]]) - return
string21 = "Abcd Is Just Another Alphabetic String"
string22 = "Abcd,Is,Just,Another,Alphabetic,String"
print(string21.split())  # Whitespace delimiter

# STRIP([chars]) - returns a copy of string. removes substring if found, in the beginning and end of string
string23 = "      This Is Just Another Alphabetic String    "
string24 = ".This Is Just Another Alphabetic String."
print(string23.strip())  # removes white spaces at the beginning and end
print(string23.strip("."))  # This Is Just Another Alphabetic String
