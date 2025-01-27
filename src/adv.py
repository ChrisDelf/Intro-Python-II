from room import Room
from player import Player
from textwrap import wrap
from item import Item
import random

# Items
item =[
    Item("Heavy Sack", "May contain Gold!", "5lbs"),
    Item("Necronomicon", "Very very bad evil book", "2lbs"),
    Item("Rusty Sword", "May cause Tetanus", "4lbs"),
    Item("Lost Cat", "Someone left this here", "6lbs")

]

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", item[1]),

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Adventurer', room['outside'])

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

choices = ['n','s','w','e']
# Write a loop that:
while True:
# * Prints the current room name
    print(f"{player.current_location}")
# * Prints the current description (the textwrap module might be useful here).
    print(wrap(player.current_location.description, 40))


# Checks to see if the room has any loot
    if (player.current_location.room_loot is None):
        print(f"There is no loot in here")
    else:
        print(f"{player.current_location.room_loot.name}")
        print(f"To take this item type `take`")

    cmd = input("->")

    print(f"User input {cmd}")
    if((cmd == 'take')
        and not (player.current_location.room_loot) is None):
            player.get_loot(player.current_location.room_loot)
            print(f"You have taken {player.current_location.room_loot.name}")
    else:
            print(f"there is nothing to take")

    if(cmd == 'inv'):
        player.check_inv()
        # print(f" Your inventory {player.loot.items[0].name}")



# Allows the user to quit the game
    if(cmd == "q"):
        print(f" Quitting the game")
        break
# * Waits for user input and decides what to do.
    if (not hasattr(player.current_location, f"{cmd}_to")
            or getattr(player.current_location, f"{cmd}_to")is None):
                print("Nothing in that direction")
                continue
    player.current_location = getattr(player.current_location, f"{cmd}_to")

    # else:
    #     print(f" Incorrect Command")




