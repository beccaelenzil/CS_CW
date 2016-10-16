def FibSequenceRec(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return FibSequenceRec(x-1)+FibSequenceRec(x-2)

print FibSequenceRec(20)


def FibSequenceIt(x):
    for n in x:
        if x == 0:
            n = 0
            return n
        elif x == 1:
            n = 1
            return n
        else:
            n = (n-1)+(n-1)
            return n

print FibSequenceIt(5)

