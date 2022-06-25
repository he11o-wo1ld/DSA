def nonConstructibleChange(coins):
    # Write your code here.
	coins.sort()
	cur_sum = 0
	for i in range(len(coins)):
		if cur_sum + 1 >= coins[i]:
			cur_sum += coins[i]
		else:
			return cur_sum + 1
	
	return cur_sum + 1
