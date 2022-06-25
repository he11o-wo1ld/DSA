def rightmostNonZeroDigit(N, arr):
	product = 1
	for i in arr:
		product *= i
	if product == 0:
		return -1
	elif product == 1:
		return -1

	str_num = str(product)
	num = str_num[::-1]

	nums = [i for i in num]

	for i in range(len(nums)):
		if nums[i] == "0":
			if nums[i+1] != "0":
				return nums[i+1]
			else:
				continue
		else:
			continue
	return -1



arr = [1,4,1,3]
N = 4


print(rightmostNonZeroDigit(N, arr))


("Messaged", "Messaged"),
("Called", "Called"),
("Emailed", "Emailed"),
("With Lock In Period")