import random
all_rooms = []
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
    def __init__(self, name, items, connections):
        self.name = name
        self.items = list(items)
        #consider making items a class instead of a string, where usable items can be defined with specific attributes
        self.connections = connections
        #possibly make connections into a dictionary where the key is the room and the value is a visited bool
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = []
        self.items = []
    def __str__(self):
        return f"Room: {self.name} has {self.items}, connected to {self.connections}"
    
    #Remove an item from the room
    def remove_item(self, item_to_remove):
        self.items = filter(lambda i: i != item_to_remove, list(self.items))

    def add_item(self, item_to_add):
        self.items = list(self.items).append(item_to_add)

        # Create Room instances and add them to the global list
    def create_rooms():
        kitchen = Room("Kitchen", ["knife", "pan"], {"Hallway": ["north", False]})
        hallway = Room("Hallway", [], {"Kitchen": ["south", True], "Bedroom": ["north", False]})
        bedroom = Room("Bedroom", ["lamp"], {"Hallway": False, "Bathroom": False})
        all_rooms.append(kitchen)
        all_rooms.append(bedroom)
        
def generate_random_map(num_rooms=5):
    rooms = {}
    
    # Create rooms with random names and descriptions
    for i in range(num_rooms):
        name = random.choice(room_names)
        description = random.choice(room_descriptions)
        room = Room(name, description)
        rooms[name] = room
    
    # Step 3: Connect rooms randomly
    room_list = list(rooms.values())
    for room in room_list:
        # Add 1-2 random connections to other rooms
        possible_connections = random.sample(room_list, k=random.randint(1, 2))
        for connection in possible_connections:
            if connection != room:
                direction = random.choice(["north", "south", "east", "west"])
                room.connections[direction] = connection.name
                # Make reciprocal connection
                opposite_direction = {
                    "north": "south", "south": "north", 
                    "east": "west", "west": "east"
                }[direction]
                connection.connections[opposite_direction] = room.name

    # Step 4: Place items randomly in rooms
    for room in room_list:
        if random.random() < 0.5:  # 50% chance to have an item in a room
            item = random.choice(items)
            room.items.append(item)
    
    return rooms

all_rooms = generate_random_map()
#how to randomize rooms
#number 1 - 3 for doorways, hold direction for way entered
# randomize items
# 

# Example usage
#for room in all_rooms:
#    print(room)