import os
import sys
import csv
import time
import random
import math as maths

try:
    shell = sys.stdout.shell
    colour = True
except AttributeError:
    print("You must run this program in IDLE for colours. Program will run in colourless mode.")
    colour = False

def bubbleSort(toSort):
    global lines
    maxIndex = len(toSort) - 1
    swapMade = False
    isSorted = False
    lines += 3
    while not isSorted:
        currentIndex = -1
        lines += 2
        for i in toSort[:maxIndex - 1]:        
            currentIndex += 1
            nextIndex = currentIndex + 1
            lines += 3
            if toSort.index(i) == maxIndex:
                lines += 2
                break
            if i > toSort[nextIndex]:
                toSort[currentIndex], toSort[nextIndex] = toSort[nextIndex], toSort[currentIndex]
                swapMade = True
                lines += 4
        if not swapMade:
            isSorted = True
            lines += 1
        swapMade = False
        maxIndex -= 1
        lines += 3

def insertionSort(toSort):
    global lines
    isSorted = False
    sortedList = [toSort[0]]
    lines += 2
    while not isSorted:
        lines += 1
        for i in toSort[1:]:
            sortedListLength = len(sortedList) - 1
            lines += 2
            for item in sortedList:
                if item < i:
                    if sortedList.index(item) == sortedListLength:
                        sortedList.append(i)
                        lines += 5
                        break
                    else:
                        lines += 5
                        pass
                elif item > i or item == i:
                    sortedList.insert(sortedList.index(item), i)
                    lines += 4
                    break
        isSorted = True
        lines += 1
        
def mergeSort(toSort):
    global lines
    if len(toSort) > 1:
        mid = len(toSort) // 2
        leftList = toSort[:mid]
        rightList = toSort[mid:]
        lines += 4
        mergeSort(leftList)
        mergeSort(rightList)
        leftIndex = 0
        rightIndex = 0
        sortIndex = 0
        lines += 5
        while leftIndex < len(leftList) and rightIndex < len(rightList):
                if leftList[leftIndex] >= rightList[rightIndex]:
                    toSort[sortIndex] = rightList[rightIndex]
                    rightIndex += 1
                    lines += 4
                else:
                    toSort[sortIndex] = leftList[leftIndex]
                    leftIndex += 1
                    lines += 5
                sortIndex += 1
                lines += 1

        while leftIndex < len(leftList):
            toSort[sortIndex] = leftList[leftIndex]
            leftIndex += 1
            sortIndex += 1
            lines += 4

        while rightIndex < len(rightList):
            toSort[sortIndex] = rightList[rightIndex]
            rightIndex += 1
            sortIndex += 1
            lines += 4

