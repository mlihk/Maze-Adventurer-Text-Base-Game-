from items import *
from map import rooms
player = {"name": "", "alive": True, "health": 100, "gold": 0}
playerInventory = []
# Start game at the beginning of story
current_room = rooms["Beginning"]
