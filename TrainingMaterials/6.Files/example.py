# Your example here

# Open a file and read its contents
with open('example.txt', 'r') as file:
    contents = file.read()
    print(contents)

# Question - what do you think r it s?

# Read a file line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Write a message to a file
with open('output.txt', 'w') as file:
    file.write('Hello, world!')

# Append a message to a file
with open('output.txt', 'a') as file:
    file.write('\nGoodbye, world!')

#Guestion , whats the output for line 21 ?

# working with Json
import json

# Read JSON data from a file
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)

# Modify the data
data['new_key'] = 'new_value'

# Write the modified data back to the file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)


# Use Exception Handling
try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


# Specify the absolute path to the file
file_path = '/path/to/your/file/example.txt'  # Change this to your file's actual path

# Open the file and read its contents
with open(file_path, 'r') as file:
    contents = file.read()
    print(contents)


# Specify the relative path to the file
file_path = '../data/example.txt'  # Relative to the location of your Python script

# Open the file and read its contents
with open(file_path, 'r') as file:
    contents = file.read()
    print(contents)
