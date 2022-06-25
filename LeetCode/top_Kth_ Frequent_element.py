def topKFrequent(nums, k):
    nums_dict = {}
    for i in nums:
        if i in nums_dict:
            nums_dict[i] += 1
        else:
            nums_dict[i] = 1
    
    count = [[] for i in range(len(nums) + 1)]

    for n, c in nums_dict.items():
        count[c].append(n)

    res= []

    for i in range(len(count)-1, 0, -1):
        for n in count[i]:
            res.append(n)
            if len(res) == k:
                return res

    return nums_dict.items()



nums = [5,5,8,9,8,5,9,7,6,4]
k = 2
print(topKFrequent(nums, k))