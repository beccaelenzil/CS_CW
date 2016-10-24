import random

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
printBoard(I)

