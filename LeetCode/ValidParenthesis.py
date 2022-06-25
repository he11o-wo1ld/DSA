def isValid(s):
	stack = []
	Parentheses = {")": "(", "}": "{", "]": "["}

	for c in s:
		if c in Parentheses:
			if stack and stack[-1] == Parentheses[c]:
				stack.pop()
			else:
				return False
		else:
			stack.append(c)
	return True if not stack else False


s = "()[]{}"
print(isValid(s))
 