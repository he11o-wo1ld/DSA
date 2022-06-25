def threeNumberSum(nums, targetSum):
    # Write your code here.
    res = []
	nums.sort()
	for i in range(len(nums)):
		if nums[i] > 0:
			break
		if i == 0 or nums[i-1] != nums[i]:
			twoSum(nums, i, res)
	return res

def twoSum(nums, i, res):
	l = i + 1
	r = len(nums) - 1
	while l < r:
		Sum = nums[i] + nums[l] + nums[r]
		if Sum < 0:
			l += 1
		elif Sum > 0:
			r -= 1
		else:
			res.append([nums[i], nums[l], nums[r]])
			l += 1
			r -= 1
			while l < r and nums[l] == nums[l - 1]:
				l += 1
