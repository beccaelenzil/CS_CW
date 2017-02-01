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

aPlayer = Fish.Player(5,12)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

#SmallFish = pygame.image.load("SmallFish.png")
#SmallFish.set_colorkey(WHITE)


aPlankton = pygame.image.load("Plankton.png")
aPlankton.set_colorkey(WHITE)

#background = pygame.image.load("GameBackground.png")
background = pygame.image.load("SeaBackground.png")

aPlankton = Fish.plankton
#aPlankton.set_colorkey(WHITE)

collision = False

counter = 1
def spawnPlankton(Fish):
    i = counter
    if i == 1:
        screen.blit(Fish.image, (600,500))
        i+=1
    elif i > 1:
        x = random.randrange(100,1200)
        y = random.randrange(50, 650)
        screen.blit(Fish.image, (x,y))





def fishMoveRight(Fish):
            # type: (object) -> object
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
        elif collision == False:
            screen.blit(Fish.plankton.image, (600,500))
        elif collision == True:
            x = random.randrange(100,1200)
            y = random.randrange(50, 650)
            screen.blit(Fish.plankton.image, (x,y))

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

    screen.blit(aPlayer.image, [x-50, y-25])

    spawnPlankton(aPlankton)


    #fishMoveRight(Fish.rightPiranha)
    #fishMoveLeft(Fish.leftShark)
    #fishMoveLeft(Fish.leftPiranha)
    #fishMoveRight(Fish.rightShark)


    #Fish.plankton.rect = Fish.plankton.image.get_rect()
    #Fish.plankton.radius = Fish.plankton.image.get.radius()
    #Fish.smallFish.rect = Fish.smallFish.image.get_rect()

    #Fish.plankton.rect = pygame.Surface.get_rect(Fish.plankton.image)
    #Fish.smallFish.rect = pygame.Surface.get_rect(Fish.smallFish.image)
    print Fish.plankton.rect
    print aPlayer.rect

    #Fish.smallFish.radius = Fish.smallFish.image.get.radius()
    #def smallFishEat():
    #if pygame.sprite.collide_rect(aPlayer.rect, Fish.plankton.rect):
     #   spawnPlankton(Fish.plankton)
      #  print "yes"

 #   smallFishEat()

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)

pygame.quit()


