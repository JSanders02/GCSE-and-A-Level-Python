def numberCoolness(number):
    number = str(number)
    coolness = 0
    if number == '69':
        return 9999999999999999999999999999999999999999999
    if number == '420':
        return 9999999999999999999999999999999999999999997
    for i in number:
        if i == '9':
            if number[number.index(i) - 1] == '6':
                return 9999999999999999999999999999999999999999998
        if i == '0':
            coolness += 4
        elif i == '1':
            coolness += 5
        elif i == '2':
            coolness += 8
        elif i == '3':
            coolness += 7
        elif i == '4':
            coolness += 2
        elif i == '5':
            coolness += 3
        elif i == '6':
            coolness += 1
        elif i == '7':
            coolness += 10
        elif i == '8':
            coolness += 7
        elif i == '9':
            coolness += 9

    print(number, coolness)
    return coolness

def coolnessSort(toSort):
    sortedList = [toSort[0]]
    toSort = toSort[1:]
    while len(toSort) > 0:
        sortNumber = toSort.pop()
        for comparisonNumber in sortedList:
            if numberCoolness(sortNumber) < numberCoolness(comparisonNumber):
                sortedList.insert(sortNumber, sortedList.index(comparisonNumber))
                break
            elif comparisonNumber == sortedList[-1]:
                sortedList.append(sortNumber)
                break

    return sortedList

print(coolnessSort([1,4,123,65,69,420,11169,54,34,65,333,99]))
