toSort = [[1,4,2],[2,3,3],[5,1,2],[4,2,3]]

#Sort key to be used when calling .sort() on a list
def sortKey(e):
	#e[1] sorts by the index 1, e[0] would sort by index 0, etc.
	return e[1]

#.sort(key={NAME OF SORT KEY FUNCTION}, reverse = True (Highest -> Lowest)/False (Lowest -> Highest))
toSort.sort(key = sortKey, reverse = True)
print(toSort)

#sorted() does the same as .sort() but returns an iterable list
sortedList = sorted(toSort, key = sortKey, reverse = False)
print(sortedList)