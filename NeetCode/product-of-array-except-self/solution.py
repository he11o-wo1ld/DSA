def productExceptSelf(nums):
	res = [0 for i in range(len(nums))]
	prefixIndex = -1
	prefixValue = 1
	postfixIndex = len(nums)
	postfixValue = 1

	for i in range(len(nums)):
		if i == 0:
			res[i] = prefixValue
		else:
			res[i] = nums[i-1] * prefixValue
		prefixValue = res[i]


	for i in range(len(nums)-1, -1, -1):
		if i == len(nums)-1:
			res[i] *= postfixValue
		else:
			res[i] = res[i] * postfixValue
		postfixValue *= nums[i]
	return res

nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
