from room import Room
from player import Player
from item import Food, Item, Egg
# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


rock = Item("rock", "This is a rock")
sandwich = Food("sandwich", "This is a delicious sandwich", 100)
stick = Item("stick", "This is a stick")
log = Item("log", "This is a log")
cake = Food("Cake", "This is a cake", 50)
sword = Item("sword", "This is a sword")

room['outside'].items.append(rock)
room['foyer'].items.append(stick)
room['foyer'].items.append(log)
room['foyer'].items.append(rock)
room['treasure'].items.append(cake)
room['treasure'].items.append(sandwich)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# fae
# If the user enters "q", quit the game.


adventurer = Player(input("Enter your name "), room['outside'])


print(f"Welcome to the Cave {adventurer.name}press q to quit")
print(f"{adventurer.current_room}")


adventurer.items.append(sword)



valid_directions = ("n", "s", "e", "w")

while True:
    cmd = input("\n~~> ")
    if cmd == "q":
        print("Goodbye!")
        exit(0)
    elif cmd in valid_directions:
        adventurer.travel(cmd)
    elif cmd == "i":
        adventurer.print_inventory()
    elif cmd == "search":
        adventurer.current_room.print_available_items()
    elif cmd == "p":
        adventurer.get_item(adventurer.current_room.items)
    elif cmd == "d":
        adventurer.drop_item(adventurer.items)
    elif(cmd == 'take'):
        player_input = input("\n~~> Enter Item name ")
        adventurer.get_specific_item(adventurer.current_room.items, player_input)
    elif(cmd == 'drop'):
        player_input = input("\n~~> Enter Item name ")
        adventurer.drop_specific_item(adventurer.items, player_input)
    
    else:
        print("invalid command")


# while True:

#     print(f"{adventurer.current_room.description}. Enter a direction (n,s,w,e) or q to quit")

#     cmd = input("->")
#     # quiting
#     if cmd == "q":
#         print("You have quit")
#         break
#     if not hasattr(adventurer.current_room, f"{cmd}_to"):
#         print("invalid command")
#         continue
#     elif getattr(adventurer.current_room, f"{cmd}_to") is None :
#         print("you cant go there")
#         continue

#     adventurer.current_room = getattr(adventurer.current_room, f"{cmd}_to")
