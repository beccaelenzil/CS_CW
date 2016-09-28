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
    for x in range(0,m):
        result = result + n
    return result
print mult(10,5)

def dot(L,K):
    """
    :param L: list
    :param K: list
    :return: dot product of L and K: L1*K1 + L2*K2
    """
    result = 1
    for x in L:
        result = result*x
