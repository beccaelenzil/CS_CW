# *** SAMIC Version ***
# I used this as a reference
# http://programarcadegames.com/python_examples/show_file.php?file=moving_sprites.py
#

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
pygame.display.set_caption("Fish Game Sami")
background = pygame.image.load("SeaBackground.png")

#plankton image
plankton_image = pygame.image.load("Plankton.png")
plankton_image.set_colorkey(WHITE)

#player image
player_image = pygame.image.load("SmallFish.png")
player_image.set_colorkey(WHITE)

#shark_image
leftShark_image = pygame.image.load("leftShark.png")

#piranha_image
leftPiranha_image = pygame.image.load("leftPiranha.png")

#eaten sound
eaten_sound = pygame.mixer.Sound('laser5.ogg')

class Fish(pygame.sprite.Sprite):
    def __init__(self,aFishImage):
        """ Constructor. Pass in the image of the fish,
        and its x and y position. """

        # Call the parent class (Sprite) constructor
        super(Fish, self).__init__()

        self.image = aFishImage
        self.fishType = ""

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
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.x = random.randrange(0,x)
        self.rect.y = random.randrange(0,y)

    def update(self):
        """ Called each frame. """

        # Move block down one pixel
        self.rect.y += 1

        # If block is too far down, reset to top of screen.
        if self.rect.y > 410:
            self.reset_pos()

     #TODO option to create an updateXY(self,x,y): update top to bottom or left to right


    # TODO def fishMove(Fish,params): that can be used by any instance(type) of FISH, player type


class Player(Fish):
    """ The player class derives from Fish, but overrides the 'update'
    functionality with new a movement function that will move the block
    with the mouse. """
    def update(self):

        self.fishType = "player"

        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()

        # Fetch the x and y out of the list,
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]


# This is a list of fish 'sprites.' Each fish in the program is
# added to this list. The list is managed by a class called 'Group.'
fish_list = pygame.sprite.Group()

# This is a list of every sprite. All fish and the player as well.
all_sprites_list = pygame.sprite.Group()

# function that creates list of any fishType
def fishList(aFishType,fishImage,aRange):
<<<<<<< Updated upstream
 for i in range(aRange):
    # This represents a fishType
    aFish = Fish(fishImage)
    aFish.fishType = aFishType

    # Set a random location for the fishType
    aFish.rect.x = random.randrange(screen_width)
    aFish.rect.y = random.randrange(screen_height)

    # Add the fishType to the list of objects
    fish_list.add(aFish)
=======
    for i in range(aRange):
        # This represents a fishType
        aFish = Fish(fishImage)
        aFish.fishType = aFishType

        # Set a random location for the fishType
        aFish.rect.x = random.randrange(screen_width)
        aFish.rect.y = random.randrange(screen_height)

        # Add the fishType to the list of objects
        if aFishType == 'plankton':
            Plankton_list.add(aFish)
        elif aFishType == 'Fish':
            Fish_list.add(aFish)
>>>>>>> Stashed changes

    # Add to all sprites
    all_sprites_list.add(aFish)

    #print "loop: all_sprites_list:" + str(len(all_sprites_list.sprites()))


#create fishTypeLists
fishList('plankton',plankton_image,10)
fishList('leftShark',leftShark_image,5)
fishList('leftPirahana',leftPiranha_image,5)


# Create a Fish.Player
player = Player(player_image)
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
            done = True

    # Clear the screen
    screen.fill(WHITE)

    #Copy pixels from the source surface (background_image) onto the screen
    screen.blit(background, [0, 0])

    # Calls update() method on every sprite in the list
    all_sprites_list.update()

    """
    # TODO could update all sprites that are plankton & player from top to bottom,
    #  all other fish sprites update from left/right
    # Example only
    for sprite in all_sprites_list:
       if sprite.fishType == "plankton" or "player":
            sprite.updateXY(400,1)
       else: # all other fish types
            sprite.updateXY(1277,717)
    """


    """
    # player eats all fish it has collided with

    # See if the player has collided with any fish.
    fish_eaten_list = pygame.sprite.spritecollide(player, fish_list, False)

    # Check the list of all collisions.

    for fish in fish_eaten_list:
        print fish.fishType
        eaten += 1
        print(eaten)
        eaten_sound.play()

        # Reset fish to the top of the screen to fall again.
        fish.reset_pos()
     """

    # player only eats plankton it has collided with
    # See if player has collided with plankton only
    fish_collided_list = pygame.sprite.spritecollide(player, fish_list, False)

    # Check the list of collisions for just planktons.
    for fish in fish_collided_list:
        if fish.fishType == "plankton":
            eaten += 1
            print(fish.fishType + " eat " + str(eaten))
            eaten_sound.play()
            # Reset fish to the top of the screen to fall again.
            fish.reset_pos()

        else:
            # TODO once player has collided with a non plankton, remove it from the collision list
            print(fish.fishType + " not eaten ")
            fish.reset_pos()

            #reset position for leftShark (per example)
            #fish.reset_posXY(1277,717)

    # Draw all the spites
    all_sprites_list.draw(screen)

    # Limit to 20 frames per second
    clock.tick(20)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()



