def isPalindrome(string):
    # Write your code here.
    reverse = ""
	for i in reversed(range(len(string))):
		print(string[i])
		reverse += string[i]
	return string == "".join(reverse)
