# ADVANCE DATA TYPES
# DICTIONARY
"""
Collection of a related data pairs key-value
Declaration: dictionaryName = {dictionaryKey : data}
Declare empty dictionary: dictionaryName = {}
Modify items in a dictionary: dictionaryName[dictionaryKey] = newValue
Delete item in dictionary: del dictionaryName[dictionaryKey]
dict is a reserved name
"""
myDictionary = {"Peter": 38, "John": 51, "Alice": 13}

# DICT()
# another way to declare dictionaries
userNameAge = dict(Peter=38, John=51, Alice=13, Alvin="Not Available")
print(userNameAge)  # {'Peter': 38, 'John': 51, 'Alice': 13, 'Alvin': 'Not Available'}
# Access Items in Dictionary by key
print(userNameAge["John"])  # 51
# Modify Item value
userNameAge["John"] = 58
print(userNameAge["John"])  # 58
# Add item to dictionary
userNameAge["Joe"] = 40
print(
    userNameAge
)  # {'Peter': 38, 'John': 51, 'Alice': 13, 'Alvin': 'Not Available', 'Joe': 40}
# Delete items in dictionary
del userNameAge["Joe"]
print(userNameAge)  # {'Peter': 38, 'John': 51, 'Alice': 13, 'Alvin': 'Not Available'}

# CLEAR()
# Removes all elements in a dictionary
dict1 = {1: "one", 2: "two", 3: "three"}
print(dict1)
dict1.clear()  # {1: 'one', 2: 'two', 3: 'three'}
print(dict1)  # {}

# DEL
# Delete entire dictionary
del dict1
print(dict1)  # NameError: name 'dict1' is not defined.

# GET()
# Return value from given key. If key is not found, return None
dict2 = {1: "one", 2: "two", 3: "three", 4: "four"}
print(dict2.get(1))  # One
print(dict2.get(5))  # None
# State the value to return if key not found
print(dict2.get(6, "Item not found"))  # Item not found

# IN
# Check if item is in a dictionary
print(1 in dict2)  # True
print(1 in dict2.keys())  # True
print("one" in dict2)  # True
print("one" in dict2.values())  # True

print(5 in dict2)  # False
print(5 in dict2.keys())  # False
print("Five" in dict2)  # False
print("Five" in dict2.values())  # False

# ITEMS()
# Returns list of dictionary pairs as tuples
dict3 = {1: "one", 2: "two", 3: "three"}
print(dict3.items())  # dict_items([(1, 'one'), (2, 'two'), (3, 'three')])

# KEYS() & VALUES()
print(dict3.keys())  # dict_keys([1, 2, 3])
print(dict3.values())  # dict_values(['one', 'two', 'three'])

# LEN()
# Number of items in a dictionary
print(len(dict3))  # 3
print(len(dict2))  # 4

# Update()
# Add one dictionary to another.
# Duplicates key-value are removed.
dict4 = {1: "one", 2: "two"}
dict5 = {1: "one", 3: "three", 4: "four"}
dict4.update(dict5)
print(dict4)  # {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

# Duplicated key with different value is updated
dict6 = {1: "one", 2: "two", 3: "threee"}
dict7 = {1: "one", 2: "twoo", 3: "three", 4: "four"}
dict6.update(dict7)
print(dict6)  # {1: 'one', 2: 'twoo', 3: 'three', 4: 'four'}
