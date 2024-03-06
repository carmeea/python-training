# Create a function which prints first 10 natural numbers
def show_first_ten_natural_numbers():
    for i in range(1, 11):
        print(i)


show_first_ten_natural_numbers()

# Create a function which prints sum of all numbers from 1 to a given number (e.g. print sum of all numbers from 1 to 5)


# Create a function with 3 arguments and return average only if is greater than 0
def calculate_average(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    if average > 0:
        return average
    else:
        return None


result = calculate_average(6, 2, 22)
if result is not None:
    print(f"The average is: {result}")
else:
    print("The average is 0.")


# Create a function with a default argument value
def print_hello_word(message="Hello, world!"):
    print(message)


print_hello_word()


# Create a function which accepts 3 values and return the maximum value
def show_maximum_value(num1, num2, num3):
    return max(num1, num2, num3)


maximum_value = show_maximum_value(28, 19, 60)
print(f"The maximum value is: {maximum_value}")


# Define a function which ask the user for a number and print “Even” if the number is even or “Odd” if the number is odd
def check_number_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


result1 = check_number_even_or_odd(17)
print(f"Number 17 is: {result1}")

result2 = check_number_even_or_odd(22)
print(f"Number 22 is: {result2}")


# Define a function that accepts 2 values and print its sum, subtraction and multiplication
def calculate_mathematical_operations(num1, num2):
    print(f"Sum is: {num1 + num2}")
    print(f"Substraction is: {num1 - num2}")
    print(f"Multiplication is: {num1 * num2}")


calculate_mathematical_operations(3, 8)

# Create a variable with values [‘Siya’, ‘Tiya’, ‘Guru’, ‘Daksh’, ‘Riya’, ‘Guru’] and return “Guru”

names = ["Siya", "Tiya", "Guru", "Daksh", "Riya", "Guru"]
found_name = names[2]
print(found_name)

# Assign an integer to a variable, then print it

num1 = 40
print(f"My number is: {num1}")

# Type a couple of words or a short sentence in a variable, then print it

my_sentence = "Hi, world!"
print(f"My sentence is: {my_sentence}")

# Assign a float with 2 decimals to a variable

my_float_number = 2.50
print(f"My float number is: {my_float_number}")

# Assign True or False to a variable then print it
is_true = True
print(is_true)

# Calculate the length of a string and return that value

my_string = "I'm Andreea"
print(f"My string length is: {len(my_string)}")

# Get the largest and the smallest number from a list

my_list_of_numbers = [1, 5, 46, 987, 25]
print(f"My largest number is: {max(my_list_of_numbers)}")
print(f"My smallest number is: {min(my_list_of_numbers)}")

# Assign 3 to variable glass_of_water, print "I drank 3 glasses of water today." and after that assign a new value to our variable. Print the result

glass_of_water = 3
print(f"I drank {glass_of_water} glasses of water today.")
glass_of_water = 5
print(f"Now, I have {glass_of_water} glasses of water.")

# Given a tuple, use a range of indexes to print the third, fourth, and fifth item in the tuple

my_tuple = (1, 5, 78, 46, 63, 134, 200)
print(my_tuple[2:5])

# Given a dictionary, add a new key/value to the dictionary and print each item

my_dict = {"num1": 1, "num2": 10, "num3": 27}
my_dict["num4"] = 45
for key, value in my_dict.items():
    print(key, value)
