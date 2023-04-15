from Bomb import Bomb
class Level:
    def Level(self, levelSize, bombAmt):
        self.levelSize = levelSize
        self.bombAmt = bombAmt
        self.levelMap = None
    def GenerateLevel(self):
        self.levelMap = [['  '] * self.levelSize for row in range(self.levelSize)]
        return self.PopulateBombs(self.levelmap)
    def PopulateBombs(self, levelMap):





