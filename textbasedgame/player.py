class Player:
    
    def __init__(self, start_room):
        self.current_room = start_room
        self.inventory = []

    def move(self, direction, rooms):
        next_room = self.current_room.get_connection(direction)
        #make get_room_in_direciton, if no room make it None
               
        if next_room: #next room exists
            if (next_room.is_locked() == True and self.inventory.count("key") == 0):
                print(f"The door to the {direction} is locked. You need a key\n")
            elif (next_room.is_locked() == True and self.inventory.count("key") > 0):
                check = input("This door is locked, care to unlock it?\n")
                if (check == "yes" or check == "y"):
                    self.current_room = next_room
                    next_room.unlock_room()
                    self.inventory.remove("key")
                    print(f"You unlcok the door and move {direction} to the {self.current_room.get_name()}.\n")
                else: 
                    print(f"You chose to not to unlock the door.\n")
                
            else:
                self.current_room = next_room
                print(f"You move {direction} to the {self.current_room.get_name()}.\n")
        else:
            print("You can't go that way.")

        return self.current_room
        

    def drop_item(self,item, curr_room):
        #if player has item, drop it in room
        if (item != None and self.inventory.count(item) > 0):
            curr_room.add_item(item)
            self.inventory.remove(item)

    def pick_up_item(self, item, room):
        if (item != None):
            self.inventory.append(item)
            room.remove_item(item)

    def use_item(self, item, room):
        if(item == "key"):
            self.inventory.remove("key")


    def check_inventory(self):
        if (len(self.inventory) == 0):
            print(f"Your pockets are sadly empty")
        else:
            print(f"You check your pockets and find: {self.inventory}")

#TODO: attacking, using items, unlocking doors