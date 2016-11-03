
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

def diagonalize(width, height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A


A = diagonalize(10, 10)
#printBoard(A)

def innerCells(w,h):
    A = createBoard(w, h)
    for row in range(1,h-1):
        for col in range(1,w-1):
            A[row][col]=1
    return A

A = innerCells(10,10)
#printBoard(A)

def randomCells(w,h):
    A = createBoard(w, h)
    for row in range(1,h-1):
        for col in range(1,w-1):
            A[row][col]= rs()
    return A
A = randomCells(10,10)
#printBoard(A)


def copy(A):
    height = len(A)
    width = len(A[0])
    newA = createBoard(width,height)
    for row in range(height):
        for col in range(width):
            newA[row][col]= A[row][col]

    return newA

A = randomCells(5,5)
#printBoard(A)

newA = copy(A)
#printBoard(newA)

def innerReverse(A):
    height = len(A)
    width = len(A[0])
    newA = createBoard(width,height)
    for row in range(1, height-1):
        for col in range(1, width-1):
            if A[col][row] == 1:
                newA[col][row] = 0
            else:
                newA[col][row] = 1
    return newA

A = randomCells(5,5)
#printBoard(A)

newA = innerReverse(A)
#printBoard(newA)

def countNeighbors(row,col,A):
    neighborCount = 0
    for r in range(row-1, row+2):
        for c in range(col-1,col+2):
            neighborCount+= A[r][c]
    neighborCount-=A[row][col]
    return neighborCount

A = randomCells(5,5)

#printBoard(A)

#print countNeighbors(2,1,A)
#print countNeighbors(2,2,A)
#print countNeighbors(0,1,A)

def next_life_generation(A):
    """
    makes a copy of A and then advances one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays at 0.
    """
    newA=copy(A)
    height = len(A)
    width = len(A[0])
    for row in range(1,height-1):
        for col in range(1,width-1):
            neighborCount = countNeighbors(row, col, A)
            if neighborCount > 3:
                newA[row][col] = 0
            elif neighborCount < 2:
                newA[row][col] = 0
            elif neighborCount == 3:
                newA[row][col] = 1
    return newA

A = randomCells(10,10)
printBoard(A)
for x in range(10):
    A = next_life_generation(A)
    printBoard(A)
    print " "


