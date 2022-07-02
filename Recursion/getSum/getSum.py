def getSum(arr):
	l = len(arr)
	if l == 0:
		return 0

	if l == 1:
		return arr[1]
	i = 0
	
	total = arr[0] + getSum(arr[i+1:l])


arr = [1,2, 3, 4, 5, 6]
print(getSum(arr))
