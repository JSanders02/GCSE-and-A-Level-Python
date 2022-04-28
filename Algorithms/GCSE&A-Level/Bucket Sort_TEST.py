import math as maths
import random

def bucketSort(toSort):
    bucketList = [[],[],[],[],[],[],[],[],[],[]]
    for unsorted in toSort:
        bucketIndex = maths.trunc(10 * unsorted)
        bucket = bucketList[bucketIndex]
        if bucket == []:
            bucket.append(unsorted)
        else:
            insertIndex = -1
            for sortedItem in bucket:
                insertIndex += 1
                if sortedItem > unsorted:
                    bucket.insert(insertIndex, unsorted)
                    break
                elif insertIndex == len(bucket) - 1:
                    bucket.append(unsorted)
                    break
        bucketList[bucketIndex] = bucket
    sortedList = []
    for i in bucketList:
        for e in i:
            sortedList.append(e)

    print('Sorted!\n')
    print(sortedList)

toSort = []
for i in range(0,20):
    toSort.append(round(random.random(), 3))
                  
bucketSort(toSort)
