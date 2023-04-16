import random
from Bomb import Bomb
from player import Player
from LevelGenerator import Level
from pynput import keyboard
from playsound import playsound
from SoundDriver import SoundDriver
import pygame
import time

pygame.init()
pygame.mixer.init()

#variables to overwrite lines
LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

#game variables
mainMap = Level(20, 1)
playerCharacter = Player([0,0], mainMap)
gameover = False
global numBombsDefused
numBombsDefused = 0

audioEventPlayer = SoundDriver()
audioGeigerPlayer = SoundDriver()
audioGeigerPlayer.audioList = ['Counter10.mp3',
                               'Counter9.mp3',
                               'Counter8.mp3',
                               'Counter7.mp3',
                               'Counter6.mp3',
                               'Counter5.mp3',
                               'Counter4.mp3',
                               'Counter3.mp3',
                               'Counter2.mp3',
                               'Counter1.mp3',]


import pygame
import time
import random

pygame.init()
pygame.mixer.init()

# Set up the drawing window

#screen = pygame.display.set_mode([500, 500])



def win():
    playsound('win.mp3')
    quit()
    global gameover
    gameover = True
    return

def main():
    mainMap.levelMap[playerCharacter.position[0]][playerCharacter.position[1]] = 'P' #initialize player on map
    updateMap(mainMap) #print map
    
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    listener.join()

def updateMap(currentMap):
    #print out map/update info
    #screen.fill((0, 0, 0))
    avgDistBomb = playerCharacter.DistanceFromBombs(mainMap.bombs)
    print("Average Distance From Bombs: " + str(playerCharacter.DistanceFromBombs(mainMap.bombs)))
    print("Is on bomb: " + str(playerCharacter.check_bomb()))
    print("Sound Playing : " + str(audioEventPlayer.currentSound))
    updateGeigerLevel(int(avgDistBomb))
    for x in range(mainMap.levelSize):
        for y in range(mainMap.levelSize):
            print('|' + str(currentMap.levelMap[x][y]) + '|', end='')
        print('')

def on_press(key):
    if playerCharacter.defusePos[0] > playerCharacter.position[0] or playerCharacter.defusePos[0] < playerCharacter.position[0] or playerCharacter.defusePos[1] > playerCharacter.position[1] or playerCharacter.defusePos[1] < playerCharacter.position[1]:
        playerCharacter.deactivateDefuse()
    #to move player
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['up', 'down', 'left', 'right']:  # arrow keys
        mainMap.levelMap[playerCharacter.position[0]][playerCharacter.position[1]] = '0' #change current player tile to be blank
        playerCharacter.move(k) #move player
        for i in range(mainMap.levelSize+3): #overwrite previous map
           print(LINE_UP, end=LINE_CLEAR) 
        mainMap.levelMap[playerCharacter.position[0]][playerCharacter.position[1]] = 'P' #change the tile at the new player position to be P
        updateMap(mainMap) #print out the map again
    if k in ['space']:
        defusePosition = []
        for value in playerCharacter.position:
            defusePosition.append(value)
        playerCharacter.activateDefuse(defusePosition)
    if k in ['r'] and gameover:
        gameover = False
    if playerCharacter.check_bomb():
        if playerCharacter.defuseOn == False and mainMap.bombAt(playerCharacter.position).isActive == True:
            playsound('explosion.mp3', False)
            gameover = True
            return False
        else:
            playerCharacter.defuse_bomb()
            global numBombsDefused
            numBombsDefused += 1
            if numBombsDefused == 3:
                win()
                return False

def updateGeigerLevel(level):
    if level > 10 or level == 0:
        audioGeigerPlayer.StopContinuous()
    else:
        audioGeigerPlayer.StopContinuous()
        audioGeigerPlayer.PlayContinuous(level-1)
            

main()  

#pygame.quit()