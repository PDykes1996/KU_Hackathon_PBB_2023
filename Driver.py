import random
from Bomb import Bomb
from player import Player
from LevelGenerator import Level

mainMap = Level(15, 10)
def main():
    playerCharacter = Player((0,0), mainMap.levelSize)
    mainMap.levelMap[playerCharacter.position[0]][playerCharacter.position[1]] = '|P|'
    updateMap(mainMap)

def updateMap(currentMap):
    for x in range(mainMap.levelSize):
        for y in range(mainMap.levelSize):
            print(currentMap.levelMap[x][y], end='')
        print('')

main()