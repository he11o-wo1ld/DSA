def kadanesAlgorithm(array):
    # Write your code here.
    curr_sum = array[0]
	max_sum = array[0]
	
	for i in range(1, len(array)):
		curr_sum = max(curr_sum + array[i], array[i])
		max_sum = max(max_sum, curr_sum)
	return max_sum
