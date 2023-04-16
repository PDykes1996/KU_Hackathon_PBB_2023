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
mainMap = Level(10, 2)
playerCharacter = Player([0,0], mainMap)
gameover = False
audioEventPlayer = SoundDriver()
audioGeigerPlayer = SoundDriver()
def main():
    mainMap.levelMap[playerCharacter.position[0]][playerCharacter.position[1]] = '|P|' #initialize player on map
    updateMap(mainMap) #print map
    #audioPlayer.PlaySound("bombsound.mp3")



    while (1): #listen for key pressed from player 
        onBomb = playerCharacter.check_bomb()
        audioEventPlayer.PlaySound('bombsound.mp3')

        if playerCharacter.check_bomb(): #if the player is on a bomb
            #audioPlayer.PlaySound("bombsound.mp3")
            pygame.mixer.music.load('bombsound.mp3')
            pygame.mixer.music.play(0)
        listener = keyboard.Listener(on_press=on_press)
        listener.start()  # start to listen on a separate thread
        listener.join()


    print("gameover")

def updateMap(currentMap):
    #print out map
    print("Average Distance From Bombs: " + str(playerCharacter.DistanceFromBombs(mainMap.bombs)))
    print("Is on bomb: " + str(playerCharacter.check_bomb()))
    print("Sound Playing : " + str(audioPlayer.currentSound))
    for x in range(mainMap.levelSize):
        for y in range(mainMap.levelSize):
            print(currentMap.levelMap[x][y], end='')
        print('')

def on_press(key):
    #to move player
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['up', 'down', 'left', 'right']:  # arrow keys
        mainMap.levelMap[playerCharacter.position[0]][playerCharacter.position[1]] = '| |' #change current player tile to be blank
        playerCharacter.move(k) #move player
        for i in range(mainMap.levelSize+3): #overwrite previous map
           print(LINE_UP, end=LINE_CLEAR) 
        mainMap.levelMap[playerCharacter.position[0]][playerCharacter.position[1]] = '|P|' #change the tile at the new player position to be P
        updateMap(mainMap) #print out the map again
        '''
    if playerCharacter.check_bomb():
        if k in ['space']:
            mainMap.bombAt([playerCharacter.position[0], playerCharacter.position[1]]).BombDefusal()
        else:
            gameover = True
            '''


main()