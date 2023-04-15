from Bomb import Bomb
import random
class Level:
    def __init__(self, levelSize, bombAmt):
        self.levelSize = levelSize
        self.bombAmt = bombAmt
        self.bombs = []
        self.levelMap = self.GenerateLevel()

    def GenerateLevel(self):
        self.levelMap = [['| |'] * self.levelSize for row in range(self.levelSize)]
        return self.PopulateBombs(self.levelMap)
    def PopulateBombs(self, levelMap):
        bombPositions = []
        for x in range(self.bombAmt):
            int1=random.randint(3,self.levelSize-1)
            int2=random.randint(3,self.levelSize-1)
            while (int1,int2) in bombPositions:
                int1=random.randint(0,self.bombAmt)
                int2=random.randint(0,self.bombAmt)
            self.bombs.append(Bomb((int1,int2),True))
            levelMap[self.bombs[x].bombPosition[0]][self.bombs[x].bombPosition[1]] = self.bombs[x].icon
        return levelMap



