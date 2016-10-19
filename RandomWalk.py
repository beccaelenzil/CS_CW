from random import *

def rs():
    """ rs chooses a random step and returns it
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return choice([-1,1])


def rwpos(start,nsteps):
    print 'start position is '+str(start)
    currentPosition = start
    for i in range(nsteps):
        currentPosition = currentPosition + rs()
        print 'current position is '+ str(currentPosition)
    return currentPosition


#rwpos(0,10)

def rwsteps(start,lo,hi):
    currentPosition = start
    stepCount = 0

    leftSpaces = (start-lo)+1
    rightSpaces = (hi-lo)-start

    while currentPosition in range(lo,hi):
        currentStep = rs()
        currentPosition = currentPosition + currentStep
        stepCount += 1
        if currentStep == 1:
            leftSpaces += 1
            rightSpaces -= 1
        else:
            leftSpaces -= 1
            rightSpaces += 1

        print '|' + leftSpaces*' ' + '0->-<'+rightSpaces*' ' +'|'
        print str(stepCount)+' steps'
        print 'current position is ' + str(currentPosition)
    print 'that took '+str(stepCount)+' steps'

rwsteps(5,1,10)
