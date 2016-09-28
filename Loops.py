def pow(b,p):

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
print pow(5,2)
print pow(1000,0)
print pow(2,6)


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


