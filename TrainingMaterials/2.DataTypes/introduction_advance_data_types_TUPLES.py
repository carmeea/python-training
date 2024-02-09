# ADVANCE DATA TYPES
# TUPLES
"""
Are like list, but you can't modify values. Good example would be storing month namings.
Individual values are accessed using index
"""
monthsOfYear = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
)
print(monthsOfYear[0])  # Jan
print(monthsOfYear[-1])  # Dec

# Delete entire tuple
myTuple = ("a", "b", "c", "d")
print(myTuple)
del myTuple
print(myTuple)  # NameError: name 'myTuple' is not defined

# Check item exists in tuple
myTuple1 = ("a", "b", "c", "d")
print("c" in myTuple1)  # True
print("e" in myTuple1)  # False

# Retrieve the number of items in a tuple
myTuple2 = ("a", "b", "c", "d", "e")
print(len(myTuple2))

# Concatenate Tuples
print(myTuple2 + ("f", "g"))
print(myTuple2)  # initial tuple items remain the same

# Duplicate a tuple and concatenate at the end of the tuple
print(myTuple2 * 3)
