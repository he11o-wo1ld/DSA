def zeroSumSubarray(nums):
    # Write your code here.
    res = 0
    sumMap = {0 : 1}
    currSum = 0
    for num in nums:
        currSum += num
        res += sumMap.get(currSum, 0)
        sumMap[currSum] = sumMap.get(currSum, 0) + 1
    return res > 0

nums = [-2, -3, -1, 2, 3, 4, -5, -3, 1, 2]
print(zeroSumSubarray(nums))
