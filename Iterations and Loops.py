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


