"""
pygame simulation of game of life
"""

import random
import time
import pygame
from SegregationModel import *

width = 50
height = 50
cell_size = 9
spacing = 1
percentX = .4
percentY = .4
thresh = .6

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
BLUE = (0,0,225)

screen_width = (height+2)*(cell_size+spacing)
screen_height = (width+2)*(cell_size+spacing)

pygame.init()

# Set the width and height of the screen [width, height]
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Segregation Model")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def drawBoard(A,width,height,cell_size,spacing):
    #A = createBoard(width,height)
    for row in range(height+2):
        x_pos = row*(cell_size+spacing)
        for col in range(width+2):
            y_pos = col*(cell_size+spacing)
            if A[row][col] == 'X':
                pygame.draw.rect(screen, RED, [x_pos,y_pos,cell_size,cell_size])
            elif A[row][col] == 'Y':
                pygame.draw.rect(screen, BLUE,[x_pos,y_pos,cell_size,cell_size])
            elif A[row][col] == '0':
                pygame.draw.rect(screen, WHITE,[x_pos,y_pos,cell_size,cell_size])
            else:
                pygame.draw.rect(screen, BLACK,[x_pos,y_pos,cell_size,cell_size])


A = unsegregatedBoard(width,height,percentX,percentY)
drawBoard(A,width,height,cell_size,spacing)
pygame.display.flip()
static = False
generationCount = 1
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        #generationCount= generationCount+1
        if event.type == pygame.QUIT:
            done = True

    drawBoard(A,width,height,cell_size,spacing)
    while static == False:
        generationCount = generationCount+1
        [static,A] = nextGeneration(A,thresh)

        print generationCount
    #print segregationIndex(width,height,A)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
