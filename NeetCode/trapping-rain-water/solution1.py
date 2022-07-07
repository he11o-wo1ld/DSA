def trap(heights):
	l, r = 0, len(heights) - 1
	total = 0

	left = heights[l]
	right = heights[r]

	while l < r:
		if l == 0:
			lval = heights[l]
			l+=1

		elif r == len(heights) - 1:
			rval = heights[r]
			r -= 1

		if left < right:
			if lval - left > 0:
				total += lval - left
				lval = 


	return total



height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))