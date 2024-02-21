conference_rooms = ("Aspen","Birch","Cedar")
#a
print(conference_rooms)
#b & c
print("\nWelcome! \nPlease take into consideration that you can select one of our 3 conference rooms:","\n1.",conference_rooms[0],
      "\n2.",conference_rooms[1], "\n3.",conference_rooms[2])
selected_room= input("Please enter the number (1,2 or 3) corresponding to the room you want to book: ")
if selected_room == "1":
    print("You have successfully booked the ",conference_rooms[0]," room")
elif selected_room == "2":
    print("You have successfully booked the ",conference_rooms[1]," room")
elif selected_room == "3":
    print("You have successfully booked the ",conference_rooms[2]," room")
else: print("Invalid input")