import random
import pygame
import Fish
import time
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SEACOLOR = (18, 116, 196)

size = (1277, 717)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Early Game Graphics")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

minnow = pygame.image.load("Minnow.png")
#user = pygame.image.load("SmallFish.png")
#user.set_colorkey(WHITE)
minnow.set_colorkey(WHITE)




#background = pygame.image.load("GameBackground.png")
background = pygame.image.load("SeaBackground.png")

#aPlankton = Fish()
#aPlankton.set_colorkey(WHITE)


def spawnPlankton(Fish):
    for item in range(len(Fish.list)):
        screen.blit(Fish.image, Fish.list[item])
    if minnow == Fish.list[item]:
        spawnPlankton(Fish)



def fishMoveRight(Fish):
            for item in range(len(Fish.list)):
                Fish_speed = Fish.speed + random.randint(-5,5)
                screen.blit(Fish.image, Fish.list[item])
                Fish.list[item][0]+= Fish_speed
                Fish.list[item][1]+= random.randint(-3,3)

                if Fish.list[item][0] > 1277:
                    x = random.randrange(-50,-10)
                    y = random.randrange(0,680)
                    Fish.list[item][1] = y
                    Fish.list[item][0] = x

def fishMoveLeft(Fish):
            for item in range(len(Fish.list)):
                Fish_speed = Fish.speed + random.randint(-5,5)
                screen.blit(Fish.image, Fish.list[item])
                Fish.list[item][0]-= Fish_speed
                Fish.list[item][1]+= random.randint(-3,3)

                if Fish.list[item][0] < -50:
                    x = random.randrange(1277,1300)
                    y = random.randrange(0,680)
                    Fish.list[item][1] = y
                    Fish.list[item][0] = x

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
            pygame.mixer.init
            pygame.mixer.music.load('laser5.ogg')
            pygame.mixer.music.play()

    screen.fill(WHITE)

    screen.blit(background, [0, 0])
    #pygame.draw.rect(screen, SEACOLOR, [0,0,700,500],500)
    font = pygame.font.SysFont('Arial', 25, True, False)
    text = font.render("Fish.io",True,BLACK)
    screen.blit(text, [570, 10])
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]

    # Copy image to screen:
    #screen.blit(minnow, [x-50, y-25])
    screen.blit(minnow, [x-50, y-25])


    """
    piranhas go horizontally across the screen with varying speeds
    """
    #pygame.transform.smoothscale(minnow,(25,25))

    spawnPlankton(Fish.plankton)
    fishMoveRight(Fish.rightPiranha)
    fishMoveLeft(Fish.leftShark)
    fishMoveLeft(Fish.leftPiranha)
    fishMoveRight(Fish.rightShark)


    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)

pygame.quit()


