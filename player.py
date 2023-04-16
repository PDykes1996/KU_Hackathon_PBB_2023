from playsound import playsound
from LevelGenerator import Level
import pygame
import cmath
import math

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
        self.defuses = 3
        self.defuseOn = False
        self.defusePos = [-1,-1]

    def activateDefuse(self, position):
        if self.defuses <= 0:
            return
        self.defuses -= 1
        self.defuseOn = True
        self.defusePos = position

    def deactivateDefuse(self):
        self.defuseOn = False
        self.defusePos = [-1,-1]

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
        return (self.position in self.level.bombPositions and self.level.bombAt(self.position).isActive == True) #returns true if the player is on a bomb (position is in the list of bomb positions)

    def hit_wall(self):
        #what happens when the player hits the wall
        playsound('border.mp3', False)

    def DistanceFromBombs(self, activeBombs):
        avgDist = 0
        count = 0
        for bomb in activeBombs:
            if bomb.isActive:
                count += 1
                playerX = self.position[0]
                playerY = self.position[1]
                bombX = bomb.bombPosition[0]
                bombY = bomb.bombPosition[1]
                SQR1 = (playerX-bombX)**2
                SQR2 = (playerY-bombY)**2
                dist = math.floor(math.sqrt(SQR1+SQR2))
                if(dist <= 10):
                    avgDist += (dist)
        return avgDist/count

    
    def defuse_bomb(self):
        #play sound
        playsound('cut.mp3')
        self.level.bombAt(self.position).isActive = False
        self.level.addBomb(self.position)
