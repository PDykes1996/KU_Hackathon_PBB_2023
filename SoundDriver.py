import pygame
from playsound import playsound
class SoundDriver:
    def __init__ (self):
        self.currentSound = None
        self.audioList = []
        
    def PlaySound(self, sound):
        self.currentSound = sound
        playsound(sound, False)

    def PlayContinuous(self,selection):
        self.currentSound = self.audioList[selection]
        pygame.mixer.music.load(self.currentSound)
        pygame.mixer.music.play(-1)
    def StopContinuous(self):
        pygame.mixer.music.stop()
         


