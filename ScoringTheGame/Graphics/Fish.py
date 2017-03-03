
#make it so the mouse moves slower and the player can't leave the screen
import random
import pygame

# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SEACOLOR = (18, 116, 196)

pygame.init()
# Setup the screen
screen_width = 1277
screen_height = 717
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Fish Game")
background = pygame.image.load("SeaBackground.png")

scorecount = 0
highScore = 0
#plankton image
plankton_image = pygame.image.load("Plankton.png")
plankton_image.set_colorkey(WHITE)


#player image
player_image_1 = pygame.image.load("SmallFish1.png")
player_image_1.set_colorkey(WHITE)

player_image_2 = pygame.image.load("SmallFish2.png")
player_image_2.set_colorkey(WHITE)

player_image_3 = pygame.image.load("SmallFish3.png")
player_image_3.set_colorkey(WHITE)

player_image_4 = pygame.image.load("SmallFish3.png")
player_image_4.set_colorkey(WHITE)

player_image_5 = pygame.image.load("SmallFish3.png")
player_image_5.set_colorkey(WHITE)

player_image_6 = pygame.image.load("SmallFish3.png")
player_image_6.set_colorkey(WHITE)


#shark_image
leftShark_image = pygame.image.load("leftShark.png")

rightShark_image = pygame.image.load("rightShark.png")

#piranha_image
leftPiranha_image = pygame.image.load("leftPiranha.png")

rightPiranha_image = pygame.image.load("rightPiranha.png")

#eaten sound
eaten_sound = pygame.mixer.Sound('laser5.ogg')



class Fish(pygame.sprite.Sprite):
    def __init__(self,aFishImage):
        """ Constructor. Pass in the image of the fish,
        and its x and y position. """

        # Call the parent class (Sprite) constructor
        super(Fish, self).__init__()

        self.image = aFishImage
        self.mask = pygame.mask.from_surface(self.image)
        self.fishType = ""
        self.speed = ""



        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()


    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screen_width)


    def reset_posXY(self,x,y):

    #Reset position to the top of the screen, at a random x location.
     #   Called by update() or the main program loop if there is a collision.

        self.rect.x = x
        self.rect.y = y


    def update(self):
        """ Called each frame. """
        if self.fishType == 'plankton':
        # Move block down one pixel
            self.rect.y += 12

            # If block is too far down, reset to top of screen.
            if self.rect.y > 750:
                self.reset_posXY(random.randrange(0,screen_width),0)

        elif self.fishType == 'right':
            self.rect.x += random.randint(7,15)
            self.rect.y += random.randint(-3,3)
            if self.rect.x > screen_width+200:
                self.reset_posXY(-200,random.randrange(0,screen_height))

        elif self.fishType == 'left':
            self.rect.x -= random.randint(5,10)
            self.rect.y += random.randint(-3,3)
            if self.rect.x < -200:
                self.reset_posXY(screen_width,random.randrange(0,screen_height))
            if scorecount >5 and scorecount<=10:
                self.rect.x -= random.randint(8,15)
                self.rect.y += random.randint(-5,5)
            elif scorecount > 10 and scorecount <= 15:
                self.rect.x -= random.randint(12,20)
                self.rect.y += random.randint(-5,5)
            elif scorecount > 20:
                self.rect.x -= random.randint(15,25)
                self.rect.y += random.randint(-10,10)



a_player_image = player_image_1

class Player(Fish):
    """ The player class derives from Fish, but overrides the 'update'
    functionality with new a movement function that will move the block
    with the mouse. """
    def __init__(self, player_image,x,y):
        super(Fish,self).__init__()
        self.image = a_player_image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y



    def update(self):

        self.fishType = "player"

        # Get the current mouse position. This returns the position
        # as a list of two numbers.


        #pygame.mouse.set_visible(False)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                #self.acc_y -= .5
                self.rect.y -= 20 #+ self.acc_y
            if event.key == pygame.K_DOWN:
                #self.acc_y += .5
                self.rect.y += 20 #+ self.acc_y
            if event.key == pygame.K_LEFT:
                #self.acc_x -= .5
                self.rect.x -= 20 #+ self.acc_x
            if event.key == pygame.K_RIGHT:
                #self.acc_x += .5
                self.rect.x += 20 #+ self.acc_x


        #print [self.acc_x, self.acc_y]

        # Fetch the x and y out of the list,
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location


    def reset_pos(self):
        self.rect.x = 0
        self.rect.y = 0

    def playerGrow(self):
        if scorecount == 0:
            player.image = player_image_1
        elif scorecount > 0 and scorecount <= 2:
            player.image = player_image_2
            #all_sprites_list.add(self)
        elif scorecount > 2 and scorecount <= 4:
            player.image = player_image_3


