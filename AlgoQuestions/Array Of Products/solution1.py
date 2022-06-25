def arrayOfProducts(array):
	resultArray = []
    for i in range(len(array)):
        leftSum = getProduct(array[:i])
        rightSum = getProduct(array[i+1:])
        totalSum = leftSum * rightSum
        resultArray.append(totalSum)
    return resultArray


def getProduct(array):
    total = 1
    for i in array:
        total *= i
    return total
