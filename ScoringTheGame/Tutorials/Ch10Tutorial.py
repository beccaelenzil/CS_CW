#DON'T HAVE A JOYSTICK TO DO THE END OF CH 10
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()


def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1+x,y,10,10], 0)

    # Legs
    pygame.draw.line(screen, BLACK ,[5+x,17+y], [10+x,27+y], 2)
    pygame.draw.line(screen, BLACK, [5+x,17+y], [x,27+y], 2)

    # Body
    pygame.draw.line(screen, RED, [5+x,17+y], [5+x,7+y], 2)

    # Arms
    pygame.draw.line(screen, RED, [5+x,7+y], [9+x,17+y], 2)
    pygame.draw.line(screen, RED, [5+x,7+y], [1+x,17+y], 2)


# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#pygame.mouse.set_visible(0)

# -------- Main Program Loop -----------
# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # --- Game logic should go here
   # pos = pygame.mouse.get_pos()


# Drawing section
    draw_stick_figure(screen, 500, 500)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3

        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed

    # Draw the stick figure
    screen.fill(WHITE)
    draw_stick_figure(screen, x_coord, y_coord)


    """
    def draw_snowman(screen, x, y):
        # Draw a circle for the head
        pygame.draw.ellipse(screen, WHITE, [35 + x, y, 25, 25])
        # Draw the middle snowman circle
        pygame.draw.ellipse(screen, WHITE, [23 + x, 20 + y, 50, 50])
        # Draw the bottom snowman circle
        pygame.draw.ellipse(screen, WHITE, [x, 65 + y, 100, 100])

    # Snowman in upper left
    draw_snowman(screen, 10, 10)

    # Snowman in upper right
    draw_snowman(screen, 300, 10)

    # Snowman in lower left
    draw_snowman(screen, 10, 300)
    """


    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()



    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
