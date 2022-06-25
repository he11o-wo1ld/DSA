def fourNumberSum(array, target):
	allPair = {}
	squad = []

	for i in range(1, len(array) - 1):
		for j in range(i + 1, len(array)):
			currSum = array[i] + array[j]
			difference = target - currSum

			if difference in allPair:

				for pair in allPair[difference]:
					squad.append(pair + [array[i], array[j]])

		for k in range(0, i):
			currSum = array[i] + array[k]

			if currSum not in allPair:
				allPair[currSum] = [[array[k], array[i]]]
			else:
				allPair[currSum].append([array[k], array[i]])
	return squad


array = [2,2,2,2,2]
targetSum = 8

print(fourNumberSum(array, targetSum))
