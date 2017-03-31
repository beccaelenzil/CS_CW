# File: Board.py
# Verions: Python 2.7.13
# Name: Colin Wood
# Date: 3/20/17
# Desc: PROG DESC
# Usage: Define a board and run hostGame [b = Board(7,6) / b.hostGame()]

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
        counter = -1

        for i in range(self.height):
            value = self.data[i-1][col]
            if value == ' ':
                counter += 1
        self.data[counter][col] = type




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
        if c >= self.width or c <0:  #if column c is out of range
            return False
        elif c <= self.width:  #if column c is in range
            if self.data[0][c] != ' ':  #if the top of the column is occupied
                return False
            elif self.data[0][c] == ' ':  #if the top of the column is free
                return True
        else:
            return True

    def isFull(self):
        """
        checks every row and column and checks if allowsMove is true
        or false in each column. If it's false, it returns true,
        meaning the board is full. If allowsMove returns True, it means
        there is a free space and the board is not full, which makes
        isFull return False.

        """
        for i in range(self.height):
            for i in range(self.width):
                if self.allowsMove(i) == False:
                    return True
                else:
                    return False

    def delMove(self,c):
        """
        Passing in column, the method checks, from top to bottom, all the spaces in a column.
        If a space is empty, nothing happens.
        The first time it finds a space that is not empty,
        it removes the occupant of the space (either X of O)
        """
        counter = 0
        for row in range(self.height):
            space = self.data[row][c]
            if space == ' ':
                counter += 1
            elif space != ' ':  #If a space is occupied
                self.data[row][c] = ' ' #put ' ' in the space
                break  #stop the loop because it doesn't need to make another action

    def winsFor(self, XO):
        """
        Checks horizontally for four in a row
        Checks vertically for four in a row
        Checks diagonally for four in a row
        """
        H = self.height
        W = self.width
        D = self.data
        win = False
        # check for horizontal wins
        for row in range(0,H):
            for col in range(0,W-3):
                if D[row][col] == XO and \
                   D[row][col+1] == XO and \
                   D[row][col+2] == XO and \
                   D[row][col+3] == XO:
                    win = True
        for row in range(0,H-3): #check vertical.
            for col in range(0,W):
                if D[row][col] == XO and \
                   D[row+1][col] == XO and \
                   D[row+2][col] == XO and \
                   D[row+3][col] == XO:
                    win = True

        for row in range(0,H-3): #diagonal down
            for col in range(0,W-3):
                if D[row][col] == XO and \
                   D[row+1][col+1] == XO and \
                   D[row+2][col+2] == XO and \
                   D[row+3][col+3] == XO:
                    win = True
        for row in range(3,H): #diagonal up
            for col in range(0,W-3):
                if D[row][col] == XO and \
                   D[row-1][col+1] == XO and \
                   D[row-2][col+2] == XO and \
                   D[row-3][col+3] == XO:
                    win = True
        return win

    def hostGame(self):
        """
        Hosts a game of connect four using previous methods
        """
        print 'Welcome to  connect four. Player 1 is X and player 2 is O. Please decide who is who.'
        gameOver = False
        playerCount = 1 #To check who's turn it is
        while gameOver == False:
            print self.__repr__()
            if self.winsFor('X'):  #If X gets four in a row
                print 'player 1, you win!'
                break  #get out of the loop here so nothing else prints
            elif self.winsFor('O'):  #If O gets four in a row
                print 'player 2, you win!'
                break

            XO = 'X'
            if playerCount%2 != 0: #If the player count is not divisible by 2, it's player 1's turn
                XO = 'X'
            elif playerCount%2 == 0: #If the player count is divisible by 2, it's player 2's turn
                XO = 'O'

            users_col = -1
            while self.allowsMove(users_col) == False:
                users_col = input(XO + ", please choose a column: ")
            self.addMove(users_col, XO)

            playerCount += 1  #add one to player count after ever move


