def FibSequenceRec(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return FibSequenceRec(x-1)+FibSequenceRec(x-2)

print FibSequenceRec(20)


def fibIter(x):
    fibSeq = [0,1]
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        for n in range(2,x):
            fibSeq.append(fibSeq[n-1]+fibSeq[n-2])
            print fibSeq
        return fibSeq[-1]

print fibIter(50)


