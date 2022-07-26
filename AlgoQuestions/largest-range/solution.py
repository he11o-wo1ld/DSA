def largestRange(array):
    s = min(array)
    l = max(array)
    arr_dict = {}
    for i in range(len(array)):
        arr_dict[array[i]] = True
    for i in range(s, l+1):
        
    return arr_dict






array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(largestRange(array))
