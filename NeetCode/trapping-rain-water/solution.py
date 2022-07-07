def trap(heights):

	leftMaxArr = [0 for i in heights]
	rightMaxArr = [0 for i in heights]
	subArray = [0 for i in range(len(heights))]

	curr = 0
	
	for i in range(len(heights)-1):
		curr = max(curr, heights[i])
		leftMaxArr[i+1] = curr

	curr = 0
	for i in range(len(heights)-1, 0, -1):
		curr = max(curr, heights[i])
		rightMaxArr[i-1] = curr


	for i in range(len(heights)):
		subArray[i] = min(leftMaxArr[i], rightMaxArr[i])

	total = 0
	for i in range(len(heights)):
		if subArray[i] - heights[i] > 0:
			total += (subArray[i] - heights[i])



	return total



height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))