# This is a list of fish 'sprites.' Each fish in the program is
# added to this list. The list is managed by a class called 'Group.'
fish_list = pygame.sprite.Group()

# This is a list of every sprite. All fish and the player as well.
all_sprites_list = pygame.sprite.Group()

# function that creates list of any fishType
def fishList(aFishType,fishImage,aRange):
 for i in range(aRange):
    # This represents a fishType
    aFish = Fish(fishImage)
    aFish.fishType = aFishType

    # Set a random location for the fishType
    aFish.rect.x = random.randrange(screen_width)
    aFish.rect.y = random.randrange(screen_height)

    # Add the fishType to the list of objects
    #print aFishType
    fish_list.add(aFish)

    # Add to all sprites
    all_sprites_list.add(aFish)

    #print "loop: all_sprites_list:" + str(len(all_sprites_list.sprites()))

plankton_number = 0
fishList('plankton', plankton_image,3 + plankton_number)
fishList('right',rightPiranha_image,12)
fishList('right',rightShark_image,10)
fishList('left',leftShark_image,5)
fishList('left',leftPiranha_image,5)

player = Player(a_player_image, 0, 0)
all_sprites_list.add(player)




"""
# Debug lists
# print "all_sprites_list length" + str(len(all_sprites_list.sprites()))

# loop through the all_sprites_list and print out all the sprite groups
spriteListLen = len(all_sprites_list.sprites())
for i in range(spriteListLen):
    print "Sprite List: " + str(len(all_sprites_list.sprites())) + " is " + str(all_sprites_list.sprites())
"""

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

eaten = False



# -------- Main Program Loop -----------
while not done:
    # User did something
    for event in pygame.event.get():
        # If user clicked close
        if event.type == pygame.QUIT:
            # Flag that we are done so we exit this loop
            #highScore = highScore
            done = True

    #Copy pixels from the source surface (background_image) onto the screen
    screen.blit(background, [0, 0])
    # Calls update() method on every sprite in the list
    #all_sprites_list.update()
    # Draw all the spites
    all_sprites_list.draw(screen)
    # Calls update() method on every sprite in the list
    all_sprites_list.update()
    # player only eats plankton it has collided with
    # See if player has collided with plankton only

    fish_collided_list = []
        #pygame.sprite.spritecollide(player, fish_list, False)

    for item in fish_list:
        if pygame.sprite.collide_mask(player, item):
            fish_collided_list.append(item)



    # Check the list of collisions for just planktons.
    font = pygame.font.SysFont('Calibri', 50, True, False)

    for fish in fish_collided_list:
        if fish.fishType == "plankton":
            eaten += 1
            #print'eaten: ' + str(eaten) + ' plankton'
            eaten_sound.play()
            # Reset plankton to the top of the screen to fall again.
            fish.reset_pos()
            scorecount += 1
            player.playerGrow()


        else:
            eaten_sound.play()
            #nonglobal highscore
            if highScore <scorecount:
                highScore = scorecount
            scorecount = 0
            eaten = 0
            player.reset_pos()
            #fish.reset_posXY(1277,717)


    highScoreBoard = font.render("High Score: " + str(highScore), True, BLACK)
    screen.blit(highScoreBoard,[screen_width-285,10])
    scoreboard = font.render("Score: " + str(scorecount), True, BLACK)
    screen.blit(scoreboard,[10,10])






    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


    # Limit to 20 frames per second
    clock.tick(10)


pygame.quit()



