def firstDuplicateValue(array):
    number_count = {}
	for nums in array:
		if nums not in number_count:
			number_count[nums] = 1
		elif nums in number_count:
			return nums
	return -1
