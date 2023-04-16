
import pygame
import time
import random

pygame.init()
pygame.mixer.init()

gridDisplay = pygame.display.set_mode((500, 500))
grid = []
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
start = [random.randint(0,9),random.randint(0,9)]
while (b1 == start or b2 == start or b3 == start or b4 == start or b5 == start):
    start = [random.randint(0,9),random.randint(0,9)]
grid = []
x = 0
while x <= 9:
    temp = []
    y = 0
    while y <= 9:
        if [x,y] == b1 or [x,y] == b2 or [x,y] == b3 or [x,y] == b4 or [x,y] == b5:
            temp.append(1)
        elif [x,y] == start:
            temp.append(2)
        else:
            temp.append(0)
        y+=1
    grid.append(temp)
    x+=1
for thing in grid:
    print(thing)
        
grid_node_width = 25
grid_node_height = 25
# Set up the drawing window

screen = pygame.display.set_mode([500, 500])

def border():
    touch_border.play(0)
    time.sleep(4)
    touch_border.stop()
    
def far():
    g1.play(0)
    time.sleep(4)
    g1.stop()
    
def near():
    g2.play(0)
    time.sleep(3)
    g2.stop()
    
def close():
    g3.play(0)
    time.sleep(2)
    g3.stop()
    
def clip():
    defuse.play(0)
    time.sleep(1)
    defuse.stop()
    
def explode():
    boom.play(0)
    time.sleep(2)
    boom.stop()

def createSquare(x, y, color):
    pygame.draw.rect(gridDisplay, color, [x, y, grid_node_width, grid_node_height])

def visualizeGrid():
    y = 0  # we start at the top of the screen
    for row in grid:
        x = 0 # for every row we start at the left of the screen again
        for item in row:
            if item == 0:
                createSquare(x, y, (255, 255, 255))
            elif item == 2:
                createSquare(x, y, (255, 0, 255))
            else:
                createSquare(x,y, (0,0,0))
            x += grid_node_width # for ever item/number in that row we move one "step" to the right
        y += grid_node_height   # for every new row we move one "step" downwards
    pygame.display.update()

# Run until the user asks to quit

running = True
while running:
    visualizeGrid()
    touch_border = pygame.mixer.Sound('border.mp3')
    g1 = pygame.mixer.Sound('counter1.mp3')
    g2 = pygame.mixer.Sound('counter2.mp3')
    g3 = pygame.mixer.Sound('counter3.mp3')
    defuse = pygame.mixer.Sound('cut.mp3')
    boom = pygame.mixer.Sound('explosion.mp3')


    # Did the user click the window close button?

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                if start[1] == 0:
                    border()
                else:
                    grid[start[0]][start[1]] = 0
                    grid[start[0]][start[1]-1] = 2
                    start[1] = start[1]-1
                    visualizeGrid()
            if event.key == pygame.K_UP or event.key == ord('w'):
                if start[0] == 0:
                    border()
                else:
                    grid[start[0]][start[1]] = 0
                    grid[start[0]-1][start[1]] = 2
                    start[0] = start[0]-1
                    visualizeGrid()
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                if start[1] == 9:
                    border()
                else:
                    grid[start[0]][start[1]] = 0
                    grid[start[0]][start[1]+1] = 2
                    start[1] = start[1]+1
                    visualizeGrid()
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                if start[0] == 9:
                    border()
                else:
                    grid[start[0]][start[1]] = 0
                    grid[start[0]+1][start[1]] = 2
                    start[0] = start[0]+1
                    visualizeGrid()


    # Fill the background with white

    screen.fill((255, 255, 255))

pygame.quit()
