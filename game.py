#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from enemies import *
from gameparser import *
import time
import math
import playsound
import threading
from playsound import *
import random

##### Timer for score ######## Marcus
def timeToHurry():
    print('unknown voice: 3 minutes has passed, quick or we are all dead!')
 
 
timer = threading.Timer(180.0, timeToHurry)
timer.start()
 
startingTimer = time.time() #constant please do not touch
 
def getTimer(): #use to get the time taken to finish the game
    usedTime = time.time() - startingTimer
    print(usedTime)
    return usedTime
 
def timeToGrade(usedTime): # converts the time into a grade
    if usedTime <= 60:
        gradeS(usedTime)
        return
    elif usedTime <= 120 and usedTime > 60:
        gradeA(usedTime)
        return
    elif usedTime <= 180 and usedTime > 120:
        gradeB(usedTime)
    elif usedTime <= 240 and usedTime > 180:
        gradeC(usedTime)
    elif usedTime > 240:
        gradeD(usedTime)
 
def gradeS(usedTime):
    print('Time used: ', math.floor(usedTime))
    print('Grade equivilant: S')
    print('unknown voice: Well done! You have shown an amazing performance that no one has ever done!')
    sound_victory_music()
 
def gradeA(usedTime):
    print('Time used: ', math.floor(usedTime))
    print('Grade equivilant: A')
    print('unknown voice: Good job! Impressive skills, you have saved the day!')
 
def gradeB(usedTime):
    print('Time used: ', math.floor(usedTime))
    print('Grade equivilant: B')
    print('unknown voice: Great! The evil has now been eliminated!')
 
 
def gradeC(usedTime):
    print('Time used: ', math.floor(usedTime))
    print('Grade equivilant: C')
    print('unknown voice: Well, we did it at last!')
 
def gradeD(usedTime):
    print('Time used: ', math.floor(usedTime))
    print('Grade equivilant: D')
    print('unknown voice: That was a close one!')

###################################################################
    

def start():
    global current_room
    print("“Where is this place?”…")
    
    print("""The fall through the chambers ceiling was painful enough, but the daunting moment of
realisation that you have now entered an underground structure, matching those you would
have found in Maps and Mummies from Wizards of the Ghost.""")

    while inventory == []:
        exits = []
        print_room(current_room)
        command = menu(exits, current_room["items"], inventory)
        execute_command(command)
        
    current_room = rooms["OS"]


def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string)."""
    
    stringList = ""
    
    # Build the string
    for item in items:
        stringList = stringList + item["name"] + ", "
    
    # Remove the last ", " from the end of the string
    return stringList[:-2]


def print_room_enemies(room):
    if room["enemies"] == []:
        print("\nThere are no ememies in this room\n")

    else:
        enemy = room.get("enemies")
        print("\n")
        print(enemy[0]["description"])
        print("\n")
    

def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names."""
    
    items = room["items"]
    # Check to see if we have items
    if items:
        print ("There is "+list_of_items(items)+" here.\n")
    

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here."."""
    
    # Check to see if we have items
    if items:
        print ("You have "+list_of_items(items)+".\n")


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this)."""
    
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    # Display any items
    print_room_items(room)
    

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads."""
    
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line"""
    
    print("GO " + direction.upper() + " to " + leads_to + ".")

def boss_spawn(enemies): #check if all enemies are dead, opens boss doors
    if (enemy_goblin_on["alive"] and enemy_goblin_oe["alive"] and enemy_goblin_ow["alive"]) == False:
        rooms["OS"] = rooms["Boss"]

def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items"""
    
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    # Loop over room items
    for item in room_items:
        print("TAKE "+item["id"].upper()+" to take "+item["name"])
    # Loop over inv items
    for item in inv_items:
        print("DROP "+item["id"].upper()+" to drop "+item["name"])
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input()."""
    
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    
    global current_room
    
    if is_valid_exit(current_room["exits"],direction):
       current_room = move(current_room["exits"],direction)

    else:
        print("You cannot go there.")


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    
    global current_room
    global inventory
    foundItem = False
    
    for item in current_room["items"]:
        if item["id"] == item_id:
            current_room["items"].remove(item)
            inventory.append(item)
            foundItem = True
    
    if not foundItem:
        print("You cannot take that.")

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    
    global current_room
    global inventory
    foundItem = False
    
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            current_room["items"].append(item)
            foundItem = True
    
    if not foundItem:
        print("You cannot drop that.")
    

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction"."""

    # Next room to go to
    return rooms[exits[direction]]

def random_spawn_item(item):    # This is run before the game starts to spawn items around the map
    random_list = ["ON","NW","N","NE","OW","W","E","OE","SW","S","SE"]
    room_r = random.choice(random_list)
    x = rooms[room_r].get("items")
    x.append(item)
    
# This is the entry point of our program
def main():

    # Spawn items in random rooms
    random_spawn_item(item_hp_ring)
    random_spawn_item(item_gauntlets)
    random_spawn_item(item_armour)
    random_spawn_item(item_potion)
    #pick a weapon
    start()

    # Main game loop
    while True:
        #checks to see if anything needs to be changed
        boss_spawn(enemies)
        # Display game status (room description, inventory etc.)
        print_room_enemies(current_room)
        #combat(current_room)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()


