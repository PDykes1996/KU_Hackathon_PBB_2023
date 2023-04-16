from Bomb import Bomb
import random
import math
class Level:
    def __init__(self, levelSize, bombAmt):
        self.levelSize = levelSize
        self.bombAmt = bombAmt
        self.bombs = []
        self.bombPositions = []
        self.levelMap = self.GenerateLevel()

    def GenerateLevel(self):
        self.levelMap = [[0] * self.levelSize for row in range(self.levelSize)]
        return self.PopulateBombs()
        #self.bombHeatmap()
    
    def PopulateBombs(self):
        #create bombs on map
        for x in range(self.bombAmt):
            int1=random.randint(3,self.levelSize-1)
            int2=random.randint(3,self.levelSize-1)
            while [int1,int2] in self.bombPositions: #make sure bomb is not on a space that already has a bomb --- NEED TO ADD WHERE BOMB DOES NOT SPAWN ON PLAYER
                int1=random.randint(0,self.bombAmt)
                int2=random.randint(0,self.bombAmt)
            self.bombs.append(Bomb([int1,int2]))
            self.bombPositions.append([int1,int2])
            self.levelMap[self.bombs[x].bombPosition[0]][self.bombs[x].bombPosition[1]] = self.bombs[x].icon
        return self.levelMap

    def addBomb(self, position):
        int1=random.randint(0,self.levelSize-1)
        int2=random.randint(0,self.levelSize-1)
        while [int1,int2] == position: 
            int1=random.randint(0,self.bombAmt)
            int2=random.randint(0,self.bombAmt)
        self.bombs.append(Bomb([int1,int2]))
        self.bombPositions.append([int1,int2])
        self.levelMap[self.bombs[-1].bombPosition[0]][self.bombs[-1].bombPosition[1]] = self.bombs[-1].icon
    
    def bombAt(self, position):
        #find the bomb at the player's current position
        for bomb in self.bombs:
            if(bomb.bombPosition == position):
                return bomb
'''
    def bombHeatmap(self):
        for bomb in self.bombs:
            for i in range(10):
                self.levelMap[bomb.bombPosition[0]+i][bomb.bombPosition[1]] += abs(i-10)
                self.levelMap[bomb.bombPosition[0]-i][bomb.bombPosition[1]] += abs(i-10)
                self.levelMap[bomb.bombPosition[0]][bomb.bombPosition[1]+i] += abs(i-10)
                self.levelMap[bomb.bombPosition[0]][bomb.bombPosition[1]-i] += abs(i-10)
'''
