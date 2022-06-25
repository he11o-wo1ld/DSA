def getPermutations(array):
	permutations = []
	permutationsHelper(0, array, permutations)
	return permutations
	
def permutationsHelper(i, array, permutations):
	if i == len(array) - 1:
		permutations.append(array[:])
	else:
		for j in range(i, len(array)):
			# swap(array, i, j)
			array[i], array[j] = array[j], array[i]
			permutationsHelper(i + 1, array, permutations)
			array[i], array[j] = array[j], array[i]
			# swap(array, i, j)
	return permutations
	
def swap(array, i, j):
	array[i], array[j] = array[j], array[i]
	return array
	
array = [1, 2, 3]
print(getPermutations(array))
