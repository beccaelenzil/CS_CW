def power(b,p):

    """
    b=base
    p=exponent
    """
    if p == 0:
        return 1
    result = 1
    for x in range (p):
        result = result*b
    return result
print power(5,2)
print power(1000,0)
print power(2,6)


def summedodds(L):
    """
    :param L: list of numbers
    :return: sum of odd numbers in list
    """
    result = 0
    for e in L:
        result = result + e
    return result
print summedodds([5,6,7])
print summedodds(range(3,10))

def mult(n,m):
    """
    :param n: integer
    :param m: integer
    :return: n*m
    """
    result = 0
    if m>0:
        for x in range(0,m):
            result = result + n
        return result

    elif m<0:
        for x in range (m,0):
            result = result - n
        return result

    else:
        return 0

print "mult(6,7)    42 ==", mult(6,7)
print "mult(6,-7)  -42 ==", mult(6,-7)
print "mult(-6,7)  -42 ==", mult(-6,7)
print "mult(-6,-7)  42 ==", mult(-6,-7)
print "mult(6,0)     0 ==", mult(6,0)
print "mult(0,7)     0 ==", mult(0,7)
print "mult(0,0)     0 ==", mult(0,0)



def dot(L,K):
    """
    :param L: list
    :param K: list
    :return: dot product of L and K: L1*K1 + L2*K2
    """
    result = 0
    if len(L)!= len(K):
        return 0
    else:
        for x in range(len(K)):
            result = result + L[x]*K[x]
        return result

print "dot( [5,3], [6,4] )     42.0 ==", dot( [5,3], [6,4] )
print "dot( [1,2,3,4], [10,100,1000,10000] )  43210.0 ==", dot( [1,2,3,4], [10,100,1000,10000] )
print "dot( [5,3], [6] )        0.0 ==", dot( [5,3], [6] )
print "dot( [], [6] )           0.0 ==", dot( [], [6] )
print "dot( [], [] )            0.0 ==", dot( [], [] )


def countevens(L):
    result = 0
    for x in L:
        if x%2 == 0:
            result = result + 1
    return result

print "countevens([2, 1, 2, 3, 4], 3 == ", countevens([2, 1, 2, 3, 4])
print "countevens([2, 2, 0]), 3 == ", countevens([2, 2, 0])
print "countevens([1, 3, 5]), 0 == ", countevens([1, 3, 5])


def count9(L):
    result = 0
    for x in L:
        if x==9:
            result = result + 1
    return result

print "count9([1, 2, 9]), 1 == ",count9([1, 2, 9])
print "count9([1, 9, 9]), 2 == ",count9([1, 9, 9])
print "count9([1, 9, 9, 3, 9]), 3 == ",count9([1, 9, 9, 3, 9])


def printrect(width,height,symbol):
    for x in range(height):
        print symbol*width

printrect(4,6,'%')

def printTriangle(width,symbol,rightsideup):
    result = 0
    if rightsideup == 1:
        for x in range(width):
            result = result + 1
            print symbol*result
    else:
        for x in range(width):
            result = width - x
            print symbol*result

printTriangle(10,'%',False)

def printBumps(num,symbol1,symbol2):
    for x in range(num+1):
        printTriangle(x,symbol1,True)
        printTriangle(x,symbol2,False)
printBumps(6,'@','%')

def printChevron(width,symbol):
    result = 0
    spaces = width/2
    for x in range(width):
        spaces = spaces+1
        result = result+1
        print spaces*' '+result*symbol
    for x in range(width):
        spaces = spaces-1
        result = width-x
        print spaces*' '+symbol*result

printChevron(50,'&')


def printDiamond(width,symbol):
    result = 0
    spaces = width/2
    for x in range(width):
        spaces = spaces-1
        result = 1+result
        print spaces*' '+result*symbol
    for x in range(width):
        spaces = spaces+1
        result = -x+width
        print spaces*' '+symbol*result

printDiamond(5,'&')
