import random

def rs():
    """ rs chooses a random step and returns it
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return random.choice([-1,1])


def rwpos(start, nsteps):
    for x in range(nsteps):
        x = x + rs()
        return x + start
        print 'current position is '+x

rwpos(40,4)
