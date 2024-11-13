import random

NUM_MAPS = 1

room_names = ["Hall", "Library", "Armory", "Garden", "Bedroom", "Kitchen"]
room_descriptions = [
    "A quiet, empty room.",
    "A dark room with cobwebs in the corners.",
    "A brightly lit room with strange markings on the walls.",
    "A dusty room with shelves filled with ancient books.",
    "A room filled with mysterious armor.",
]
items = ["Key", "Map", "Potion", "Sword", "Lantern"]

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        #consider making items a class instead of a string, where usable items can be defined with specific attributes
        self.connections = {}

    def __str__(self):
        return f"Room: {self.name} has {self.items}, connected to {self.connections}"
    def get_name(self):
        return self.name
    
    #Remove an item from the room
    def remove_item(self, item_to_remove):
        self.items = filter(lambda i: i != item_to_remove, self.items)

    def add_item(self, item_to_add):
        self.items = self.items.append(item_to_add)

    def connect(self, room, dir):
        self.connections[dir] = room
    def get_connection(self, direction):
        return self.connections.get(direction, None)
    
    def add_item(self, item):
        if (item != None):
            self.items.append(item)
    def remove_item(self, item):
        if (item != None and self.items.count(item) > 0):
            self.items.remove(item)

    def check_room(self):
        print(f"You seem to be standing in some kind of {self.name}\n")

        if (len(self.items) == 1):
            print(f"You see a {self.items[0]} on the ground\n")
        elif(len(self.items) > 1):
            print(f"You see some things scattered about: {self.items}\n")

        for direction, room in self.connections.items():
            print(f"There's a room to the {direction}\n")
        
        # Create Room instances and add them to the global list
    

#how to randomize rooms
#number 1 - 3 for doorways, hold direction for way entered
# randomize items
# 

# Example usage
#for room in all_rooms:
#    print(room)

#MAPS
map_id = random.randint(1, NUM_MAPS)
map = []
if (map_id == 1):
    #make rooms
    entrance = Room("Entrance", "Start to a cool adventure")
    living_room = Room("Living Room", "A cozy living room with a sofa and TV.")
    kitchen = Room("Kitchen", "A small kitchen with a stove and fridge.")
    bathroom = Room("Bathroom", "A small bathroom with a shower.")
    bedroom = Room("Bedroom", "A quiet bedroom with a comfy bed.")
    #connect them
    entrance.add_item("sword")
    entrance.connect(living_room, "north")
    living_room.connect(entrance, "south")

    living_room.connect(kitchen, "north")
    kitchen.connect(living_room, "south")

    living_room.connect(bathroom, "east")
    bathroom.connect(living_room, "west")

    kitchen.connect(bedroom, "west")
    bedroom.connect(kitchen, "east")

    map = [entrance, living_room, kitchen, bathroom, bedroom]

#make a lost woods map where 2 of the 3 directions lead to the same room!

#TODO: more maps, keys/locked doors, enemies, 