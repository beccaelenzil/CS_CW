import random
import time

def play():
    for x in range(5):
        factor1 = random.randint(0,12)
        factor2 = random.randint(0,12)

        correctAnswer = factor1*factor2
        userAnswer=-1
        while userAnswer!= correctAnswer:
            userAnswer = raw_input("Please enter the product of "+ str(factor1)+" and "+str(factor2)+": ")
            try:
                userAnswer=int(userAnswer)
                if userAnswer == correctAnswer:
                    print "Nice"
                else:
                    print "You absolute waste of space."
                    print "try again"
            except:
                print "Are you dumb? I'll give you a hint: the answer is an integer."
                print "meaning 1,2,3,4,..."
                print "no letters, no decimals, just straight up numbers"

def instructions():
    print "Let's see if you know how to do 1st grade math"
    print "I'll give you two numbers and you answer with their product"

def main():
    instructions()
    play()

main()
