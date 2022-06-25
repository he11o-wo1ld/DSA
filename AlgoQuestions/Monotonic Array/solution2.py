def isMonotonic(array):
    # Write your code here.
    if len(array) <= 2:
		return True
	
	direction = array[1] - array[0]
	for i in range(2, len(array)):
		if direction == 0:
			direction = array[i] - array[i - 1]
			continue
		if breakDirections(direction, array[i-1], array[i]):
			return False
	return True


def breakDirections(direction, previousNumber, currentNumber):
	difference = currentNumber - previousNumber
	if direction > 0:
		return difference < 0
	return difference > 0
