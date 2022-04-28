def awfulerSort(toSort):
    for i in toSort:
        toSort[toSort.index(i)] = toSort[toSort.index(i) - 1] + 1
        print(toSort)
    print('Done!')

awfulerSort([2,5,2,65,234,76,3,1])
