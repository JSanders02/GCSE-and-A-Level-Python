import random

def listGen(length):
    numList = []

    for i in range(0, int(length)):
        number = random.randint(0, int(length) * 10)
        numList.append(number)
    return numList

def partition(arr, p, r):
    piv = arr[r]
    mid = p - 1

    for i in range(p, r):
        if arr[i] <= piv:
            mid += 1
            arr[mid], arr[i] = arr[i], arr[mid]

    arr[mid + 1], arr[r] = arr[r], arr[mid + 1]

    return mid + 1

def quickSort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quickSort(arr, p, q - 1)
        quickSort(arr, q + 1, r)

def randomPartition(arr, p, r):
    i = random.randint(p, r)
    arr[r], arr[i] = arr[i], arr[r]
    return partition(arr, p, r)

def randomQuickSort(arr, p, r):
    if p < r:
        q = randomPartition(arr, p, r)
        quickSort(arr, p, q - 1)
        quickSort(arr, q + 1, r)

toSort = listGen(10)
print(toSort)
randomQuickSort(toSort, 0, len(toSort) - 1)
print(toSort)