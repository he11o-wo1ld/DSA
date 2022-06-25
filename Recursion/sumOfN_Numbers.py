def SumOfNNumbers(n):
	if n == 1:
		print(n)
		return
	SumOfNNumbers(n-1)
	print(n)


SumOfNNumbers(7)