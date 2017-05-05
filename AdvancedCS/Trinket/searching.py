
# Number of Operations - sequentialSearch
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
#print sequentialSearch(sequentialSearchList, 6)




# Number of Operations - binarySearch
# --------------------
# Best Case: 1
# Worst Case: len(aList)/2
# Average Case: len(aList)/4

def binarySearch(aList, item): #assuming aList is already sorted
    mid = len(aList)//2
    done = False

    if aList[mid] == item:
        done = True
    elif aList[mid] > item:
        newList = aList[:mid]
    elif aList[mid] < item:
        newList = aList[mid:]



    if done != True:
        if len(aList) > 1:
            print newList
            done = binarySearch(newList, item)
        elif len(aList) == 1:
            if aList[0] != item:
                done = False
        else:
            done = False

    print done
    return done

binarySearchList = (1,3,5,8,9,13,15,17,20,25,32,40)
print binarySearch(binarySearchList,15)














