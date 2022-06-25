def twoNumberSum(array, targetSum):
    # Write your code here.
    arr = {}
	for i in array:
		if targetSum - i not in arr:
			arr[i] = True
		else:
			return [targetSum - i, i]
	return []