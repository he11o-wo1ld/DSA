def minNumberOfCoinsForChange(amount, coins):
    dpArray = [float('inf') for i in range (amount+1)]
	dpArray[0] = 0
	for i in range(len(dpArray)):
		for j in range(len(coins)):
			coinsValue = coins[j]
			if coinsValue <= i:
				dpArray[i] = min(dpArray[i-coinsValue]+1,dpArray[i])
	ans = dpArray[len(dpArray) - 1]
	if ans == float('inf'):
		return -1
	else:
		return ans
