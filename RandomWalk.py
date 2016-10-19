import random

def rs():
    """ rs chooses a random step and returns it
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return random.choice([-1,1])


def rwpos(start, nsteps):
    currentPosition = start
    for i in range(nsteps):
        currentPosition = currentPosition + rs()
        print 'current position is '+ str(currentPosition)
    return currentPosition

rwpos(40,4)
