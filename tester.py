import random

def main():
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
    y = 0
    grid = [][]
    while x < 9:
        while y < 9:
            if [x][y] == b1 or [x][y] == b2 or [x][y] == b3 or [x][y] == b4 or [x][y] == b5:
                grid[x][y] = 1
            else:
                grid[x][y] = 0
                
                
main()
