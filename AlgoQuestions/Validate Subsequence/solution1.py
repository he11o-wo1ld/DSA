def isValidSubsequence(array, sequence):
    # Write your code here.
    arr = {}
	for i in array:
		if i in arr:
			arr[i] += 1
		else:
			arr[i] = 1
	
	for i in sequence:
		if i in arr:
			arr[i] -= 1
			if arr[i] == 0:
				arr.pop(arr[i])
		else:
			return False
	return True