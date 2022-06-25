def minimumAverageDifference(nums):
	# print(nums[1:], len(nums[1:]))
	l = 1
	total = 0
	while l <= len(nums):
		leftSum = getSum(nums[:l])
		rightSum = getSum(nums[l:])
		# print(f"{nums[:l]} / {len(nums[:l])} = {leftSum}, {nums[l:]} / {len(nums[l:])} = {rightSum}")
		average = int(leftSum - rightSum)
		l += 1
		total += abs(average)
		
	return total // len(nums)



def getSum(arr):
	total = 0
	if len(arr) >= 1:
		for i in arr:
			total += i
		total = total // len(arr) 
	return total


nums = [2,5,3,9,5,3]
# print(minimumAverageDifference(nums))
