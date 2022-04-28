import random
def combSort(toSort):
    gap = len(toSort)
    Sorted = False
    print(' | '.join([str(i) for i in toSort]))
    while not Sorted:
        try:
            for i in range(0, len(toSort)):
                print(' | '.join([str(i) for i in toSort]))
                if toSort[i] > toSort[i + gap]:
                    toSort[i], toSort[i + gap] = toSort[i + gap], toSort[i]
                    if gap == 1:
                        Sorted = True
        except IndexError:
            gap = int(gap // 1.3)
            if gap < 1:
                gap = 1
    print('\nSorted!\n')

toSort = []
for i in range(0,20):
    number = random.randint(0,20)
    toSort.append(number)
    
combSort([8, 4, 1, 56, 3, -44, 23, -6, 28, 0])
