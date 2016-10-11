import random


Slope = random.randint(0,10)
yIntercept = random.randint(0,10)

def play():
    x = raw_input("please select a number: ")
    compRule = Slope*int(x)+yIntercept
    print 'm('+str(int(x))+')+'+'b='+str(compRule)
    y = raw_input('Do you need another guess? ')
    if y == 'yes':
        play()
    elif y == 'no':
        GuessRule()

def GuessRule():
    z = raw_input('What do you think m is? ')
    if int(z) == Slope:
        print 'Good job!'
        q = raw_input('What do you think b is? ')
        if int(q) == yIntercept:
            print 'You win!'
    else:
        print 'Nope'
        print 'Try more numbers'
        play()



play()
