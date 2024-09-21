import random

class WumpusGame:
    def __init__(self):
        self.cave_size = 20  # Size of the cave (can be adjusted)
        self.num_pits = 5     # Number of pits in the cave (can be adjusted)
        self.arrows = 3       # Number of arrows the player has
       
        self.generate_cave()
        self.place_objects()
       
    def generate_cave(self):
        # Generate cave layout
        self.rooms = []
        for _ in range(self.cave_size):
            self.rooms.append({
                'has_wumpus': False,
                'has_pit': False,
                'connected_rooms': []
            })
       
        # Connect rooms randomly
        for i in range(self.cave_size):
            num_connections = random.randint(2, 4)  # Random number of connections per room
            connected = set()
            while len(connected) < num_connections:
                room = random.randint(0, self.cave_size - 1)
                if room != i:
                    connected.add(room)
            self.rooms[i]['connected_rooms'] = list(connected)
       
    def place_objects(self):
        # Place Wumpus
        wumpus_room = random.randint(0, self.cave_size - 1)
        self.rooms[wumpus_room]['has_wumpus'] = True
       
        # Place pits
        pits_placed = 0
        while pits_placed < self.num_pits:
            pit_room = random.randint(0, self.cave_size - 1)
            if not self.rooms[pit_room]['has_wumpus'] and not self.rooms[pit_room]['has_pit']:
                self.rooms[pit_room]['has_pit'] = True
                pits_placed += 1
   
    def print_current_room_info(self, current_room):
        print(f"You are in room {current_room}")
        print("Tunnels lead to rooms:", self.rooms[current_room]['connected_rooms'])
        if self.rooms[current_room]['has_wumpus']:
            print("You smell a terrible stench...")
        if self.rooms[current_room]['has_pit']:
            print("You feel a cold breeze...")
   
    def play(self):
        current_room = 0
        game_over = False
       
        while not game_over:
            self.print_current_room_info(current_room)
            action = input("Enter 'move <room_number>' or 'shoot <room_number>': ")
           
            if action.startswith("move"):
                try:
                    move_to_room = int(action.split()[1])
                    if move_to_room in self.rooms[current_room]['connected_rooms']:
                        current_room = move_to_room
                    else:
                        print("You can't move there!")
                except ValueError:
                    print("Invalid input! Please enter 'move <room_number>'.")
           
            elif action.startswith("shoot"):
                try:
                    shoot_room = int(action.split()[1])
                    if shoot_room in self.rooms[current_room]['connected_rooms']:
                        self.arrows -= 1
                        if self.rooms[shoot_room]['has_wumpus']:
                            print("Congratulations! You killed the Wumpus!")
                            game_over = True
                        else:
                            print("Oh no! Missed!")
                            if self.arrows == 0:
                                print("Out of arrows! Game over!")
                                game_over = True
                    else:
                        print("You can't shoot there!")
                except ValueError:
                    print("Invalid input! Please enter 'shoot <room_number>'.")
           
            else:
                print("Invalid input! Please enter 'move <room_number>' or 'shoot <room_number>'.")
       
        print("Game over.")

# Example usage:
game = WumpusGame()
game.play()


