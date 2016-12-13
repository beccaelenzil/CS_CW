import math
import pygame
import random
pygame.init()

"""
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
SEACOLOR = (18,116,196)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Colin Learning Graphics")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



rect_x = 50
rect_y = 50
rect_x_change = 5
rect_y_change = 5
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop


    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    rect_x += rect_x_change
    rect_y+= rect_y_change

    if rect_x > 650 and rect_y > 450:
        rect_y_change = rect_y_change * -1
        rect_x_change = rect_x_change * -1
    elif rect_x > 650 and rect_y < 0:
        rect_y_change = rect_y_change * -1
        rect_x_change = rect_x_change * -1
    elif rect_x <0 and rect_y > 450:
        rect_y_change = rect_y_change * -1
        rect_x_change = rect_x_change * -1
    elif rect_x < 0 and rect_y <0:
        rect_y_change = rect_y_change * -1
        rect_x_change = rect_x_change * -1
    elif rect_y > 450:
        rect_y_change = rect_y_change * -1
    elif rect_x > 650:
        rect_x_change = rect_x_change * -1
    elif rect_y < 0:
        rect_y_change = rect_y_change * -1
    elif rect_x < 0:
        rect_x_change = rect_x_change * -1

    screen.fill(BLACK)

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

    """

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

snow_list = []
for i in range(50):
    x = random.randrange(0, 700)
    y = random.randrange(0, 500)
    snow_list.append([x, y])

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with bliting the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    for item in range(len(snow_list)):
        pygame.draw.circle(screen, WHITE, snow_list[item], 2)
        snow_list[item][1] += 1

        if snow_list[item][1] > 500:
            y = random.randrange(-50, -10)
            snow_list[item][1] = y
            x = random.randrange(0,400)
            snow_list[item][0] = x



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(20)

# Close the window and quit.
pygame.quit()
