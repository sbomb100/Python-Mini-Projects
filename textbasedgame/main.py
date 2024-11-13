from rooms import all_rooms
from player import Player

game_running = True
current_room = all_rooms[0]
commands = ["move dir: allows you to pick a direction to change rooms", 
            "check room: ask about items or connecting rooms", 
            "quit: stop the game"]
last_command = None #perhaps allow for empty lines to exec last command for faster movement
player = Player(start_room=current_room)

while game_running:
    command = input("--> What would you like to do?\n")

    if command[0] == "help":
        print(f"commands to type: \n")
        for elem in commands:
            print(f"{elem}") 
        print("\n")

    #movement implementation
    elif command[0] == "move":
        direction = command[1]
        player.move(direction, all_rooms)
        
    #observe the current room
    elif command == "check room":
        print(f"Current Room: {str(current_room)}\n")

    #end run
    elif command == "quit":
        game_running = False
        print("\n")

    else:
        print("please input a valid command! type 'help' for assistance \n")
    
