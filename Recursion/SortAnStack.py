# Sorting an array using recursion.
def sortArray(arr):
	if len(arr) == 1:	# if len of the array is 0 or None return the array
		return arr
		
	tmp = arr[len(arr) - 1]		
	# saving the last element of the array
	
	arr.pop()
	# removing the last element of the array
	
	arr.sort()
	# sorting the array after removing the last element of the array
		
	insert(arr, tmp)
	# Calling the insert helper function, it'll return the sorted array
	`
	return arr
	
	
def insert(arr, tmp):
	# Checking if length of array is 0, then return 0
	# temp is the last element of the main array,
	# if temp is greater or equal to the last element of the current array
	if len(arr) == 0 or arr[len(arr) - 1] <= tmp:
		# append temp in last position of the array
		arr.append(tmp)
		return
	
	# storing the last item in val
	val = arr[len(arr) - 1]
	
	# removing the last element from the current array
	arr.pop()
	
	# recursive call
	# calling insert function with current array after removing last element and tmp
	insert(arr, tmp)
	
	# append val end of the array
	arr.append(val)
	# return arr
	
	
arr = [0,1,5,2]
print(sortArray(arr))