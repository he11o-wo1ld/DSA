def sortedSquaredArray(array):
    # Write your code here.
	arr = [0 for _ in array]
    for i in range(len(array)):
		num = array[i]
		arr[i] = num * num
	arr.sort()
	return arr
