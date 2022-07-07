def twoSum(numbers, target):
    for i in range(len(numbers)-1, 0, -1):
        if numbers[i] > target:
            numbers.pop(i)
    l = 0
    r = len(numbers) - 1

    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l+1, r+1]
        if numbers[l] + numbers[r] > target:
            r -= 1
        if numbers[l] + numbers[r] < target:
            l += 1
    return

numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))
