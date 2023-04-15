from playsound import playsound
from LevelGenerator import Level
class Player:
    def __init__(self, position, level):
        #initializes the player class
        self.position = position
        self.level = level
        #Sounds
        self.OOBSound = ""
        self.wireCutSound = ""
        self.geiger1Sound = ""
        self.geiger2Sound = ""
        self.geiger3Sound = ""

    def move(self, direction):
        if direction == "left" and self.position[1] > 0:
            self.position[1] -= 1
        elif direction == "right" and self.position[1] < self.mapSize-1:
            self.position[1] += 1
        elif direction == "down" and self.position[0] < self.mapSize-1:
            self.position[0] += 1
        elif direction == "up" and self.position[0] > 0:
            self.position[0] -= 1
        else:
            self.hit_wall()

        if self.check_bomb():
            self.hit_bomb()
            
    def check_bomb(self):
        return self.position in self.level.bombPositions

            
    def hit_bomb(self):
        #what happens when the player hit bomb
        print("b")

    def hit_wall(self):
        #what happens when the player hits the wall
        playsound(self.OOBSound)