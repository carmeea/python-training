# Making your PROGRAM INTERACTIVE

"""
To make your program interactive we can use two built-in functions: 
input() - provides option to interact with input console
print() - print messages
"""

myName = input("Please enter your name: ")
myAge = input("Please enter your age: ")
print("Your name is", myName, "and you are", myAge, "years old.")
# Print statement using % formatter
print("Your name is %s and you are %s years old." % (myName, myAge))
# Print statement using format()
print("Your name is {} and you are {} years old.".format(myName, myAge))

print("Hello\tWorld")  # add tab between words
print(r"Hello\tWorld")  # raw string to not interpret special chars
print("Hello\nWorld")  # print words on separate lines
print("\\")  # print backslash
print("I am 5'9\" tall")  # print double quotes & not signal end of string
