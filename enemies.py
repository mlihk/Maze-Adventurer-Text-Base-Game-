#from items import *

enemy_goblin_on = {
    "name": "Goblin",

    "description":
     """As you enter the room, a snigger and chuckle meet you from the opposite corner, slightly shining eyes meet your gaze, their owner lunges towards you.""",

    "ASCII": """
            ((.-""-.))     
        |\  \/      \/  /|
        | \ / =.  .= \ / |
        \( \   o\/o   / )/
         \_, '-/  \-' ,_/
               \__/   
           \ \__/\__/ /
         ___\ \|--|/ /___
       (`    \      /    `)    
       |      '----'      |""",

    "death": "As the goblin falls back you here a mechanised cacophony of sound radiating from behind you.",

    "health": 20,

    "alive": True,

    "base_damage": 5

}

enemy_goblin_oe = {
    "name": "Goblin",

    "description":
    """From the ceiling falls a creature with the grace of a rock, he looks up to you and unsheathes its daggers.""",

    "ASCII": """
            ((.-""-.))     
        |\  \/      \/  /|
        | \ / =.  .= \ / |
        \( \   o\/o   / )/
         \_, '-/  \-' ,_/
               \__/   
           \ \__/\__/ /
         ___\ \|--|/ /___
       (`    \      /    `)    
       |      '----'      |""",
    
    "death": "As the goblin falls back you here a mechanised cacophony of sound radiating from behind you.",

    "health": 20,

    "alive": True,

    "base_damage": 5

}

enemy_goblin_ow = {
    "name": "Goblin",

    "description":
    """As you enter the room, a cackle then cry comes from the corner, bearing two knives, and pale green skin, the
creature lunges at you.""",

    "ASCII": """
            ((.-""-.))     
        |\  \/      \/  /|
        | \ / =.  .= \ / |
        \( \   o\/o   / )/
         \_, '-/  \-' ,_/
               \__/   
           \ \__/\__/ /
         ___\ \|--|/ /___
       (`    \      /    `)    
       |      '----'      |""",

    "death": "As the goblin falls back you here a mechanised cacophony of sound radiating from behind you.",

    "health": 20,

    "alive": True,

    "base_damage": 5

}

enemy_mecha = {
    "name": "Mecha Kirill",

    "description":
    """As you walk into the room, you can see a huge button displaying exit lit up in red. Underneath, is a small
compact construct with a small head inside. The eyes begin to stare at you, as the construct slowly begins to rise,
lifting two cannons on each arm and standing over 9 feet tall. “Computers are the future, the world will meet a
new era of tyranny, for I am MECHAKIRILL""",

    "death": """As little pops are heard of transistors and electronics breaking inside the looming structure, the hulking
mass of metal and destruction falls back against the rear wall, conveniently catching the exit button, which now lights green.
“Yoouu…ffaaaiillllll”, all signs of what could be considered life, are no-longer considered.""",

    "health": 100,

    "alive": True,

    "base_damage": 30
}

enemies = {
    "Goblin ON": enemy_goblin_on,
    "Goblin OE": enemy_goblin_oe,
    "Goblin OW": enemy_goblin_ow,
    "Mecha": enemy_mecha
}
