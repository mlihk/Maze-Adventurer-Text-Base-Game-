from items import *
from map import rooms

inventory = [item_hp_ring, item_potion]
plrhealth = int(100)
plrgold = int(0)
# Start game at the beginning of story
current_room = rooms["Beginning"]
