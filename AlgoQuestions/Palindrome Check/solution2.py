def isPalindrome(string, i = 0):
    # Write your code here.
	l = len(string) - 1 - i
	return True if i >= l else string[i] == string[l] and isPalindrome(string, i+1)
