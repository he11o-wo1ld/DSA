def smallestDifference(arrayOne, arrayTwo):
    a1 = 0
    a2 = 0

    min_diff = float('inf')
    res = []

    arrayOne.sort()
    arrayTwo.sort()

    while a1 < len(arrayOne) and a2 < len(arrayTwo):
        
        #   Getting the absolute value of the subtraction
        #   Compare the absolute subtract value with the minimum difference
        #   if the absolute subtract value less then minimum difference it'll update the minimum difference

        if abs(arrayOne[a1] - arrayTwo[a2]) < min_diff:
            res = [arrayOne[a1], arrayTwo[a2]]
            min_diff = abs(arrayOne[a1] - arrayTwo[a2])

        if arrayOne[a1] > arrayTwo[a2] and a2 < len(arrayTwo):
            a2 += 1

        elif arrayTwo[a2] > arrayOne[a1] and a1 < len(arrayOne):
            a1 += 1
        else:
            return [arrayTwo[a2], arrayOne[a1]]

    return res
 

arrayOne = [10, 0, 20, 25, 20i00]
arrayTwo = [1005, 1006, 1014, 1032, 1031]

print(smallestDifference(arrayOne, arrayTwo))



# {
#   "arrayOne": [-1, 5, 10, 20, 28, 3],
#   "arrayTwo": [26, 134, 135, 15, 17]
# }
# Test Case 2
# {
#   "arrayOne": [-1, 5, 10, 20, 3],
#   "arrayTwo": [26, 134, 135, 15, 17]
# }
# Test Case 3
# {
#   "arrayOne": [10, 0, 20, 25],
#   "arrayTwo": [1005, 1006, 1014, 1032, 1031]
# }
# Test Case 4
# {
#   "arrayOne": [10, 0, 20, 25, 2200],
#   "arrayTwo": [1005, 1006, 1014, 1032, 1031]
# }
# Test Case 5
# {
#   "arrayOne": [10, 0, 20, 25, 2000],
#   "arrayTwo": [1005, 1006, 1014, 1032, 1031]
# }
# Test Case 6
# {
#   "arrayOne": [240, 124, 86, 111, 2, 84, 954, 27, 89],
#   "arrayTwo": [1, 3, 954, 19, 8]
# }
# Test Case 7
# {
#   "arrayOne": [0, 20],
#   "arrayTwo": [21, -2]
# }
# Test Case 8
# {
#   "arrayOne": [10, 1000],
#   "arrayTwo": [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]
# }
# Test Case 9
# {
#   "arrayOne": [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123],
#   "arrayTwo": [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]
# }
# Test Case 10
# {
#   "arrayOne": [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123, 530],
#   "arrayTwo": [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]
# }