#https://trinket.io/python/21a9eac422

def Fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return Fib(x-1)+Fib(x-2)

#print Fib(20)


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

#print fibIter(20)




def listReverseNotIter(L):
    if len(L) == 0:
        return 'a list of values, please'
    elif len(L) == 1:
        return L
    elif len(L) >1:
        return L[::-1]

print listReverseNotIter([1,2,3,4,5])
print listReverseNotIter([])
print listReverseNotIter([1,4,7,9])
print listReverseNotIter([1])

def listReverseIter(L):
    K = []
    for i in range(len(L)-1,-1,-1):
        K.append(L[i])
    return K

print listReverseIter([1,2,3,4,5])
print listReverseIter([])
print listReverseIter([1,4,7,9])
print listReverseIter([1])

def listReverse(L):
    if len(L) == 0:
        return '[]'
    elif len(L) == 1:
        return L
    else:
        return [L[-1]]+listReverse(L[0:-1])

print listReverse([1,2,3,4,5])
print listReverse([])
print listReverse([1,4,7,9])
print listReverse([1])

