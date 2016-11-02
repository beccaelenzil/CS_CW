from random import *

def rs():
    """ rs chooses a random step and returns it
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return choice([0,1])

def createOneRow(width):
    """ returns one row of zeros of width "width"...
         You should use this in your
         createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row

#print createOneRow(10)


def createBoard(width, height):
    """
    returns "height" rows of zeros of width "width"...
    """
    I = []
    for i in range(height):
        I += [createOneRow(width)]
    return I


def printBoard(I):
    for row in I:
        line = ''
        for col in row:
            line += str(col)
        print line

I = createBoard(5,5)
#printBoard(I)

def unsegregatedBoard(width,height,percentX,percent0):
    Z = createBoard(width,height)
    numberX = width*height*percentX
    numberO = width*height*percent0
    for row in range(1,height-1):
        for col in range(1,width-1):
            Z[row][col]= random.choice()
    return Z





