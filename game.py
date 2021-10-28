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
import sys
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
    #sound_victory_music()
    sys.exit()
 
def gradeA(usedTime):
    print('Time used: ', math.floor(usedTime))
    print('Grade equivilant: A')
    print('unknown voice: Good job! Impressive skills, you have saved the day!')
    sys.exit()
 
def gradeB(usedTime):
    print('Time used: ', math.floor(usedTime))
    print('Grade equivilant: B')
    print('unknown voice: Great! The evil has now been eliminated!')
    sys.exit() 
 
def gradeC(usedTime):
    print('Time used: ', math.floor(usedTime))
    print('Grade equivilant: C')
    print('unknown voice: Well, we did it at last!')
    sys.exit()
 
def gradeD(usedTime):
    print('Time used: ', math.floor(usedTime))
    print('Grade equivilant: D')
    print('unknown voice: That was a close one!')
    sys.exit()

###################################################################
    

def start():
    global current_room
    print(r"""

======================================================================================================
______                         _     _       _          _   _             __       _                  
|  _  \                       | |   (_)     | |        | | | |           / _|     | |                 
| | | |___  ___  ___ ___ _ __ | |_   _ _ __ | |_ ___   | |_| |__   ___  | |_ _   _| |_ _   _ _ __ ___ 
| | | / _ \/ __|/ __/ _ \ '_ \| __| | | '_ \| __/ _ \  | __| '_ \ / _ \ |  _| | | | __| | | | '__/ _ \
| |/ /  __/\__ \ (_|  __/ | | | |_  | | | | | || (_) | | |_| | | |  __/ | | | |_| | |_| |_| | | |  __/
|___/ \___||___/\___\___|_| |_|\__| |_|_| |_|\__\___/   \__|_| |_|\___| |_|  \__,_|\__|\__,_|_|  \___|

=======================================================================================================
*** “Where is this place?”…") ***
=======================================================================================================   
The fall through the chambers ceiling was painful enough, but the daunting moment of
realisation that you have now entered an underground structure, matching those you would
have found in Maps and Mummies from Wizards of the Ghost.
=======================================================================================================
""")

    while inventory == []:
        exits = []
        print_room(current_room)
        command = menu(exits, current_room["items"], inventory)
        execute_command(command)
    for item in inventory:
        print()
        print(item["ASCII"])
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
        pass

    else:
        enemy = room.get("enemies")
        print("\n")
        print(enemy[0]["intro"])
        print("\n")
        print (enemy[0]["ASCII"])
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
        print ("There is "+list_of_items(items)+" here.")
    

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
    #print("=======================================================================================================")
    print("***", room["name"].upper(),"***")
    print()
    print("=======================================================================================================")
    # Display room description
    print(room["description"])
    print("=======================================================================================================")
    # Display any items
    print_room_items(room)
    print("=======================================================================================================")

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
    if (enemy_goblin_on["alive"] == False and enemy_goblin_oe["alive"] == False and enemy_goblin_ow["alive"] == False):
        rooms["OS"] = rooms["BossOS"]
        rooms["S"] = rooms["BossS"]

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


###########################################################################
#                         dylans combat stuff                             #
###########################################################################
def combat(current_room):
    enemy = current_room["enemies"][0]
    print(enemy["intro"])
    while True:
        combatturn(enemy)
        printcombatitems()
        valid = 0
        while valid == 0:
            command = normalise_input(input("What would you like to do?"))
            if len(command) != 0 and command[0] == "use":
                for item in inventory:
                    if item["id"] == command[1] and item !=  item_dmg_gauntlet and item !=  item_armour:
                        useitem = item
                        valid = 1
        print()
        executecombatcommand(useitem, enemy)
        if enemy["health"] <= 0:
            break
        enemiesattack(enemy)
        if plrhealth <= 0:
            gameover()
        

def combatturn(enemy):
    print()
    print("Your health is " + str(plrhealth) + " and the " + enemy["name"] + "'s is " + str(enemy["health"]))
    print()

def printcombatitems():
    global inventory
    for item in inventory:
        if item !=  item_dmg_gauntlet and item !=  item_armour:
            print("USE "+item["id"].upper()+" to use "+item["name"])
    print()

def executecombatcommand(useitem, enemy):
    global plrhealth
    global inventory
    global plrgold
    if useitem["class"] == "weapon":
        modifier = 1
        if item_dmg_gauntlet in inventory:
            modifier = 1.2

        roll_list = []
        count = useitem["damage_dice"]      # Random damage based on dice throws
        rand_dmg = 0
        while count > 0:
            roll = random.randint(1,useitem["damage_dice"]+1)
            roll_list.append(roll)
            rand_dmg = rand_dmg + roll
            count = count - 1

        print("You rolled:", str(roll_list)[1:-1])
        damage = round((modifier*(rand_dmg)), 1)
        enemy["health"] -= damage
        if (enemy["health"] <= 0):
            enemy["health"] = 0
            print(enemy["death"])
            current_room["enemies"] = []
            plrgold += enemy["gold_worth"]
        else:
            print("You use " + str(useitem["name"].upper()) + " and deal " + str(damage) + " damage.")
            print()
    if useitem["class"] == "heal":
        plrhealth += useitem["healing"]
        if plrhealth > 100:
            plrhealth = 100
        if useitem["single-use"] == True:
            inventory.remove(useitem)

def enemiesattack(enemy):
    global plrhealth
    damage = ((enemy["base_damage"])*(random.randint(75, 125)/100))
    if item_armour in inventory:
        damage = round((damage*0/8), 1)
    plrhealth -= damage
    plrhealth = round(plrhealth, 1)
    if plrhealth <= 0:
        plrhealth = 0
    print(enemy["name"] + " attacked and dealt " + str(damage) + " damage.")
    print()        
        
def gameover():
    print("\nYOU HAVE DIED\n")
    print('''   _____              __  __   ______      ____   __      __  ______   _____  
  / ____|     /\     |  \/  | |  ____|    / __ \  \ \    / / |  ____| |  __ \ 
 | |  __     /  \    | \  / | | |__      | |  | |  \ \  / /  | |__    | |__) |
 | | |_ |   / /\ \   | |\/| | |  __|     | |  | |   \ \/ /   |  __|   |  _  / 
 | |__| |  / ____ \  | |  | | | |____    | |__| |    \  /    | |____  | | \ \ 
  \_____| /_/    \_\ |_|  |_| |______|    \____/      \/     |______| |_|  \_\
                                                                                  ''')

    timeToGrade(getTimer()) 
    
###########################################################################


    
# This is the entry point of our program
def main():
    # Spawn items in random rooms
    random_spawn_item(item_hp_ring)
    random_spawn_item(item_dmg_gauntlet)
    random_spawn_item(item_armour)
    random_spawn_item(item_potion)
    #pick a weapon and starting info
    start()
    # Main game loop
    while True:
        #checks to see if anything needs to be changed
        boss_spawn(enemies)
        #COMBAT
        if plrhealth == 0:
            gameover()
            break
        if current_room["enemies"]:
            combat(current_room)
        # Display game status (room description, inventory etc.)
        #print_room_enemies(current_room)
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


