def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp
    return nums

def solve(nums, ans, idx):
    if idx >= len(nums):
        ans.append(nums)
        return

    for i in range(idx, len(nums)):
        swap(nums, idx, i)
        solve(nums, ans, idx)
        swap(nums, idx, i)
    return ans

def permute(nums):
    ans = []
    idx = 0
    solve(nums, ans, idx);
    return ans


nums = [1,2,3]
print(permute(nums))