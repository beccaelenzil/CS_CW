from Board import Board
import random



class Player:

    """ an AI player for Connect Four """

    def __init__( self, ox, tbt, ply ):
        """ the constructor """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s

    def oppCh(self):
        """ return the opposing player's type, X or O """
        if self.ox == 'X':
            return 'O'
        else:
            return 'X'


    def scoreBoard(self, b):
        """
        If the player wins, the player score is 100.
        If the opposing player wins, the player score is 0.
        If no one has one yet, the player score is 50
        """
        if b.winsFor(self.ox):
            return 100.0
        if b.winsFor(self.oppCh()):
            return 0.0
        else:
            return 50.0

    def tiebreakMove(self, scores):
        """
        Analyzes the resulting score of every possible move on a board.
        Returns the column that results in the highest score.
        If there is more than one maximum score, it decides which score to
        choose based on self.tbt
        """
        maxIndices = []  #List of columns with max scores
        for i in range(len(scores)):  #Look through all the scores
            if scores[i] == max(scores):  #Find the max score(s)
                maxIndices.append(i)  #Add max score(s) to maxIndices

        if len(maxIndices)>1:  #Pick which move to play based on self.tbt
            if self.tbt == 'LEFT':
                return maxIndices[0]
            elif self.tbt == 'RIGHT':
                return maxIndices[len(maxIndices)-1]
            else:
                return maxIndices[random.randrange(len(maxIndices))]
        else:
            return maxIndices[0]


    def scoresFor(self, b):
        scores = [50] * b.width
        for i in range(len(scores)):
            if b.allowsMove(i) == False:
                scores[i] = -1
            else:
                if winsFor()





#b = Board(6,7)
#b.hostGame()
