import random
from pygame import mixer
class Bomb:
    def __init__(self, bombPosition, isActive):
        self.icon = "|!|"
        self.bombPosition = bombPosition
        self.isActive = isActive
        self.explosionSound = "bombsound.mp3"
        self.diffuseSound = ""
    def BombExplosion(self):
        pygame.mixer.Sound.play(self.explosionSound)
    def BombDefusal(self):
        pygame.mixer.Sound.play(self.diffuseSound)






