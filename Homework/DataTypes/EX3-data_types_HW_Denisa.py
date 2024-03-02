conference_rooms = ("Aspen","Birch","Cedar")
#a
print(conference_rooms)
#b & c
print("\nWelcome! \nPlease take into consideration that you can select one of our 3 conference rooms:","\n1.",conference_rooms[0],
      "\n2.",conference_rooms[1], "\n3.",conference_rooms[2])
selected_room= int(input("\nPlease enter the number (1,2 or 3) corresponding to the room you want to book: "))
if 1 <= selected_room <= len(conference_rooms):
    booked_room = conference_rooms[selected_room - 1]
    print(f"Room {selected_room} {booked_room} has been booked.")
else:
    print("Invalid room number. Please enter a number between 1 and 3.")