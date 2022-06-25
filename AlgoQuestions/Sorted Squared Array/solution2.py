def sortedSquaredArray(array):
    # Write your code here.
    start = 0
	end = len(array) - 1
	arr = [0 for _ in array]
	
	
	for i in reversed(range(len(array))):
		startVal = array[start]
		endVal = array[end]
		
		if abs(startVal) > abs(endVal):
			arr[i] = startVal * startVal
			start += 1
		else:
			arr[i] = endVal * endVal
			end -= 1
	return arr