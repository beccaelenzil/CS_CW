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
piranha = pygame.image.load("rightPiranha.png")


background = pygame.image.load("GameBackground.png")



class Fish():
    def __init__(self):
        self.size = ""
        self.speed = ""
        self.position = ""
        self.image = ""

leftShark_list = []
for i in range(3):
    i = random
    x = random.randrange(0,1277)
    y = random.randrange(0, 717)
    leftShark_list.append([x, y])

rightPiranha_list = []
for i in range(5):
    i = random
    x = random.randrange(0,1277)
    y = random.randrange(0, 717)
    rightPiranha_list.append([x, y])

leftPiranha_list = []
for i in range(5):
    i = random
    x = random.randrange(0,1277)
    y = random.randrange(0, 717)
    leftPiranha_list.append([x, y])

rightShark_list = []
for i in range(3):
    i = random
    x = random.randrange(0,1277)
    y = random.randrange(0, 717)
    rightShark_list.append([x, y])


rightPiranha = Fish()
#rightPiranha=Fish(10,5,(-10,random.randint(0,717)),pygame.image.load("rightPiranha.png"))
rightPiranha.size = 10
rightPiranha.speed = 5
rightPiranha.position = (-10,random.randint(0,717))
rightPiranha.image = pygame.image.load("rightPiranha.png")
rightPiranha.quantity = 10
rightPiranha.list = rightPiranha_list

#print rightPiranha.image

leftShark = Fish()
leftShark.size = 15
leftShark.speed = 5
leftShark.image = pygame.image.load("leftShark.png")
leftShark.position = (-10,random.randint(0,717))
leftShark.quantity = 10
leftShark.list = leftShark_list

leftPiranha = Fish()
#piranha2=Fish(5,10,(-10,random.randint(0,717)),pygame.image.load("rightPiranha.png"))
leftPiranha.size = 5
leftPiranha.speed = 10
leftPiranha.position = (-10,random.randint(0,717))
leftPiranha.image = pygame.image.load("leftPiranha.png")
leftPiranha.list = leftPiranha_list

rightShark = Fish()
rightShark.size = 15
rightShark.speed = 7.5
rightShark.image = pygame.image.load("rightShark.png")
rightShark.position = (-10,random.randint(0,717))
rightShark.quantity = 5
rightShark.list = rightShark_list


minnow1 = Fish()
minnow1.size = 2
minnow1.speed = 15
#minnow1.position = (1290,random.randint(0,717))
#minnow1.image =







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




    fishMoveRight(rightPiranha)

    fishMoveLeft(leftShark)

    fishMoveLeft(leftPiranha)

    fishMoveRight(rightShark)


    # --- Go ahead and update the screen with what we've drawn.

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)

pygame.quit()