def quickSort(toSort):
    global lines
    if len(toSort) % 2 == 0:
        pivotPoint = (len(toSort) // 2) - 1
        lines += 2
    else: 
        pivotPoint = (len(toSort) // 2)
        lines += 3
    pivot = toSort[pivotPoint]
    endIndex = len(toSort) - 1
    toSort[pivotPoint], toSort[endIndex] = toSort[endIndex], toSort[pivotPoint]
    leftBound = 0
    rightBound = endIndex - 1
    lines += 5
    while rightBound >= leftBound:
        lines += 1
        while toSort[leftBound] < pivot:
            leftBound += 1
            lines += 2
        while toSort[rightBound] >= pivot and rightBound >= leftBound:
            rightBound -= 1
            lines += 2
        if rightBound >= leftBound:
            toSort[leftBound], toSort[rightBound] = toSort[rightBound], toSort[leftBound]
            lines += 2
    toSort[endIndex], toSort[leftBound] = toSort[leftBound], toSort[endIndex]
    leftList = toSort[:leftBound]
    rightList = toSort[leftBound + 1:]
    lines += 3
    if leftBound > 0:
        quickSort(leftList)
        toSort[:leftBound] = leftList
        lines += 3
    if len(toSort[leftBound + 1:]) > 1:
        quickSort(rightList)
        toSort[leftBound + 1:] = rightList
        lines += 3
    lines += 1

def radixSort(toSort, passNum):
    global lines
    if passNum <= 4:
        countList = [0,0,0,0,0,0,0,0,0,0]
        sortedList = ['' for i in toSort]
        lines += 2
        for i in toSort:
            try:
                currentDigit = int(str(i)[-passNum])
                lines += 3
            except IndexError:
                currentDigit = 0
                lines += 4
            countList[currentDigit] += 1
            lines += 1
        countList[0] -= 1
        lines += 1
        for index in range(1,10):
            countList[index] += countList[index - 1]
            lines += 2
        toSort.reverse()
        lines += 1
        for i in toSort:
            try:
                currentDigit = int(str(i)[-passNum])
                lines += 3
            except IndexError:
                currentDigit = 0
                lines += 4
            index = countList[currentDigit]
            countList[currentDigit] -= 1
            sortedList[index] = i
            lines += 3
        passNum += 1
        lines += 2
        radixSort(sortedList, passNum)
    lines += 1

def combSort(toSort):
    global lines
    gap = len(toSort)
    Sorted = False
    lines += 2
    while not Sorted:
        try:
            lines += 2
            for i in range(0, len(toSort)):
                if toSort[i] > toSort[i + gap]:
                    toSort[i], toSort[i + gap] = toSort[i + gap], toSort[i]
                    lines += 1
                    if gap == 1:
                        Sorted = True
                        lines += 1
                    lines += 1
                lines += 2
        except IndexError:
            gap = int(gap // 1.3)
            lines += 2
            if gap < 1:
                gap = 1
                lines += 1
            lines += 1

##def pigeonholeSort(toSort):
##    minimum = min(toSort)
##    maximum = max(toSort)
##    rangeOfItems = maximum - minimum + 1
##    pigeonholes = [[] for i in range(0,rangeOfItems)]
##    for i in range(0, len(toSort) - 1):
##        pigeonholes[toSort[i] - minimum].append(toSort[i])
##    sortedList = []
##    for i in pigeonholes:
##        for e in i:
##            sortedList.append(e)

def listGenerator(length):
    numList = []

    for i in range(0,length):
        number = random.randint(0, 15000)
        numList.append(number)
    
    return numList

for listLength in range(1,11):
    testList = listGenerator(listLength * 1000)
    
    sortList = [bubbleSort, insertionSort, mergeSort, quickSort, radixSort, combSort]
    sortNameList = ['Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Radix Sort', 'Comb Sort', 'Pigeonhole Sort']
    resultsList = []

    if colour:
        shell.write("Sorting list of length " + str(listLength) + " thousand...\n","stderr")
    elif not colour:
        print("Sorting list of length " + str(listLength) + " thousand...")

    for i in sortList:
        lines = 0
        testSet = testList.copy()
        whichIndex = sortList.index(i)
        sortUsed = False
        if i == radixSort:
            sortUsed = True
            start = time.time()
            i(testSet, 1)
            end = time.time()
            elapsed = end - start
        elif i == bubbleSort and listLength > 3:
            resultsList.append(['Lots of seconds', 'So many lines'])
            pass
        else:
            sortUsed = True
            start = time.time()
            i(testSet)
            end = time.time()
            elapsed = end - start
        if sortUsed:
            if colour:
                shell.write(sortNameList[whichIndex] + " sorted the list in " + str(elapsed) + " seconds, and executed " + str(lines) + " lines of code!\n","STRING")
            elif not colour:
                print(sortNameList[whichIndex] + " sorted the list in " + str(elapsed) + " seconds, and executed " + str(lines) + " lines of code!")

            resultsList.append([str(elapsed), str(lines)])

    with open("Results.csv", 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(resultsList)
        csv_file.close()
        print('Results written to Results.csv!') 
