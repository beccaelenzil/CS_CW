from random import *

def rs():
    """ rs chooses a random step and returns it
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return choice([-1,1])


def rwpos(start,nsteps):
    """
    input: the number you start with and the number of steps taken
    output: The position after each step
    """
    print 'start position is '+str(start)
    currentPosition = start
    for i in range(nsteps):
        currentPosition = currentPosition + rs()
        print 'current position is '+ str(currentPosition)
    return currentPosition


rwpos(0,10)

def rwsteps(start,lo,hi):
    """
    input: start position (start), lowest value of the range (lo), highest value of the range (hi)
    Based on the start position and the low and high, the function moves a character randomly either
    one space to the left or right. When the character touches either the low value or the high value,
    the computer tells you how many steps it took to hit the low or high.
    """
    currentPosition = start
    stepCount = 0

    leftSpaces = lo + start
    rightSpaces = hi-start
    print '|' + leftSpaces*' ' + '>-<-0'+rightSpaces*' ' +'|' + 'start position:' + str(currentPosition)
    while currentPosition in range(lo+1,hi):
        currentStep = rs()
        currentPosition = currentPosition + currentStep
        stepCount += 1
        if currentStep == 1:
            leftSpaces += 1
            rightSpaces -= 1
        else:
            leftSpaces -= 1
            rightSpaces += 1

        print '|' + leftSpaces*' ' + '>-<-0'+rightSpaces*' ' +'|' + 'position:' + str(currentPosition)

    print 'that took '+str(stepCount)+' steps'

rwsteps(5,0,10)


def rwposPlain(start, nsteps):
    """
    This function takes a start position and a number of steps and takes a step up 1 or down 1 randomly.
    After nsteps iterations, it returns the final position. It only prints the final position.
    """
    currentPosition = start
    for i in range(0,nsteps):
        currentPosition = currentPosition + rs()
    return currentPosition


print rwposPlain(0, 100)

def ave_signed_disp(numtrials):
    """
    Takes in number of sims of 100 steps
    Returns average distance from start
    """
    posList = []
    for n in range(numtrials):
        pos = rwposPlain(0,100)
        posList.append(pos)
    avePos = sum(posList)/float(numtrials)
    return avePos

print ave_signed_disp(1000)

def ave_sq_disp(numtrials):
    """
    Takes in number of sims of 100 steps
    Returns the square of the average distance from start
    """
    posList = []
    for n in range(numtrials):
        pos = rwposPlain(0,100)
        posList.append(pos**2)
    avePos = sum(posList)/float(numtrials)
    return avePos


print ave_sq_disp(1000)
