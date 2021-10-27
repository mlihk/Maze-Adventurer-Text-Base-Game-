from items import *
from enemies import *

room_os = {
    "name": "OS",

    "description":
    """You are in a chamber with a corridor leading NORTH and a door 
leading SOUTH. The Southern door has wires attached to it.""",

    "exits": {"north": "S"},

    "items": [item_bow]
}

room_os_boss = {
    "name": "OS",

    "description":
    """You are in a chamber You are in a chamber with a corridor leading
NORTH and a door leading SOUTH. The Southern door is open you can see
the light of the world.""",

    "exits": {"north": "S", "south": "BR"},

    "items": [item_bow]
}

room_s = {
    "name": "S",

    "description":
    """You see a shimmering red barrier in front of you, the whir of mechanisms 
can be heard beyond its threshold. To your EAST, SOUTH and WEST, are 
3 corridors with no distinguishing features other than the torches that 
light the way.""",

    "exits": {"north": "BR","east": "SE","west": "SW","south": "OS"},

    "items": [item_bow]
}
room_sw = {
    "name": "SW",

    "description":
    """The room is made of stone, to the NORTH and EAST 
are corridors leading away.""",

    "exits": {"north": "W","east": "S"},

    "items": [item_bow]
}
room_w = {
    "name": "W",

    "description":
    """You enter the room. To the NORTH, WEST and SOUTH are 
corridors that lead further into the maze. To your EAST 
to see a large room with seemingly no floor, in the 
centre is a Pillar of stone and grinding gears, you 
can see no further way to continue this direction.""",

    "exits": {"north": "NW", "west": "OW", "south": "SW"},

    "items": [item_bow]
}
room_ow = {
    "name": "OW",

    "description":
    """The room contains one exit to the EAST, the lifeless corpse of a Goblin like creature lays still. 
Above the exit you see a sign “All 3, you, they, be free.”""",

    "exits": {"east": "W"},

    "enemies": [enemy_goblin_ow],

    "items": [item_bow]
}
room_nw = {
    "name": "NW",

    "description":
    """The room is made of stone, to the 
EAST and SOUTH are corridors leading away.""",

    "exits": {"east": "N","south":"W"},

    "items": [item_bow]
}
room_n = {
    "name": "N",

    "description":
    """You enter the room. To the WEST, NORTH and EAST are corridors 
that lead further into the maze. To your SOUTH to see a large room 
with seemingly no floor, in the centre is a Pillar of stone and 
grinding gears, you can see no further way to continue this direction.""",

    "exits": {"west": "NW","north":"ON","east":"NE"},

    "items": [item_bow]
}
room_on = {
    "name": "ON",

    "description":
    """The room contains one exit to the SOUTH, the lifeless corpse of a 
Goblin like creature lays still. Above the exit you see a 
sign “All 3, you, they, be free.”""",

    "exits": {"south": "N"},

    "enemies": [enemy_goblin_on],

    "items": [item_bow]
}
room_ne = {
    "name": "NE",

    "description":
    """The room is made of stone, to the SOUTH and WEST are corridors leading 
away. A small piece of writing is on the wall…Cake = Lie.""",

    "exits": {"south": "E","west":"N"},

    "items": [item_bow]
}
room_e = {
    "name": "E",

    "description":
    """You are in a chamber with a corridor leading NORTH and a door 
leading SOUTH. The Southern door has wires attached to it.""",

    "exits": {"north": "NE","south":"SE","east":"OE"},

    "items": [item_bow]
}
room_oe = {
    "name": "OE",

    "description":
    """The room contains one exit to the WEST, the lifeless corpse of a 
Goblin like creature lays still. 
Above the exit you see a sign “All 3, you, they, be free.”.""",

    "exits": {"west": "E"},

    "enemies": [enemy_goblin_oe],

    "items": [item_bow]
}
room_se = {
    "name": "SE",

    "description":
    """The room is made of stone, 
to the WEST and NORTH are corridors leading away.""",

    "exits": {"north": "E","west":"S"},

    "items": [item_bow]
}
room_br = {
    "name": "BR",

    "description":
    """You are in a large room with the remains of Mechakirill 
the light showing the activation of the exit button 
is glowing green. To your SOUTH you see the exit to another room, 
and a light in the distance.""",

    "exits": {"south": "S"},

    "enemies": [enemy_mecha],

    "items": [item_bow]
}




rooms = {
    "OS": room_os,
    "S": room_s,
    "SW": room_sw,
    "W": room_w,
    "OW": room_ow,
    "NW": room_nw,
    "N": room_n,
    "ON": room_on,
    "NE": room_ne,
    "E": room_e,
    "OE": room_oe,
    "SE": room_se,
    "BR": room_br
}