def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    dp = [[0 for _ in range(width + 1)] for _ in range(height + 1)]
	
	for widthIdx in range(1, width + 1):
		for heightIdx in range(1, height + 1):
			if widthIdx == 1 or heightIdx == 1:
				dp[heightIdx][widthIdx] = 1
			else:
				left = dp[heightIdx][widthIdx - 1]
				right = dp[heightIdx - 1][widthIdx]
				dp[heightIdx][widthIdx] = left + right
	return dp[height][width]
