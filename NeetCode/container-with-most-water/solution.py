# Brutforce
def maxArea(heights):
	res = 0
	for l in range(len(heights)):
		for r in range(l+1, len(heights)):
			height = r - l
			width = min(heights[l], heights[r])
			area = height * width
			res = max(area, res)
	return res

heights = [1,8,6,2,5,4,8,3,7]
print(maxArea(heights))
