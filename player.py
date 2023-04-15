class Player:
    def __init__(self, position, mapSize):
        #initializes the player class
        self.position = position
        self.mapSize = mapSize

    def move(self, direction):
        if direction == "left":
            #checks to see if the move is valid
            if (self.position[1] - 1) >= 0:
                self.position[1] -= 1
            else:
                self.hit_wall()
        if direction == "right":
            #checks to see if the move is valid
            if (self.position[1] + 1) < self.mapSize-1:
                self.position[1] += 1
            else:
                self.hit_wall()
        if direction == "down":
            #checks to see if the move is valid
            if (self.position[0] + 1) >= 0:
                self.position[1] += 1
            else:
                self.hit_wall()
        
        #if no moves are valid...nothing so far

    def hit_wall(self):
        #what happens when the player hits the wall
        print("e")

    def print_map(self):
        #prints the map of where the blob has been
        print(f"{self.map_dimensions[0]} {self.map_dimensions[1]}", end="")
        print(f"{self.start[0]} {self.start[1]}", end="")
        for row in self.map:
            for column in row:
                print(column, end="")
            print("")
        print(f"Total eaten: {self.people_eaten}")
        print(self.current)