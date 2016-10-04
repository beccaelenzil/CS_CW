import random

def play():
    CompNum = random.randint(0,3)
    userAnswer = raw_input('Whats your guess? ')
    if userAnswer == CompNum:
        print 'NO WAY YOU ACTUALLY GOT IT'
    else:
        print 'nah'

def instructions():
    print "I'm thinking of a number between 1 and 100. Can you guess it?"
    print "type your guess (an integer) below"

def main():
    instructions()
    play()

main()
