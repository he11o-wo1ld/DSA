def twoNumberSum(array, targetSum):
    # Write your code here.
	array.sort()
	end = len(array) - 1
	start = 0
	
	while start < end:
		curr_sum = array[start] + array[end]
		if curr_sum == targetSum:
			return [array[start], array[end]]
		elif curr_sum < targetSum:
			start += 1
		elif curr_sum > targetSum:
			end -= 1
	return []