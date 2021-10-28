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

##### Score that decrease as you do more things #####
score = 200

def decrease_score():
    global score
    score = score - 1 


##### Timer for score ######## Marcus
def timeToHurry():
    print('unknown voice: 3 minutes has passed, quick or we are all dead!')
 
 
timer = threading.Timer(180.0, timeToHurry)
timer.start()
 
startingTimer = time.time() #constant please do not touch
 
def getTimer(): #use to get the time taken to finish the game
    usedTime = time.time() - startingTimer
    print()
    #print(usedTime)
    return usedTime
 
def timeToGrade(usedTime): # converts the time into a grade
    print("Your score is:",score)
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
 _____ _           ___  ___          _     _       _           _                _       _   _     
|_   _| |          |  \/  |         | |   ( )     | |         | |              (_)     | | | |    
  | | | |__   ___  | .  . | ___  ___| |__ |/ ___  | |     __ _| |__  _   _ _ __ _ _ __ | |_| |__  
  | | | '_ \ / _ \ | |\/| |/ _ \/ __| '_ \  / __| | |    / _` | '_ \| | | | '__| | '_ \| __| '_ \ 
  | | | | | |  __/ | |  | |  __/ (__| | | | \__ \ | |___| (_| | |_) | |_| | |  | | | | | |_| | | |
  \_/ |_| |_|\___| \_|  |_/\___|\___|_| |_| |___/ \_____/\__,_|_.__/ \__, |_|  |_|_| |_|\__|_| |_|
                                                                      __/ |                       
                                                                     |___/                        
=======================================================================================================
*** “Where is this place?”…") ***
=======================================================================================================   
The fall through the chambers ceiling was painful enough, but the daunting moment of
realisation that you have now entered an underground structure, matching those you would
have found in Maps and Mummies from Wizards of the Ghost.""")

    while True:
        exits = []
        print_room(current_room)
        command = menu(exits, current_room["items"], inventory)
        execute_command(command)
        if item_bow in inventory or item_sword in inventory or item_staff in inventory:
            break
    print("=======================================================================================================")
    for item in inventory:
        print()
        print(item["ASCII"])
    current_room = rooms["OS"]
    decrease_score()

def list_of_items(items):
    
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
    
    items = room["items"]
    # Check to see if we have items
    if items:
        print ("There is "+list_of_items(items)+" here.")
    

def print_inventory_items(items):
    
    # Check to see if we have items
    if items:
        print ("You have "+list_of_items(items)+".\n")


def print_room(room):
    
    # Display room name
    print("=======================================================================================================")
    print()
    print("                                       ***", room["name"].upper(),"***")
    print()
    print("=======================================================================================================")
    # Display room description
    print(room["description"])
    # Display any items
    print_room_items(room)
    print("=======================================================================================================")

def exit_leads_to(exits, direction):
    
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    
    print("GO " + direction.upper() + " to " + leads_to + ".")
#Checks if all goblins are dead
def boss_spawn(enemies): #check if all enemies are dead, opens boss doors
    #if (enemy_goblin_on["alive"] == False and enemy_goblin_oe["alive"] == False and enemy_goblin_ow["alive"] == False):
    if (enemy_goblin_on["health"] <= 0 and enemy_goblin_oe["health"] <= 0 and enemy_goblin_ow["health"] <= 0):
        rooms["OS"] = rooms["BossOS"]
        rooms["S"] = rooms["BossS"]
def win(enemies):                               # When you kill mecha kirill you win the game
    if enemy_mecha["health"] <= 0:
        print("=======================================================================================================")
        print(r"""
 _   _ _      _                     _   _   _  
| | | (_)    | |                   | | | | | | 
| | | |_  ___| |_ ___  _ __ _   _  | | | | | | 
| | | | |/ __| __/ _ \| '__| | | | | | | | | | 
\ \_/ / | (__| || (_) | |  | |_| | |_| |_| |_| 
 \___/|_|\___|\__\___/|_|   \__, | (_) (_) (_) 
                             __/ |             
                            |___/

__   __            _                           _       __           _           _  
\ \ / /           | |                         | |     / _|         | |         | | 
 \ V /___  _   _  | |__   __ ___   _____    __| | ___| |_ ___  __ _| |_ ___  __| | 
  \ // _ \| | | | | '_ \ / _` \ \ / / _ \  / _` |/ _ \  _/ _ \/ _` | __/ _ \/ _` | 
  | | (_) | |_| | | | | | (_| |\ V /  __/ | (_| |  __/ ||  __/ (_| | ||  __/ (_| | 
  \_/\___/ \__,_| |_| |_|\__,_| \_/ \___|  \__,_|\___|_| \___|\__,_|\__\___|\__,_| 
                                                                                   
                                                                                   
___  ___ _____ _____  _   _   ___         _   _____________ _____ _      _         
|  \/  ||  ___/  __ \| | | | / _ \       | | / /_   _| ___ \_   _| |    | |        
| .  . || |__ | /  \/| |_| |/ /_\ \______| |/ /  | | | |_/ / | | | |    | |        
| |\/| ||  __|| |    |  _  ||  _  |______|    \  | | |    /  | | | |    | |        
| |  | || |___| \__/\| | | || | | |      | |\  \_| |_| |\ \ _| |_| |____| |____    
\_|  |_/\____/ \____/\_| |_/\_| |_/      \_| \_/\___/\_| \_|\___/\_____/\_____/    
                                                                                   
                                                                                   """)

        timeToGrade(getTimer())

'''
def alive_change(enemies):
    if enemy_goblin_on["health"] == 0:
        enemy_goblin_on["alive"] = False
            
    if enemy_goblin_oe["health"] == 0:
        enemy_goblin_oe["alive"] = False
            
    if enemy_goblin_ow["health"] == 0:
        enemy_goblin_ow["alive"] = False
'''
def print_menu(exits, room_items, inv_items):
    
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
    
    return chosen_exit in exits


def execute_go(direction):
    
    global current_room
    
    if is_valid_exit(current_room["exits"],direction):
       current_room = move(current_room["exits"],direction)
       decrease_score()

    else:
        print("You cannot go there.")


def execute_take(item_id):
    
    global current_room
    global inventory
    foundItem = False
    
    for item in current_room["items"]:
        if item["id"] == item_id:
            current_room["items"].remove(item)
            inventory.append(item)
            foundItem = True
            decrease_score()
    
    if not foundItem:
        print("You cannot take that.")

def execute_drop(item_id):
    
    global current_room
    global inventory
    foundItem = False
    
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            current_room["items"].append(item)
            foundItem = True
            decrease_score()
    
    if not foundItem:
        print("You cannot drop that.")
    

def execute_command(command):

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

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):

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
    print(r"""

=======================================================================================================
 _____                 _           _     _____      _ _   _       _           _ _ 
/  __ \               | |         | |   |_   _|    (_) | (_)     | |         | | |
| /  \/ ___  _ __ ___ | |__   __ _| |_    | | _ __  _| |_ _  __ _| |_ ___  __| | |
| |    / _ \| '_ ` _ \| '_ \ / _` | __|   | || '_ \| | __| |/ _` | __/ _ \/ _` | |
| \__/\ (_) | | | | | | |_) | (_| | |_   _| || | | | | |_| | (_| | ||  __/ (_| |_|
 \____/\___/|_| |_| |_|_.__/ \__,_|\__|  \___/_| |_|_|\__|_|\__,_|\__\___|\__,_(_)

=======================================================================================================""")
    print(enemy["intro"])
    print("=======================================================================================================")
    print(enemy["ASCII"])
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
    print("=======================================================================================================")
    print("Your health is " + str(plrhealth) + " and the " + enemy["name"] + "'s is " + str(enemy["health"]))
    print("=======================================================================================================")

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
            roll = random.randint(1,useitem["damage"]+1)
            roll_list.append(roll)
            rand_dmg = rand_dmg + roll
            count = count - 1

        print("=======================================================================================================")
        print("You rolled:", str(roll_list)[1:-1])
        decrease_score()
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
        damage = round((damage*0.8), 1)
    plrhealth -= damage
    plrhealth = round(plrhealth, 1)
    if plrhealth <= 0:
        plrhealth = 0
    print(enemy["name"] + " attacked and dealt " + str(damage) + " damage.")
    print("=======================================================================================================")
    print(r"""
 _   _           _     _____                _ 
| \ | |         | |   |_   _|              | |
|  \| | _____  _| |_    | |_   _ _ __ _ __ | |
| . ` |/ _ \ \/ / __|   | | | | | '__| '_ \| |
| |\  |  __/>  <| |_    | | |_| | |  | | | |_|
\_| \_/\___/_/\_\\__|   \_/\__,_|_|  |_| |_(_)
                                              
                                              """)        
        
def gameover():
    print('''   _____              __  __   ______      ____   __      __  ______   _____  
  / ____|     /\     |  \/  | |  ____|    / __ \  \ \    / / |  ____| |  __ \ 
 | |  __     /  \    | \  / | | |__      | |  | |  \ \  / /  | |__    | |__) |
 | | |_ |   / /\ \   | |\/| | |  __|     | |  | |   \ \/ /   |  __|   |  _  / 
 | |__| |  / ____ \  | |  | | | |____    | |__| |    \  /    | |____  | | \ \ 
  \_____| /_/    \_\ |_|  |_| |______|    \____/      \/     |______| |_|  \_\
                                                                                  ''')

    usedTime = time.time() - startingTimer
    print()
    print('Time used: ', math.floor(usedTime),'seconds')
    print('You died...')
    sys.exit()
    
###########################################################################


    
# This is the entry point of our program
def main():
    # Spawn items in random rooms
    random_spawn_item(item_dmg_gauntlet)
    random_spawn_item(item_armour)
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
            win(enemies)
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


