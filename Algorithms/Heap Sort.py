import math

def maxHeapify(heap, heapSize, i=0):
    l = (i + 1) * 2 - 1
    r = ((i + 1) * 2)

    # Find largest child of i
    largest = i
    if l < heapSize and heap[l] >= heap[i]:
        largest = l

    if r < heapSize and heap[r] >= heap[largest]:
        largest = r

    # If i has a child that is larger, swap it with the larger child, and recurse on i's new index
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        maxHeapify(heap, heapSize, largest)


def buildMaxHeap(heap):
    for i in range(math.floor(len(heap) / 2), 0, -1):
        maxHeapify(heap, len(heap), i - 1)

def heapSort(heap):
    # Convert to max heap
    buildMaxHeap(heap)

    heapSize = len(heap)
    for i in range(len(heap) - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0] # Swap first element (largest element) with last
        heapSize -= 1 # Reduce heap size, as largest element is now out of the heap
        maxHeapify(heap, heapSize) # Call maxHeapify again to retain the max heap property

heap = [16, 4, 10, 23, 1, 23, 4, 53, 2, 14]

heapSort(heap)

print(heap)