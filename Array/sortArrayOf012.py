def sort012(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            zero = arr.pop(i)
            arr.pop(i)
            arr.insert(0, zero)
        
        elif arr[i] == 2:
            tmp = arr.pop(i)
            arr.pop(i)
            arr.append(tmp)
    return arr
            
arr = [0,2,1,2,0]
print(sort012(arr))