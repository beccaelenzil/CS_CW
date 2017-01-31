import pygame
import random


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





Plankton_list = []
for i in range(1):
    i = random
    x = random.randrange(100,1200)
    y = random.randrange(50, 650)
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

WHITE = (255, 255, 255)
aPlankton = pygame.image.load("Plankton.png")
aPlankton.set_colorkey(WHITE)

plankton = Fish(10,5)
plankton.position = (random.randrange(0,1277), random.randrange(0, 717))
plankton.list = Plankton_list
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
        self.image = pygame.image.load("SmallFish.png")
        self.image_surface = pygame.Surface([width, height])
        self.rect = self.image.get_rect()




