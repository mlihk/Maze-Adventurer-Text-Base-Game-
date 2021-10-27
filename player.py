from items import *
from map import rooms

inventory = [item_sword, item_hp_ring, item_potion]
plrhealth = int(100)
plrgold = int(0)

# Start game at the reception
current_room = rooms["OS"]
