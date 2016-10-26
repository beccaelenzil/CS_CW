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


A = diagonalize(5, 5)
#printBoard(A)

def innerCells(w,h):
    A = createBoard(w, h)
    for row in range(1,h-1):
        for col in range(1,w-1):
            A[row][col]=1
    return A

A = innerCells(10,10)
#printBoard(A)
