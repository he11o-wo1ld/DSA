def merge(intervals):
	intervals.sort(key=lambda i : i[0])

	res = [intervals[0]]

	for start, end in intervals[1:]:
		lastEnd = res[-1][1]

		if start <= lastEnd:
			res[-1][1] = max(lastEnd, end)
		else:
			res.append([start, end])
	return res
	
	# if len(nums) == 1:
	# 	return nums

	# res = []
	# nums.sort()

	# for i in range(1, len(nums)):
	# 	if nums[i][0] <= nums[i-1][1]:
	# 		if nums[i][1] <= nums[i-1][1]:
	# 			res.append([nums[i-1][0], nums[i-1][1]])
	# 		elif nums[i][0] >= nums[i-1][0]:
	# 			res.append([nums[i][0], nums[i][1]])
	# 		else:
	# 			res.append([nums[i-1][0], nums[i][1]])
	# 	else:
	# 		if i == 1:
	# 			res.append(nums[i-1])
	# 		res.append(nums[i])
	# return res



intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[5,6], [7,8]]
# intervals = [[1,4],[2,3]]
# intervals = [[0,4],[1,5]]
# intervals = [[1,4],[3,5]]

print(merge(intervals))