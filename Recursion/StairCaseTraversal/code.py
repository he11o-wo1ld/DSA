def countWays(n):
	if n < 0:
		return 0

	if n == 0 or n == 1:
		return 1

	return countWays(n-1) + countWays(n-2) + countWays(n-3)

n = int(input('>'))
print(countWays(n))