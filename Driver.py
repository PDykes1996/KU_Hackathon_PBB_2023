import random
from Bomb import Bomb
from player import Player
from LevelGenerator import Level
from pynput import keyboard

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'
mainMap = Level(15, 10)
playerCharacter = Player((0,0), mainMap.levelSize)
def main():
    mainMap.levelMap[playerCharacter.position[0]][playerCharacter.position[1]] = '|P|'
    updateMap(mainMap)

    while (1):
        listener = keyboard.Listener(on_press=on_press)
        listener.start()  # start to listen on a separate thread
        listener.join() 

def updateMap(currentMap):
    for x in range(mainMap.levelSize):
        for y in range(mainMap.levelSize):
            print(currentMap.levelMap[x][y], end='')
        print('')

def on_press(key):
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['up', 'down', 'left', 'right']:  # keys of interest
        print('Key pressed: ' + k)
        mainMap.levelMap[playerCharacter.position[0]][playerCharacter.position[1]] = '| |'
        playerCharacter.move(k)
        for i in range(mainMap.levelSize):
            print(LINE_UP, end=LINE_CLEAR)
        mainMap.levelMap[playerCharacter.position[0]][playerCharacter.position[1]] = '|P|'
        updateMap(mainMap)
        return False  # stop listener; remove this if want more keys



main()