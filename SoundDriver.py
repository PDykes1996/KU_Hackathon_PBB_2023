import pygame
class SoundDriver:
    def __init__ (self):
        self.currentSound = None
        
    def PlaySound(self, sound):
        self.currentSound = sound
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(0)
    def PlayContinuous(self,sound):
        self.currentSound = sound
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(-1)
         


