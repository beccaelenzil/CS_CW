#File: Sorting.py
#Versions: Python 2.7.13
#Name: Colin Wood
#Date: 4/14/17
#Desc: PROG DESC
#Usage:

import random
#import matplotlib.pyplot as plt

def display(some_list):
    plt.clf()
    plt.bar(range(len(some_list)),some_list)
    plt.pause(0.01)
    plt.show()


def makeList(listLength, listRange):
    numList = []
    for i in range(listLength):
        numList.append((random.randint(0, listRange)))
    return numList

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

def quickSort(aList, start, stop):
    if stop - start < 1:
    #why can't it be if len(aList) < 1?
        return aList
    else:
        base = aList[start]
        left = start
        right = stop
        while left <= right:
            while aList[left] < base:
                left += 1
            while aList[right] > base:
                right -= 1
            if left < right:
                aList[left], aList[right] = aList[right], aList[left]
                left += 1
                right -= 1

        print aList
        quickSort(aList, start, right)
        quickSort(aList, left, stop)


my_list = [39, 30, 45, 33, 20, 61, 36, 5, 31, 64]
quickSort(my_list, 0, len(my_list) - 1)







