# Lenier
def maxArea(heights):
	l = 0
	r = len(heights)-1

	maxArea = 0	

	while l < r:
		area = (r-l) * min(heights[l], heights[r])
		maxArea = max(maxArea, area)

		if heights[l] > heights[r]:
			r -= 1
		else:
			l += 1
	return maxArea

heights = [1,8,6,2,5,4,8,3,7]
print(maxArea(heights))
