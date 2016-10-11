import random


Slope = random.randint(1,10)
yIntercept = random.randint(1,10)

def inputOutput():
    x = raw_input("please select a number: ")
    while x.isdigit() == False:
        x = raw_input("Only numbers please. Please select a number: ")

    compRule = Slope*int(x)+yIntercept
    print 'm('+str(int(x))+')+'+'b= '+str(compRule)

    y = raw_input('Do you need another guess? Enter yes or no: ')
    y = y.lower()
    while y != 'yes' and y!= 'no':
        y = raw_input('Do you need another guess? Enter yes or no: ')


    if y == 'yes':
        inputOutput()
    elif y == 'no':
        GuessRule()



def GuessRule():
    z = raw_input('What do you think m is? ')
    while z.isdigit() == False:
        z = raw_input('m is an integer. What do you think m is? ')
    if int(z) == Slope:
        print 'Good job!'
        q = raw_input('What do you think b is? ')
        while q.isdigit() == False:
            q = raw_input('b is an integer. What do you think b is? ')
        if int(q) == yIntercept:
            print 'You win!'
            playAgain()
        else:
            print 'Nope'
            print 'Try more numbers'
            inputOutput()

    else:
        print 'Nope'
        print 'Try more numbers'
        inputOutput()

def  playAgain():
    m = raw_input('Would you like to play again? Enter yes or no: ')
    m = m.lower()
    if m == 'yes':
        inputOutput()
    elif m == 'no':
        print "goodbye"
    while m != 'yes' and m!= 'no':
        raw_input('Would you like to play again? Enter yes or no: ')




def instructions():
    print "hi! Let's play a game."
    print "I'm thinking of two numbers, each between 1 and 10"
    print "You give me a number"
    print "You try to guess my numbers after I put your number into the form mx+b."
    print "m and b are my numbers, while x is yours."
    print "When you think you know my numbers, tell me you don't need more guesses by typing 'no' and you can try to guess them."
    inputOutput()


instructions()
