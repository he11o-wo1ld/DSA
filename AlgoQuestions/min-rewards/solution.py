def minRewards(scores):
    min_arr = []
    output = []
    for i in range(len(scores)):
        if i >= 1 and i < len(scores) - 1: 
            if scores[i] < scores[i+1] and scores[i] < scores[i-1]:
                min_arr.append(i)
        if i == 0 and scores[i] < scores[i+1]:
            min_arr.append(i)
        if i == len(scores) - 1 and scores[i] < scores[i-1]:
            min_arr.append(i)

    for i in min_arr:
        a = 0
        b = i
        for j in range(a, b+1):
            output.append(b+1 - j)
        break
        a = b
        b = i


    return output


scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
print(minRewards(scores))