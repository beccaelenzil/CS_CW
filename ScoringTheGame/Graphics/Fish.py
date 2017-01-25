import pygame
import random


class Fish(pygame.sprite.Sprite):
    def __init__(self):
        super(Fish, self).__init__()
        self.size = ""
        self.speed = ""
        self.position = ""
        self.image = ""
        self.list = []
        self.range = ""

"""
aPlanktonFish = Fish()

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
"""

class plankton(Fish):
    def __init__(self):
        super(plankton,self).__init__()
        #plankton = Fish()
        plankton.position = (random.randrange(0,1277), random.randrange(0, 717))
        #plankton.range = 1
        plankton.list = createFishList(1)
        plankton.image = pygame.image.load("Plankton.png")




class rightPiranha(Fish):
    def __init__(self):
        super(rightPiranha,self).__init__()
        #rightPiranha = Fish()
        #rightPiranha=Fish(10,5,(-10,random.randint(0,717)),pygame.image.load("rightPiranha.png"))
        rightPiranha.size = 10
        rightPiranha.speed = 20
        #rightPiranha.position = (-10,random.randint(0,717))
        rightPiranha.image = pygame.image.load("rightPiranha.png")
        #rightPiranha.range = 10
        rightPiranha.list = createFishList(10)


class leftShark(Fish):
    def __init__(self):
        super(leftShark, self).__init__()
        #leftShark = Fish()
        leftShark.size = 15
        leftShark.speed = 10
        leftShark.image = pygame.image.load("leftShark.png")
        #leftShark.position = (-10,random.randint(0,717))
        #leftShark.range = 10
        leftShark.list = createFishList(10)


class leftPiranha(Fish):
    def __init__(self):
        super(leftPiranha, self).__init__()
        #leftPiranha = Fish()
        #piranha2=Fish(5,10,(-10,random.randint(0,717)),pygame.image.load("rightPiranha.png"))
        leftPiranha.size = 5
        leftPiranha.speed = 15
        #leftPiranha.position = (-10,random.randint(0,717))
        leftPiranha.image = pygame.image.load("leftPiranha.png")
        #leftPiranha.range = 5
        leftPiranha.list = createFishList(5)

class rightShark(Fish):
    def __init__(self):
        super(rightShark, self).__init__()
        rightShark.size = 15
        rightShark.speed = 5
        rightShark.image = pygame.image.load("rightShark.png")
        rightShark.position = (-10,random.randint(0,717))
        #rightShark.range = 5
        rightShark.list = createFishList(5)


def createFishList(aRange):
    list = []
    for i in range(aRange):
        #i = random
        x = random.randrange(0,1277)
        y = random.randrange(0, 717)
        list.append([x, y])

