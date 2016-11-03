import random

def rs():
    """ rs chooses a random step and returns it
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return random.choice([0,1])

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
    numberX = int(width*height*percentX)
    numberY = int(width*height*percent0)
    numberO = width*height-numberY-numberX
    population = numberO*'0' + numberX*'X' + numberY*'Y'
    population = random.sample(population, width*height)
    oiii=0
    Z = createBoard(width,height)
    for r in range(width):
        for c in range(height):
            Z[r][c] = population[oiii]
            oiii = oiii + 1
    return Z


Z = unsegregatedBoard(10,10,0.30,.25)
printBoard(Z)





