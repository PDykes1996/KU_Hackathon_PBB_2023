import random
from player import Player

def main():
    player = Player((0,0), 10) #creating a new player... starting arbitrarily at position 0,0 and with mapsize 10 


    b1 = [random.randint(0,9),random.randint(0,9)]
    b2 = [random.randint(0,9),random.randint(0,9)]
    while (b1 == b2):
        b2 = [random.randint(0,9),random.randint(0,9)]
    b3 = [random.randint(0,9),random.randint(0,9)]
    while (b1 == b3 or b2 == b3):
        b3 = [random.randint(0,9),random.randint(0,9)]
    b4 = [random.randint(0,9),random.randint(0,9)]
    while (b1 == b4 or b2 == b4 or b3 == b4):
        b4 = [random.randint(0,9),random.randint(0,9)]
    b5 = [random.randint(0,9),random.randint(0,9)]
    while (b1 == b5 or b2 == b5 or b3 == b5 or b4 == b5):
        b5 = [random.randint(0,9),random.randint(0,9)]
    x = 0
    print(b1)
    print(b2)
    print(b3)
    print(b4)
    print(b5)
    grid = []
    while x <= 9:
        temp = []
        y = 0
        while y <= 9:
            if [x,y] == b1 or [x,y] == b2 or [x,y] == b3 or [x,y] == b4 or [x,y] == b5:
                temp.append(1)
            else:
                temp.append(0)
            y+=1
        grid.append(temp)
        x+=1
    


    while (1):
        for thing in grid:
            print(thing)

main()