def minRewards(scores):
    res_arr = [1 for i in range(len(scores))]

    for i in range(1, len(scores)):
        # print(scores[i-1], scores[i]) 
        if scores[i - 1] < scores[i]:
            res_arr[i] = max(res_arr[i], res_arr[i-1] + 1)

    for i in range(len(scores) - 2, -1, -1):
        # print(scores[i + 1], scores[i])
        if scores[i + 1] < scores[i]:
            res_arr[i] = max(res_arr[i], res_arr[i+1] + 1)

    total = 0
    for i in range(len(res_arr)): total = total + res_arr[i] 
    return total


scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
print(minRewards(scores))