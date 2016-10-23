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

#rwsteps(25,0,50)

def rwposPlain(start, nsteps):
    currentPosition = start
    for i in range(nsteps):
        currentPosition = currentPosition + rs()
        return 'position is '+currentPosition



print rwposPlain(50, 1000)
