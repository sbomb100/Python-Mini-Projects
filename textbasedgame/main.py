from rooms import map
from player import Player

game_running = True
current_room = map[0]
commands = ["move dir: allows you to pick a direction to change rooms", 
            "grab item: lets you pick up a defined item",
            "drop item: lets you place a held item on the ground",
            "inventory: lists all items in your inventory"
            "check room: ask about items or connecting rooms", 
            "quit: stop the game"]
last_command = None #perhaps allow for empty lines to exec last command for faster movement
player = Player(start_room = current_room)
assert(map != [])

while game_running:
    inp = input("--> What would you like to do?\n")
    command = inp.split(" ")
    print("---------------------------------------")
    
    #player commands -------

    #movement implementation
    if command[0] == "move":
        direction = command[1]
        current_room = player.move(direction, map)

    #item manip
    elif command[0] == "grab":
        player.pick_up_item(command[1], current_room)
        print(f"You grab the {command[1]}")

    elif command[0] == "drop":
        player.drop_item(command[1], current_room)
        print(f"You dropped the {command[1]}")
    
    elif command[0] == "inventory":
        player.check_inventory()
    
    #observe the current room
    elif command[0] == "check" and command[1] == "room":
        print("You look around: \n")
        current_room.check_room()

    
    #logistics commands ---------
    #list all commands
    elif command[0] == "help":
        print(f"commands: \n")
        for elem in commands:
            print(f"{elem}") 
        print("\n")

    #end run
    elif command[0] == "quit":
        game_running = False
        print("\n")

    

    else:
        print("please input a valid command! type 'help' for assistance \n")

    print("---------------------------------------")
    
#TODO: brainstorm more commands and things needed for the game,  inspect commadns