def largestRange(array):
	remaining = set(array)
	largest = [array[0], array[0]]

	for num in array:
		if num not in remaining:
			continue

		lo = num
		hi = num

		while hi + 1 in remaining:
			remaining.discard(hi + 1)
			hi += 1

		while lo - 1 in remaining:
			remaining.discard(lo - 1)
			lo -= 1

		largest = max(largest, (lo, hi), key=lambda x: x[1] - x[0])

	return largest


array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(largestRange(array))
