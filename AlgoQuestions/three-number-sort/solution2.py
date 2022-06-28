# time : O(n) | space : O(1)
def threeNumberSort(array, order):
	firstValue = order[0]
	thirdValue = order[2]

	firstIdx = 0
	for idx in range(len(array)):
		if array[idx] == firstValue:
			array[firstIdx], array[idx] = array[idx], array[firstIdx]
			firstIdx += 1

	thirdIdx = len(array) - 1
	for i in range(len(array)-1, -1, -1):
		if array[i] == thirdValue:
			array[thirdIdx], array[i] = array[i], array[thirdIdx]
			thirdIdx -= 1

	return array

array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
print(threeNumberSort(array, order))
