item_bow = {

    "name": "sturdy bow (deals 3d4)",

    "class": "weapon",

    "id": "bow",

    "ASCII":
    r"""   (
    \
     )
##-------->        
     )
    /
   (""",

    "sound": "player_bow_attack.wav",

    "description":
    """A Short bow made of Elm; it comes with a quiver of at least 5 arrows.""",

    "damage_dice": 3,
    
    "damage": 4
}

item_staff = {

    "name": "magical staff (deals 1d12)",

    "class": "weapon",

    "id": "staff",

    "ASCII": """.^.:.
 <.*.'::.      
   |  .:''    
   |    
   |        
   |  """,
    "sound": "player_staff_attack.mp3",

    "description":
    """A two metre tall Staff of alder, it has a shiny gem on top…If only you could choose rogue.""",

    "damage_dice": 1,
    
    "damage": 12           
}

item_sword = {

    "name": "rusty sword (deals 2d6)",

    "class": "weapon",

    "id": "sword",

    "ASCII": r"""      /| ________________
O|===|* >________________>
      \|""",

    "sound": "player_sword_attack.wav",

    "description":
    """An 80cm long blade and hilt, accompanied by a beautiful scabbard.""",

    "damage_dice": 2,
    
    "damage": 6
}

item_hp_ring = {
    "name": "healing ring (heals 10hp - unlimited)",

    "class": "heal",

    "id": "ring",

    "ASCII": r"""  '   ,'\  
 /   /   | 
.   ; ,. : 
'   | |: : 
'   | .; : 
|   :    | 
 \   \  /  
  `----'  """, 


    "description":
    "ring that heals",

    "healing": 10,

    "single-use": False
}

item_dmg_gauntlet = {
    "name": "damage gauntlets (+25% damage)",

    "class": "modifier",

    "id": "gauntlet",

    "description":
    "Damage gauntlets increases your damage by 20%"
}

item_armour = {
    "name": "heavy armour (+25% defence)",

    "class": "modifier",

    "id": "armour",

    "description":
    "Heavy armour absorbs 20% damage"
}

item_potion = {
    "name": "healing potion (heals 30hp - single use)",

    "class": "heal",

    "quantity": 1,

    "id": "potion",

    "ASCII": r"""  |~|
  | |
.'   `.
`.___.'""",

    "description":
    "Fully replenishes health",

    "healing": 30,

    "single-use": True    
}


items = {
    "sturdy bow": item_bow,
    "magical staff": item_staff,
    "sword": item_sword,
    "healing ring": item_hp_ring,
    "heavy armour": item_armour,
    "potion": item_potion
}
    
    
