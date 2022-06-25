def binarySearch(array, target):
    # Write your code here.
	return search(array, target, 0, len(array)-1)

def search(array, target, left, right):
	if left > right:
		return -1
	mid = (left + right) // 2
	
	if array[mid] == target:
		return mid
	elif array[mid] > target:
		return search(array, target, left, mid - 1)
		
	elif array[mid] < target:
		return search(array, target, mid + 1, right)