def productSum(array, multiplier=1):
	Sum = 0

	for i in array:
		if type(i) is list:
			Sum += productSum(i, multiplier+1)
		else:
			Sum += i
	return Sum * multiplier



array =  [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(array))