def quickSort(toSort):

    if len(toSort) % 2 == 0:
        pivotPoint = (len(toSort) // 2) - 1
    else: 
        pivotPoint = (len(toSort) // 2)
    pivot = toSort[pivotPoint]
    print('pivot: ' + str(pivot))
    endIndex = len(toSort) - 1
    toSort[pivotPoint], toSort[endIndex] = toSort[endIndex], toSort[pivotPoint]

    leftBound = 0
    rightBound = endIndex - 1

    while rightBound >= leftBound:

        while toSort[leftBound] < pivot:
            leftBound += 1

        while toSort[rightBound] >= pivot and rightBound >= leftBound:
            rightBound -= 1

        if rightBound >= leftBound:
            toSort[leftBound], toSort[rightBound] = toSort[rightBound], toSort[leftBound]

        print('After Swap: ' + ' | '.join([str(i) for i in toSort]))

    toSort[endIndex], toSort[leftBound] = toSort[leftBound], toSort[endIndex]
    print('Pivot in final pos: ' + ' | '.join([str(i) for i in toSort]))
    print('\n')

    leftList = toSort[:leftBound]
    rightList = toSort[leftBound + 1:]
    
    if leftBound > 0:
        print('Left half: ' + ' | '.join([str(i) for i in leftList]))
        quickSort(leftList)
        toSort[:leftBound] = leftList
        print(str(leftList))
    if len(toSort[leftBound + 1:]) > 1:
        print('Right half: ' + ' | '.join([str(i) for i in rightList]))
        quickSort(rightList)
        toSort[leftBound + 1:] = rightList
        print('right' + str(rightList))

    print('After completely Sorting: ' + ' | '.join([str(i) for i in toSort]))

quickSort([53, 115, 111, 9, 17, 31, 143, 175, 113, 196, 115, 104, 132, 156, 144, 159, 85, 116, 181, 119])
