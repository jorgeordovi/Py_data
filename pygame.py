import pygame
# Initialize Pygame
pygame.init()
# Set up the display
display = pygame.display.set_mode((800, 600))
# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# Load the font
font = pygame.font.SysFont("Arial", 40)
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keyboard input
    keys = pygame.key.get_pressed()
    direction = [0, 0] # initialize direction to (0,0)
    if keys[pygame.K_UP]:
        direction[1] = -1
    elif keys[pygame.K_DOWN]:
        direction[1] = 1
    if keys[pygame.K_LEFT]:
        direction[0] = -1
    elif keys[pygame.K_RIGHT]:
        direction[0] = 1
    # Move snake
    x += direction[0]
    y += direction[1]
    head = (x, y)  # update head position
    body = [(x + 10), (y + 10)]   # create body rectangle
    for i in range(len(body)):     # draw rectangles for each cell in body
        rect = pygame.Rect(body[i][0], body[i][1], 20, 20)
        display.fill(GREEN, rect) 
    pygame.draw.rect(display, RED, pygame.Rect(x, y, 50, 50))      # draw head as red circle
    display.update()                                            # update screen
def isCollision(head, body):                       # check if collision occurs between snake and food
    return (head[0] < x + 30 and head[0] > x - 30) and \
           (head[1] < y + 30 and head[1] > y - 30)
def moveSnake():                      # function to move snake based on its direction
    global speed
    speed -= 2
    if abs(speed) <= 5:             # slow down when snake moves slowly
        speed *= 3
    else:
        speed = 6                 # reset movement speed after reaching minimum value
    x += speed * direction[0]
    y += speed * direction[1]
    checkCollision(head, body)       # detect collisions at every step
moveSnake()              # call moveSnake method repeatedly until quitting
