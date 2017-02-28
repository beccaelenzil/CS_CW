import random
import pygame
#import Fish
import time
pygame.init()

class Fish(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super(self.__class__,self).__init__()
        self.size = ""
        self.speed = ""
        self.position = ""
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.list = []
        self.range = ""


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

WHITE = (255, 255, 255)
aPlankton = pygame.image.load("Plankton.png")
aPlankton.set_colorkey(WHITE)

plankton = Fish(50,45)
plankton.position = (random.randrange(0,1277), random.randrange(0, 717))
plankton.image = aPlankton
plankton.width = 10
plankton.height =5


rightPiranha = Fish(20,15)
rightPiranha.size = 10
rightPiranha.speed = 20
rightPiranha.image = pygame.image.load("rightPiranha.png")
rightPiranha.list = rightPiranha_list




leftShark = Fish(30,25)
leftShark.size = 15
leftShark.speed = 10
leftShark.image = pygame.image.load("leftShark.png")
leftShark.list = leftShark_list



leftPiranha = Fish(20,10)
leftPiranha.size = 5
leftPiranha.speed = 15
leftPiranha.image = pygame.image.load("leftPiranha.png")
leftPiranha.list = leftPiranha_list


rightShark = Fish(27,22)
rightShark.size = 15
rightShark.speed = 5
rightShark.image = pygame.image.load("rightShark.png")
rightShark.position = (-10,random.randint(0,717))
rightShark.list = rightShark_list


class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(self.__class__,self).__init__()
        self.size = 5
        self.image = pygame.image.load("SmallFish1.png")
        self.image_surface = pygame.Surface([width, height])
        self.rect = self.image.get_rect()


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

aPlayer = Player(100,70)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

#SmallFish = pygame.image.load("SmallFish1.png")
#SmallFish.set_colorkey(WHITE)



#background = pygame.image.load("GameBackground.png")
background = pygame.image.load("SeaBackground.png")



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

                if Fish.list[item][0] < -215:
                    x = random.randrange(1277,1300)
                    y = random.randrange(0,680)
                    Fish.list[item][1] = y
                    Fish.list[item][0] = x

collision = False

#if aPlayer.rect.colliderect(plankton.rect):
#    collision == True



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
            screen.blit(plankton.image, (600,500))
        elif collision == True:
            x = random.randrange(100,1200)
            y = random.randrange(50, 650)
            screen.blit(plankton.image, (x,y))

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

    spawnPlankton(plankton)

    fishMoveRight(rightPiranha)
    fishMoveLeft(leftShark)
    fishMoveLeft(leftPiranha)
    fishMoveRight(rightShark)


    #Fish.plankton.rect = Fish.plankton.image.get_rect()
    #Fish.plankton.radius = Fish.plankton.image.get.radius()
    #Fish.smallFish.rect = Fish.smallFish.image.get_rect()

    #Fish.plankton.rect = pygame.Surface.get_rect(Fish.plankton.image)
    #Fish.smallFish.rect = pygame.Surface.get_rect(Fish.smallFish.image)
    print plankton.rect
    print aPlayer.rect

    #Fish.smallFish.radius = Fish.smallFish.image.get.radius()


 #   smallFishEat()

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)

pygame.quit()


