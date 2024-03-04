"""
11. Create a variable with values [‘Siya’, ‘Tiya’, ‘Guru’, ‘Daksh’, ‘Riya’, ‘Guru’] and return “Guru”
"""

my_list = ["Siya", "Tiya", "Guru", "Daksh", "Riya", "Guru"]


def find_name(list, name):
    for i in range(len(list)):
        if list[i] == name:
            print("Found the name " + name + " at position", i + 1)


find_name(my_list, "Guru")
