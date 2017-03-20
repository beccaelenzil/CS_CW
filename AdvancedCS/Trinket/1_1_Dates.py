# python 2
#
# Problem Set 1, Problem 1: Dates
#
# Name: Colin Wood
#

class Date:
    """ a user-defined data structure that
        stores and manipulates dates
    """

    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """ the constructor for objects of type Date """
        self.month = month
        self.day = day
        self.year = year


    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
        return s


    # here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """ Returns True if the calling object is
            in a leap year; False otherwise. """
        if self.year % 400 == 0: return True
        elif self.year % 100 == 0: return False
        elif self.year % 4 == 0: return True
        return False


    def copy(self):
        """ Returns a new object with the same month, day, year
            as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        """ Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

    def tomorrow(self):
        if self.isLeapYear():
            February = 29
        else:
            February = 28

        DIM = [0, 31, February, 30, 31, 30, 31, 30, 31, 30, 31, 30, 31]

        self.day += 1

        if DIM[self.month] < self.day:
            self.month += 1
            self.day = 1
            if self.month == 13:
                self.year += 1
                self.month = 1

    def yesterday(self):
        if self.isLeapYear():
            February = 29
        else:
            February = 28

        DIM = [0, 31, February, 30, 31, 30, 31, 30, 31, 30, 31, 30, 31]

        self.day -= 1

        if self.day == 0:
            self.month -= 1
            self.day = DIM[self.month]
            if DIM[self.month] == 0:
                self.year -= 1
                self.month = 12
                self.day = 31

    def addNDays(self,N):
        for x in range(N):
            self.tomorrow()


    def subNDays(self,N):
        for x in range(N):
            self.yesterday()

    def isBefore(self, d2):
        if self.year < d2.year:
            return True
        elif self.year == d2.year:
            if self.month < d2.month:
                return True
            if self.month == d2.month:
                if self.day < d2.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


    def isAfter(self,d2):
        if self.year > d2.year:
            return True
        elif self.year == d2.year:
            if self.month > d2.month:
                return True
            if self.month == d2.month:
                if self.day > d2.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False



    def diff(self, d2):
        """
        something's wrong
        """
        x = 0
        date = self

        while not date.equals(d2):
            if date.isBefore(d2):
                date.tomorrow()
                x += 1
            elif date.isAfter(d2):
                date.yesterday()
                x -= 1
        return x


    #def dow(self):

