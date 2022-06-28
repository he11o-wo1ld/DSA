def threeNumberSort(array, order):
	array_dict = {}
	count = 0

	for value in array:
		array_dict[value] = array_dict.get(value, 0) + 1

	for value in order:
		for _ in range(array_dict.get(value,0)):
			array[count] = value
			count += 1

	return array



array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
print(threeNumberSort(array, order))
