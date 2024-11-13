class Player:
    
    def __init__(self, start_room):
        self.current_room = start_room
        self.inventory = []

    def move(self, direction, rooms):
        current_room_obj = rooms[self.current_room]
        next_room = current_room_obj.get_room_in_direction(direction)
        
        if next_room:
            self.current_room = next_room
            print(f"You move {direction} to the {self.current_room}.")
        else:
            print("You can't go that way.")