import random

def play():
    CompNum = random.randint(1,100)
    userAnswer = -1
    GuessCount = 0
    while userAnswer != CompNum:
        try:
            userAnswer = int(raw_input('Whats your guess? '))
            if userAnswer < CompNum:
                print 'Too low'
                GuessCount = GuessCount + 1
            elif userAnswer > CompNum:
                print 'Too high'
                GuessCount = GuessCount + 1
            elif userAnswer == CompNum:
                print 'good job!'
                GuessCount = GuessCount + 1
                print 'You found the answer after '+str(GuessCount)+' guesses'
        except:
            print 'a number, please'
            GuessCount = GuessCount + 1

def instructions():
    print "I'm thinking of a number between 1 and 100. Can you guess it?"
    print "type your guess (an integer) below"

def main():
    instructions()
    play()

main()
