
# Number of Operations
# --------------------
# Best Case: 1
# Worst Case: len(aList)
# Average Case: len(aList)/2

def sequentialSearch(aList, item):
    done = False
    while done == False:
        for i in range(len(aList)):
            if aList[i] == item:
                done = True
                return done
            elif i == len(aList)-1:
                return done


sequentialSearchList = [5,5,3,1,7,4,3,1,0,9,6]
#print sequentialSearchList
print sequentialSearch(sequentialSearchList, 6)


def binarySearch(aList, item):
    




