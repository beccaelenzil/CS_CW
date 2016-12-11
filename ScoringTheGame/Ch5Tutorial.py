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


"""
minnow = pygame.image.load("Minnow.png")
background = pygame.image.load("Background for Fish Game.jpg")
"""
# -------- Main Program Loop -----------
rect_x = 50
rect_y = 50
rect_x_change = 8
rect_y_change = 8
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        """
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
        """
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
    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, [0, 92], [600,500], 2)
    pygame.draw.line(screen, BLACK, [0, -7], [700, 465], 2)
    pygame.draw.line(screen, BLACK, [250,-7], [700, 298], 2)
    pygame.draw.line(screen, BLACK, [250,93], [700,395], 2)

    x_offset = 20
    y_offset = 20
    for i in range(200):
        x_offset+=25
        y_offset+=17
        pygame.draw.rect(screen,BLACK,[-45+x_offset,-45+y_offset,250,100],2)

    screen.blit(background, [0, 0])
    pygame.draw.rect(screen, SEACOLOR, [0,0,700,500],500)
    font = pygame.font.SysFont('Times New Roman', 25, True, False)
    text = font.render("Shark.io",True,BLACK)
    screen.blit(text, [290, 10])
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
    minnow.set_colorkey(WHITE)

    # Copy image to screen:
    #screen.blit(minnow, [x-100, y-75])
    # --- Go ahead and update the screen with what we've drawn.
    """
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()


