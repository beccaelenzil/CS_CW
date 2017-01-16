import random
import pygame
import time
pygame.init()

BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
SEACOLOR = (18,116,196)

size = (1277,717)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Early Game Graphics")



# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



minnow = pygame.image.load("Minnow.png")
minnow.set_colorkey(WHITE)
piranha = pygame.image.load("rightPiranha.png")


background = pygame.image.load("GameBackground.png")

fish_list = []
for i in range(20):
    x = random.randrange(0,1277)
    y = random.randrange(0, 717)
    fish_list.append([x, y])



# -------- Main Program Loop -----------

while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")


    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)



    screen.blit(background, [0, 0])
    #pygame.draw.rect(screen, SEACOLOR, [0,0,700,500],500)
    font = pygame.font.SysFont('Arial', 25, True, False)
    text = font.render("Minnow.io",True,BLACK)
    screen.blit(text, [570, 10])
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]

    # Copy image to screen:
    screen.blit(minnow, [x-50, y-25])


    """
    piranhas go horizontally across the screen with varying speeds
    """
    #pygame.transform.smoothscale(minnow,(25,25))
    for item in range(len(fish_list)):
        piranha_speed = random.randint(5,15)
        screen.blit(piranha, fish_list[item])
        fish_list[item][0]+= piranha_speed
        fish_list[item][1]+= random.randint(-3,3)

        if fish_list[item][0] > 1277:
            x = random.randrange(-50,-10)
            y = random.randrange(0,680)
            fish_list[item][1] = y
            fish_list[item][0] = x

    # --- Go ahead and update the screen with what we've drawn.

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)

pygame.quit()


