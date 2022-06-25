def swap(str1, str2):
    a = str1[:1]
    b = str2[:1]
    
    str1 = b + str1[1:]
    str2 = a + str2[1:]
    return [[str1], [str2]]

def distinctNames(ideas):
    test = []
    test_dict = {}

    for i in ideas:
        test_dict[i] = i

    for i in range(len(ideas)):
        for j in range(len(ideas)):
            if ideas[i] != ideas[j]:
                test.append([ideas[i], ideas[j]])
    print(test)
    
    count = 0
    for i in test:
        tmp = swap(i[0], i[1])
        # print(tmp[0][0], '&' ,tmp[1][0])
        if tmp[0][0] not in test_dict or tmp[1][0] not in test_dict:
            print(tmp[0][0], '&' ,tmp[1][0])
            count += 1
    return count

ideas = ["coffee","donuts","time","toffee"]
print(distinctNames(ideas))

# print(swap('abc', 'def'))
