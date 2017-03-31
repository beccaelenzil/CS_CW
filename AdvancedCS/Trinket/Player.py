from Board import Board



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
        If the player wins, the plaer score is 100.
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
        max(scores)



