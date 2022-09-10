# def uniquePath(m, n):
# 	row = [1] * n
# 	for i in range(m - 1):
# 		newRow = [1] * n
# 		for j in range(n - 2, -1, -1):
# 			newRow[j] = newRow[j + 1] + row[j]
# 		row = newRow
# 	return row[0]

# m = 3
# n = 7
# print(uniquePath(m,n))


# def f():
# 	i = 0
# 	Sum = 0
# 	while i< 100:
# 		Sum += i
# 		Sum += i
# 		i+=1
# 	print(Sum)

arr = [1, 2, 3, 4, 5, 6, 7, 8]
for i, j in  enumerate(arr):
	print(i, j)
