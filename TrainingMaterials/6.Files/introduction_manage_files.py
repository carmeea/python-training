# Manage FILES


# Opening and Reading files
"""
Before reading from a file, first you must open it.
open() - requires 2 parameters, param1 -> path to file, param2 -> access mode
'r' mode: read only
'w' mode: writing only. If file doesn't exit will be created, if it exists data in the file will be erased
'a' mode: for appending. If file doesn't exit will be created, if it exists data written to the file will automatically be added at the end.
'r+' mode: reading and wrinting
readline() - each time function is called, it reads a new line and adds at the end '\n' to the end of each line.


"""

# Opening a file in the same dirtectory
f1 = open("myTextFile.txt", "r")
firstLineF1 = f1.readline()
secondLineF1 = f1.readline()
print(firstLineF1)
print(secondLineF1)

print(firstLineF1, end="")  # remove the \n at the end of the line
print(secondLineF1)
f1.close()  # close the file to free up any system resources

# Opening a file in the Parent Directory
f2 = open("../myTextFile2.txt", "r")
firstLineF2 = f2.readline()
print(firstLineF2)
f2.close()

# Opening a file in another location


# Using For Loop to Read Text files
f3 = open("myTextFile.txt", "r")
for line in f3:
    print(line, end="")
f3.close()

# Writing to a text file
"""
'w' mode will ovewrite the file
'a' mode will add
"""
f = open("myTextFile.txt", "a")
f.write("\nThis string will be added")
f.write("\nPython can be fun")
f.close()

# Opening and Reading Text Files by Buffer size
"""
read() - reading a file by buffer size so that the program does not take too much memory resources
"""
print("\nCheck myOutputFile.txt")
inputFile = open("myTextFile.txt", "r")
outputFile = open("myOutputFile.txt", "w")
msg = inputFile.read(10)
# Loop until the etire file is read, 10 bytes at a time
while len(msg):
    outputFile.write(msg)
    # outputFile.write(msg + "\n") # to prove only 10 bytes is read at a time
    msg = inputFile.read(10)
inputFile.close()
outputFile.close()

# Opening, Reading and Writing Binary Files
"""
Binary files refers to any file that contains non-text (image, videos, etc)
'rb' & 'wb' mode for binary files
"""
inputFile = open("myImage.jpg", "rb")
outputFile = open("myOutputImage.jpg", "wb")
msg = inputFile.read(10)
while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10)
inputFile.close()
outputFile.close()

# Deleting and Renaming Files
"""
remove(), rename() - are available in the os module
"""
import os

os.rename("myOutputFile.txt", "myOutputFileRenamed.txt")
os.rename("myOutputImage.jpg", "myOutputImageRenamed.jpg")
os.remove("myOutputFile.txt")
os.remove("myOutputImage.jpg")
