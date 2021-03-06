from room import Room
from player import Player
from item import Item

import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

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

# adding some items to the game to test
dagger = Item('dagger', 'A slightly rusty dagger.')
pouch = Item('pouch', 'A small leather pouch containing some assorted coins.')
potion = Item('potion', 'A suspicious-looking green potion.')
torch = Item('torch', 'A standard torch.')

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player('Player', room['outside'])
newPlayer.items = [dagger, pouch, potion, torch]

print(newPlayer) # testing to make sure class is working properly via default repr
print(newPlayer.items)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
while True:
    print('\n ********** \n')
    print(f'You are currently at {newPlayer.location}')
    print(f'{newPlayer.location.description}')
    print('\n ********** \n')
    # will try to add some kind of "directions" message or a directions command so these don't pop up every time
    player_input = input('What would you like to do? Use list to find items, north/south/east/west to move. q to quit.').lower()
    # going to implement a more succinct way later as per Jon's feedback, getting the basic version done now
    if player_input == 'list':
        print('The following items are in this room: \n')
        for item in newPlayer.location.items:
            print(f'{item.name}: {item.description}')
    elif player_input == 'north' or player_input == 'n':
        newPlayer.location = newPlayer.location.n_to
        print('Successfully moved north.')
        if newPlayer.location == room['overlook'] or newPlayer.location == room['treasure']:
            print('Cannot go this way! Try another direction.')
            break
    elif player_input == 'south' or player_input == 's':
        newPlayer.location = newPlayer.location.s_to
        print('Successfully moved south.')
        if newPlayer.location == room['outside'] or newPlayer.location == room['narrow']:
            print('Cannot go this way! Try another direction.')
            break
    else:
        print('Cannot go this way! Try another direction.')

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# loop begins here
