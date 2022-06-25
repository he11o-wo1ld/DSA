def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if not len(array):
		return 0
	if len(array) == 1:
		return array[0]
	
	firstNum = array[0]
	secondNum = max(array[0], array[1])
	
	for i in range(2, len(array)):
		current = max(firstNum + array[i], secondNum)
		firstNum = secondNum
		secondNum = current
	return secondNum
