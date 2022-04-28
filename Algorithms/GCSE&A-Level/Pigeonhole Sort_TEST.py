def pigeonholeSort(toSort):
    minimum = min(toSort)
    maximum = max(toSort)
    rangeOfItems = maximum - minimum + 1
    pigeonholes = [[] for i in range(0,rangeOfItems)]
    for i in range(0, len(toSort) - 1):
        pigeonholes[toSort[i] - minimum].append(toSort[i])
    sortedList = []
    for i in pigeonholes:
        for e in i:
            sortedList.append(e)
    print('Sorted!\n')
    print(sortedList)

pigeonholeSort([802, 630, 20, 745, 52, 300, 612, 932, 78, 187])
