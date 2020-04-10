import os
from room import Room
import player
import item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),
    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),
    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),
    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
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

backpack = item.Item('backpack', 'something to hold your treasure.')
socks = item.Item('socks', 'nothing like a fresh pair of socks (freshness not guaranteed).')
gloves = item.Item('gloves', 'gotta keep those hands clean.')
toothbrush = item.Item('toothbrush', 'fresh breath is all you need.')

room['outside'].items = [backpack, socks, gloves, toothbrush]
room['foyer'].items = [socks, gloves]
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
character = player.Character('Mr. Gump', room['outside'])
player_action = "\n\tActions:\n\t[N] North\n\t[E] East\n\t[S] South\n\t[W] West\n\t[Q] Quit\n\t--------\n\t"
cant_move = "You are blocked from heading that direction.\n"

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
os.system('clear')
print("\n\n\t", character.current_room.name)
print("\t", character.current_room.description)

if character.current_room.items is not None:
        print('\n\tYou see a lump in the corner of the room and find: \n')
        for item in room['outside'].items:
            # print(f"{item.name} {item.description}")
            print("\t", item.name)

player_direction = input(player_action).lower()

while not player_direction == "q":
    os.system('clear')

    if character.current_room.items is not None:
        print('\n\tYou see a lump in the corner of the room and find: \n')
        for item in room['outside'].items:
            print("\t", item.name)

    if player_direction == 'n':
        if character.current_room.n_to != None:
            character.current_room = character.current_room.n_to
        else:
            print(cant_move)
    elif player_direction == 's':
        if character.current_room.s_to != None:
            character.current_room = character.current_room.s_to
        else:
            print(cant_move)
    elif player_direction == 'e':
        if character.current_room.e_to != None:
            character.current_room = character.current_room.e_to
        else:
            print(cant_move)
    elif player_direction == 'w':
        if character.current_room.w_to != None:
            character.current_room = character.current_room.w_to
        else:
            print(cant_move)
    elif 'inventory' in player_direction:
        print('\n\tHere is your inventory:\n')
        for i in character.inventory:
            print(f"\t{i.name}")

    elif 'get' in player_direction:
        to_get = player_direction.split(" ", 1)[1]
        # add to inventory
        item_in_inventory = [True for x in character.inventory if x.name == to_get]
        if item_in_inventory != True:
            """ Add item to character inventory """
            for x in character.current_room.items:
                if to_get in x.name:
                    character.add_item(x)
                    item_index = character.current_room.items.index(x)
                    character.current_room.items.pop(item_index)
            """ Remove item from room """
            
        else:
            print('how did you find that?')

        print('\n\tYou added the', to_get, 'to your backpack')
    elif 'drop' in player_direction:
        to_drop = player_direction.split(" ", 1)[1]
        # remove from inventory
        for x in character.inventory:
            if to_drop in x.name:
                character.drop_item(x)
                # add to room
                character.current_room.items.append(x)

        print('\n\tYou just dropped ', to_drop)
    elif 'look' in player_direction:
        """ See what items are hiding somewhere in the room """
        for i in character.current_room.items:
            item.display_item(i)
    else:
        print('\n\tYou spin in circles not knowing which direction to go.\n')

    print("\n\n\t", character.current_room.name)
    print("\t", character.current_room.description)

    player_direction = input(player_action).lower()

os.system('clear')
