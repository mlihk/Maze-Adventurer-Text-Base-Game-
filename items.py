item_bow = {

    "name": "sturdy bow",

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

    "description":
    """A Short bow made of Elm; it comes with a quiver of at least 5 arrows.""",

    "damage_dice": 3,
    
    "damage": 4
}

item_staff = {

    "name": "magical staff",

    "class": "weapon",

    "id": "staff",

    "ASCII": """.^.:.
 <.*.'::.      
   |  .:''    
   |    
   |        
   |  """, 

    "description":
    """A two metre tall Staff of alder, it has a shiny gem on top…If only you could choose rogue.""",

    "damage_dice": 1,
    
    "damage": 12           
}

item_sword = {

    "name": "rusty sword",

    "class": "weapon",

    "id": "sword",

    "ASCII": r"""      /| ________________
O|===|* >________________>
      \|""",

    "description":
    """An 80cm long blade and hilt, accompanied by a beautiful scabbard.""",

    "damage_dice": 2,
    
    "damage": 6
}

item_hp_ring = {
    "name": "healing ring",

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
    "name": "damage gauntlets",

    "class": "modifier",

    "id": "gauntlet",

    "description":
    "Damage gauntlets increases your damage by 20%"
}

item_armour = {
    "name": "heavy armour",

    "class": "modifier",

    "id": "armour",

    "description":
    "Heavy armour absorbs 20% damage"
}

item_potion = {
    "name": "healing potion",

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
    
    
