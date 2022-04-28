import random

def isSorted(checkList):
    for i in checkList[1:]:
        if checkList[checkList.index(i) - 1] > i:
            return False
    return True

def awfulSort(toSort):
    while not isSorted(toSort):
        random.shuffle(toSort)
        print(str(toSort) + '\n')

awfulSort([0,4,2,5,1,45,23,87,45,23])

