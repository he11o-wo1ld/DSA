def mejorityElement(nums):
	res = 0
	count = 0

	for i in nums:
		if count == 0:
			res = i
		count += (1 if i == res else -1)
	return res

nums = [2,2,3,2,3,2,3,3,2]
print(mejorityElement(nums))