# ADVANCE DATA TYPES
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

# APPEND()
# Add to list
userAgeList.append(99)
print(userAgeList)  # [16, 19, 20, 37, 39, 40, 42, 53, 66, 71, 99]

# LEN
# Retrieve number of items in a list
print(len(userAgeList))  # 11

# POP()
# Get value of an item and remove from list. Requires index of item as parameter
userAgeList6 = [16, 19, 20, 37]
age = userAgeList6.pop(2)
print(age)  # 20
print(userAgeList6)  # [16, 19, 37]

# DEL
# Delete from list
del userAgeList[-1]
print(userAgeList)
# Deletes item with index 7, meaning item 8 in list, list always starts with index 0
del userAgeList[len(userAgeList) - 3]
print(userAgeList)
# Delete ites from index 1 to 5-1
myListAlf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
del myListAlf[1:5]
print(myListAlf)  # ['a', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
# Delete items from index 0 to 3-1
del myListAlf[:3]
print(myListAlf)
# Delete items from index 2 to end
del myListAlf[2:]
print(myListAlf)

# EXTEND()
myListAlf1 = ["a", "b", "c", "d", "e"]
myListNum1 = [1, 2, 3, 4]
myListAlf1.extend(myListNum1)
print(myListAlf1)  # ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4]

# IN
# Check if item included in a list
print("c" in myListAlf1)  # True
print("f" in myListAlf1)  # False

# INSERT()
# Add items to a list at particular position index
myListAlf1.insert(1, "Hi")  # position 2
print(myListAlf1)  # ['a', 'Hi', 'b', 'c', 'd', 'e', 1, 2, 3, 4]

# REMOVE()
myListAlf2 = ["a", "b", "c", "d", "e", "A", "B", "C"]
myListAlf2.remove("c")
print(myListAlf2)  # ['a', 'b', 'd', 'e', 'A', 'B', 'C']

# REVERSE()
myListAlf2.reverse()
print(myListAlf2)  # ['C', 'B', 'A', 'e', 'd', 'b', 'a']

# SORT()
myListAlf2.sort()
print(myListAlf2)  # ['A', 'B', 'C', 'a', 'b', 'd', 'e']

# SORTED()
# Return a new sorted list without sorting the original list
myListNum2 = [7, 5, 2, 0, -3, 3]
myListNum3 = sorted(myListNum2)
print(myListNum3)  # [-3, 0, 2, 3, 5, 7]
print(myListNum2)  # [7, 5, 2, 0, -3, 3]

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
