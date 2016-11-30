import random

def instructions():
    print 'Welcome to Camel!'
    print 'You have stolen a camel to make your way across the great Mobi desert.'
    print 'The natives want their camel back and are chasing you down! Survive your'
    print 'desert trek and out run the natives.'
    Camel()




def Camel():
    milesTraveled = 0
    thirst = 0
    camelTiredness = 0
    nativeDistance = 20
    drinksLeft = 3
    done = False
    while done == False:
        print 'A: Drink from your canteen.'
        print 'B: Ahead moderate speed.'
        print 'C: Ahead full speed.'
        print 'D: Stop for the night.'
        print 'E: Status check.'
        print 'Q: Quit.'
        choice = raw_input('Select an option: A, B, C, D, E, or Q:  ')

        if choice == 'A':

        elif choice == 'B':

        elif choice == 'C':

        elif choice == 'D':
            camelTiredness = 0
            nativeDistance = nativeDistance - random.randint(7,14)
            print 'The camel is happy and energized'
        elif choice == 'E':
            print 'Miles traveled: ', milesTraveled
            print 'Drinks in canteen: ', drinksLeft
            print 'The natives are ', nativeDistance, ' miles behind you.'
        elif choice == 'Q':
            done = True
        elif choice not in ['A','B','C','D','E','Q']:
            "Next time, please choose one of the options"



instructions()
