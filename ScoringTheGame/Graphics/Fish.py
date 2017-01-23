import pygame
import random

class Fish(pygame.sprite.Sprite):
    def __init__(self):
        super(Fish,self).__init__()
        self.size = ""
        self.speed = ""
        self.position = ""
        self.image = ""


Plankton_list = []
for i in range(1):
    i = random
    x = random.randrange(0,1277)
    y = random.randrange(0, 717)
    Plankton_list.append([x, y])


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


plankton = Fish()
plankton.position = (random.randrange(0,1277), random.randrange(0, 717))
plankton.list = Plankton_list
plankton.image = pygame.image.load("Plankton.png")


rightPiranha = Fish()
#rightPiranha=Fish(10,5,(-10,random.randint(0,717)),pygame.image.load("rightPiranha.png"))
rightPiranha.size = 10
rightPiranha.speed = 20
rightPiranha.position = (-10,random.randint(0,717))
rightPiranha.image = pygame.image.load("rightPiranha.png")
rightPiranha.quantity = 10
rightPiranha.list = rightPiranha_list

leftShark = Fish()
leftShark.size = 15
leftShark.speed = 10
leftShark.image = pygame.image.load("leftShark.png")
leftShark.position = (-10,random.randint(0,717))
leftShark.quantity = 10
leftShark.list = leftShark_list

leftPiranha = Fish()
#piranha2=Fish(5,10,(-10,random.randint(0,717)),pygame.image.load("rightPiranha.png"))
leftPiranha.size = 5
leftPiranha.speed = 15
leftPiranha.position = (-10,random.randint(0,717))
leftPiranha.image = pygame.image.load("leftPiranha.png")
leftPiranha.list = leftPiranha_list

rightShark = Fish()
rightShark.size = 15
rightShark.speed = 5
rightShark.image = pygame.image.load("rightShark.png")
rightShark.position = (-10,random.randint(0,717))
rightShark.quantity = 5
rightShark.list = rightShark_list
