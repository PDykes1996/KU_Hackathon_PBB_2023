import random
#from pygame import mixer
class Bomb:
    def __init__(self, bombPosition):
        self.icon = "!"
        self.bombPosition = bombPosition
        self.explosionSound = "bombsound.mp3"
        self.diffuseSound = ""
        self.isActive = True

    def BombExplosion(self):
        pygame.mixer.Sound.play(self.explosionSound)





