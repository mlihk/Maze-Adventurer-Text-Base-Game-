from items import *
from map import rooms

inventory = []
#inventory = [item_sword, item_hp_ring, item_potion]
plrhealth = int(1)
plrgold = int(0)
# Start game at the beginning of story
current_room = rooms["Beginning"]
