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

pygame.mouse.set_visible(False)

minnow = pygame.image.load("Minnow.png")
minnow.set_colorkey(WHITE)
piranha = pygame.image.load("Piranha.png")


background = pygame.image.load("GameBackground.png")


class Fish():
    def __init__(self):
        self.size = ""
        self.speed = ""
        self.position = ""
        self.image = ""


piranha1 = Fish()
#piranha1=Fish(10,5,(-10,random.randint(0,717)),pygame.image.load("Piranha.png"))
piranha1.size = 10
piranha1.speed = 5
piranha1.position = (-10,random.randint(0,717))
piranha1.image = pygame.image.load("Piranha.png")
piranha1.quantity = 10

#print piranha1.image

shark1 = Fish()
shark1.size = 15
shark1.speed = 3
shark1.image = pygame.image.load("SHark1.png")
shark1.position = (-10,random.randint(0,717))
shark1.quantity = 10

piranha2 = Fish()
#piranha2=Fish(5,10,(-10,random.randint(0,717)),pygame.image.load("Piranha.png"))
piranha1.size = 5
piranha1.speed = 10
piranha1.position = (-10,random.randint(0,717))
piranha1.image = pygame.image.load("Piranha.png")

minnow1 = Fish()
minnow1.size = 2
minnow1.speed = 15
#minnow1.position = (1290,random.randint(0,717))
#minnow1.image =


shark1_list = []
for i in range(shark1.quantity):
    i = random
    x = random.randrange(0,1277)
    y = random.randrange(0, 717)
    shark1_list.append([x, y])

piranha1_list = []
for i in range(piranha1.quantity):
    i = random
    x = random.randrange(0,1277)
    y = random.randrange(0, 717)
    piranha1_list.append([x, y])

fish_list = []
for i in range(15):
    i = random
    x = random.randrange(0,1277)
    y = random.randrange(0,717)
    fish_list.append([x,y])


def fishMoveRight(Fish):
            for item in range(len(fish_list)):
                Fish_speed = Fish.speed + random.randint(-5,5)
                screen.blit(Fish.image, fish_list[item])
                fish_list[item][0]+= Fish_speed
                fish_list[item][1]+= random.randint(-3,3)

                if fish_list[item][0] > 1277:
                    x = random.randrange(-50,-10)
                    y = random.randrange(0,680)
                    fish_list[item][1] = y
                    fish_list[item][0] = x


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




    fishMoveRight(piranha1)

    fishMoveRight(shark1)


    # --- Go ahead and update the screen with what we've drawn.

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)

pygame.quit()


