"""
Create a tuple with the names of three conference rooms: 'Aspen', 'Birch', and 'Cedar'.
a. Print the entire tuple.
b. Ask the user to input the number (1, 2, or 3) corresponding to the room they want to book.
c. Print a confirmation message including the name of the booked room.
"""

conference_rooms = ("Aspen", "Birch", "Cedar")
print("Conference Rooms:", conference_rooms)
roomBooked = input(
    "Please let us know what room do you want to book (input a number between 1 and 3): "
)
print(f"The booked room rezerved is ${conference_rooms[int(roomBooked)-1]}.")
