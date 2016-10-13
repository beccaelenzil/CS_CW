import random

#Sets two variables, Slope and yIntercept, to be random numbers between 1 and 10
def setValues():
    Slope = random.randint(1,10)
    yIntercept = random.randint(1,10)
    inputOutput(Slope, yIntercept)

#Requests user input. Multiplies the input (an integer) by Slope and adds yIntercept to the product.
#Asks if the user needs to try more inputs in order to guess the Slope and yIntercept
#If the user says yes, the function will start over
#If the user says no, it will send the user to GuessRule()
def inputOutput(Slope, yIntercept):

    x = raw_input("please select a number: ")
    while x.isdigit() == False:
        x = raw_input("Only numbers. Please try again: ")

    compRule = Slope*int(x)+yIntercept
    print 'm('+str(int(x))+')+'+'b= '+str(compRule)
    print " "

    y = raw_input('Do you need to select another input? Enter yes or no: ')
    y = y.lower()
    while y != 'yes' and y!= 'no':
        y = raw_input('Do you need to select another input? Enter yes or no: ')

    if y == 'yes':
        inputOutput(Slope,yIntercept)
    elif y == 'no':
        GuessRule(Slope,yIntercept)


#Asks the user to guess what Slope is.
#If the user guesses incorrectly, he told to try more numbers and sent back to inputOutput()
#If the user guesses correctly, the user is asked what yIntercept is.
#If the user guesses yIntercept incorrectly, he is told to try more numbers and sent back to inputOutput()
#If the user is correct, the game is over, and the user is sent to playAgain()
def GuessRule(Slope,yIntercept):
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
            print ' '
            inputOutput(Slope,yIntercept)

    else:
        print 'Nope'
        print 'Try more numbers'
        inputOutput(Slope,yIntercept)

#Asks the user if he wants to play again
#If yes, user is sent back to inputOutput()
#If no, the game ends
def  playAgain():
    m = raw_input('Would you like to play again? Enter yes or no: ')
    m = m.lower()
    if m == 'yes':
    setValues()
    elif m == 'no':
        print "goodbye"
    while m != 'yes' and m!= 'no':
        raw_input('Would you like to play again? Enter yes or no: ')



#Gives user the instructions for the game and launches inputOutput()
def instructions():
    print "hi! Let's play a game."
    print "I'm thinking of two numbers, each between 1 and 10"
    print "You give me a number"
    print ' '
    print "You try to guess my numbers after I put your number into the form y=mx+b."
    print "m and b are my numbers, while x is yours."
    print "When you think you know my numbers, tell me you don't need more guesses by typing 'no' and you can try to guess them."
    print ' '
    print "You should be able to find the answer after one input for x."
    print " "

def main():
    instructions()
    setValues()

main()
