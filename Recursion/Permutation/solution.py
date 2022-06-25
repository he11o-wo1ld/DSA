def permutation(array):
	i = 0

	def swap(arr, i, j):


	def solve(arr, i):
		if i == len(arr) - 1:
			print(arr)
			return

		for j in range(i, len(arr)):
			arr[j], arr[i] = arr[i], arr[j]
			solve(arr, i+1)
			arr[i], arr[j] = arr[j], arr[i]

	
	solve(array, i)
	return array;

arr = 'ABCD'
print(permutation(arr))