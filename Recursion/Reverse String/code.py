def reverseStr(string):
	return getReversed(string, 0, len(string)-1)

def getReversed(string, l, r):
	if l > r:
		return

	print(string[l], string[r])
	# tmp = string[l]
	# string[l] = string[r]
	# string[r] = tmp
	
	getReversed(string, l+1, r-1)
	return string

print(reverseStr("Hello World"))