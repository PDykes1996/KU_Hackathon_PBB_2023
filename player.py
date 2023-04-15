class Player:
    def __init__(self, position, mapSize):
        #initializes the player class
        self.position = position
        self.mapSize = mapSize

    def move(self, direction):
        if direction == "left" and self.position[1] > 0:
            self.position[1] -= 1
        elif direction == "right" and self.position[1] < self.mapSize-1:
            self.position[1] += 1
        elif direction == "down" and self.position[0] < self.mapSize-1:
            self.position[0] += 1
        elif direction == "up" and self.position[0] > 0:
            self.position[0] -= 1
        else:
            self.hit_wall()

    def hit_wall(self):
        #what happens when the player hits the wall
        print("e")