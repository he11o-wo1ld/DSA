def numberOfWaysToTraverseGraph(width, height):
	xAxis = width - 1
	yAxis = height - 1
	
	numerator = factorial(xAxis + yAxis)
	denominator = factorial(xAxis) * factorial(yAxis)
	
	return numerator // denominator

def factorial(num):
	result = 1
	for i in range(2, num + 1):
		result *= i
	return result
