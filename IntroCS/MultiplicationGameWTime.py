import random
import time

def play():
    for x in range(5):
        factor1 = random.randint(0,12+x)
        factor2 = random.randint(0,12+x)

        correctAnswer = factor1*factor2
        userAnswer=-1

        while userAnswer!= correctAnswer:

            # set time when problem displayed 
            time1 = time.time()

            userAnswer = raw_input("Please enter the product of "+ str(factor1)+" and "+str(factor2)+": ")

            # find time elapsed since problem displayed
            time2 = time.time()
            timeElapsed = time2 - time1

            try:
                userAnswer=int(userAnswer)
                if timeElapsed < 5:
                    if userAnswer == correctAnswer:
                        print "Correct"
                    else:
                        print "Incorrect"
                else:
                    if userAnswer == correctAnswer:
                        print "Correct, but you were too slow."
                    else:
                        print "Incorrect and you were too slow."
            except:
                print "I'll give you a hint: the answer is an integer."
                print "no letters, no decimals, just straight up numbers"
    again()

def again():
    print 'play again?'
    answer = raw_input("type yes or no"+": ")
    if answer == 'yes':
        play()
    elif answer == 'no':
        print 'game over'
    else:
        again()

def instructions():
    print "Let's see how well you know your multiplication tables"
    print "I'll give you two numbers and you answer with their product"

def main():
    instructions()
    play()


main()
