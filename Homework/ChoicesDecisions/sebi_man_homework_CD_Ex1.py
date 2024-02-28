numbers = range(1500, 2700)
numbers_list = []
for x in numbers:
    if (x % 5 == 0) & (x % 7 == 0):
        print(x)
        numbers_list.append(x)
        x+=1
    else:
        x+=1

user_input = int(input("Please enter your number: "))
if user_input in numbers_list:
    print(f"{user_input} is in the list")
else:
    print(f"{user_input} is not present in the list")
