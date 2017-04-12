
def mergeSort(alist):
    print "Splitting ",alist
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print "Merging ",alist

#alist = [54,26,93,17,77,31,44,55,20]
#mergeSort(alist)
#print(alist)

def quickSort(aList):
    i = 0
    j = 0
    mid = len(aList)/2
    base = aList[0]

    for i in range(0, len(aList)):
        if aList[i] >= base:
            for j in reversed(aList):
                if aList[len(aList)-j] >= base:
                    aList[i] = aList[len(aList)-j]
                    aList[len(aList)-j] = aList[1]
    
    return aList

print quickSort([5,4,6])


