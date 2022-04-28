def radixSort(toSort, passNum):
    if passNum <= 4:
        countList = [0,0,0,0,0,0,0,0,0,0]
        sortedList = ['' for i in toSort]

        for i in toSort:
            try:
                currentDigit = int(str(i)[-passNum])
            except IndexError:
                currentDigit = 0
            countList[currentDigit] += 1

        countList[0] -= 1

        for index in range(1,10):
            countList[index] += countList[index - 1]

        toSort.reverse()
        for i in toSort:
            try:
                currentDigit = int(str(i)[-passNum])
            except IndexError:
                currentDigit = 0
            index = countList[currentDigit]
            countList[currentDigit] -= 1
            sortedList[index] = i

        passNum += 1
        print(sortedList)
        radixSort(sortedList, passNum)

toSort = [1,29,39,19,1235,234,45,76,34,231,23,54]
radixSort(toSort, 1)
