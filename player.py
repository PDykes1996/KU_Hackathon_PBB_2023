from playsound import playsound
from LevelGenerator import Level
import pygame

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
        #move player
        if direction == "left" and self.position[1] > 0:
            self.position[1] -= 1
        elif direction == "right" and self.position[1] < self.level.levelSize-1:
            self.position[1] += 1
        elif direction == "down" and self.position[0] < self.level.levelSize-1:
            self.position[0] += 1
        elif direction == "up" and self.position[0] > 0:
            self.position[0] -= 1
        else: #if none of the moves are legal, you hit a wall
            self.hit_wall()
            
    def check_bomb(self):
        return self.position in self.level.bombPositions #returns true if the player is on a bomb (position is in the list of bomb positions)

    def hit_wall(self):
        #what happens when the player hits the wall
        return
        #playsound(self.OOBSound)