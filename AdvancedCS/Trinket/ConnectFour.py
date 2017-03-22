# python 2
#
# Problem Set 2, Problem 1
# Name:
#


class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """

    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [[' ']*W for row in range(H)]

        # we do not need to return inside a constructor!


    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        W = self.width
        H = self.height

        s = ''   # the string to return
        for row in range(0,H):
            s += '|'
            for col in range(0,W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*W+1) * '-'    # bottom of the board
        s += '\n'

        x = -1
        for i in range(W):
            if x == 9:
                x = 0
                s += " " +str(x)
            else:
                x+= 1
                s += " " + str(x)

        return s


    def addMove(self, col, XO):

        """
        Passing in column, the method checks each row of the column.
        If a space is empty, it checks the space below in the same column.
        Then, if the space in the next row (same column) is occupied,
        it moves an X or O (argument) into the above space.
        """
        type = XO
        counter = 0
        for i in range(self.height):
            value = self.data[i][col]
            if value == ' ':
                counter += 1
            elif value != ' ':  #If a space is occupied
                self.data[i-1][col] = type  #put an X or O in the space above
            if counter == self.height:  #If there are no spaces occupied in the column
                self.data[i][col] = type  #put and X or an O at the bottom of the column




    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'

            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.

            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'



    def allowsMove(self, c):
        """
        Returns True if you can make a move in column c.
        This means c is in the range of columns and the top space of column c is free.
        Returns False if you can't make a move in column c.
        This means c is out of the range of columns or column c is full.
        """
        if c > self.width:  #if column c is out of range
            return False
        elif c <= self.width:  #if column c is in range
            if self.data[c][0] != ' ':  #if the top of the column is occupied (something's wrong here)
                return False
            elif self.data[c][0] == ' ':  #if the top of the column is free (something's wrong here)
                return True
        else:
            return True



board = Board(6,7)
#print board
board.addMove(4,'X')
#print board
board.addMove(4,'O')
board.addMove(3,'O')
board.addMove(4,'X')
board.addMove(4,'O')
print board
