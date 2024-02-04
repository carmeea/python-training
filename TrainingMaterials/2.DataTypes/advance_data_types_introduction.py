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
