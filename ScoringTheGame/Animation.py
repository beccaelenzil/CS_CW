import math
import pygame
pygame.init()

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
    """

    """
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()


