from rooms import map
from player import Player

game_running = True
current_room = map[0]
commands = ["move dir: allows you to pick a direction to change rooms", 
            "grab item: lets you pick up a defined item",
            "drop item: lets you place a held item on the ground",
            "inventory: lists all items in your inventory",
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
    if command[0] == "move" or command[0] == "m":
        direction = command[1]
        current_room = player.move(direction, map)

    #item manip
    elif command[0] == "grab" or command[0] == "g":
        player.pick_up_item(command[1], current_room)
        print(f"You grab the {command[1]}")

    elif command[0] == "drop" or command[0] == "d":
        player.drop_item(command[1], current_room)
        print(f"You dropped the {command[1]}")
    
    elif command[0] == "inventory" or command[0] == "i":
        player.check_inventory()
    
    #observe the current room
    elif (command[0] == "check" and command[1] == "room") or command[0] == "cr":
        print("You look around: \n")
        current_room.check_room()

    
    #logistics commands ---------
    #list all commands
    elif command[0] == "help" or command[0] == "h":
        print(f"commands: \n")
        for elem in commands:
            print(f"{elem}") 
        print("\n")

    #end run
    elif command[0] == "quit" or command[0] == "q":
        game_running = False
        print("Cya!\n")

    

    else:
        print("please input a valid command! type 'help' for assistance \n")

    print("---------------------------------------")
    
#TODO: brainstorm more commands and things needed for the game,  inspect commadns

#----inspect prompts
#check room: you see something glimmer in the corner of the room: inspect corner/glimmer
#a book seems to have something stuffed inside: inspect book
#the floorboard seems to have been moved at one point: inspect floor/ground
#the ground seems to have been dug recently: inspect dirt/ground
#door is locked and seems to be no keys, light shines through keyhole: inspect keyhole