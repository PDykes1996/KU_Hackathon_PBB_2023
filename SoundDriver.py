import pygame
from playsound import playsound
class SoundDriver:
    def __init__ (self):
        self.currentSound = None
        
    def PlaySound(self, sound):
        self.currentSound = sound
        playsound(sound, False)
    def PlayContinuous(self,sound):
        self.currentSound = sound
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(-1)
         


