def hasSingleCycle(array):
	visitedIndex = 0
	currentIndex = 0
	
	while visitedIndex < len(array):
		if visitedIndex > 0 and currentIndex == 0:
			return False
		visitedIndex += 1
		currentIndex = getIndex(currentIndex, array)
	return currentIndex == 0

def getIndex(currentIndex, array):
	jump = array[currentIndex]
	nextIndex = (currentIndex + jump) % len(array)
	return nextIndex if nextIndex >= 0 else nextIndex + len(array)
