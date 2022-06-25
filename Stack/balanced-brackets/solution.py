def balancedBrackets(string):
	In = {'(':1, '{':2, '[':3}
	Out = {')':1, '}':2, ']':3}

	stack = []

	if string == '':
		return True

	if string[0] not in In:
		return False

	for i in range(len(string)):
		if string[i] in In:
			stack.append(string[i])

		elif string[i] in Out:
			l = len(stack)-1
			if In[stack[l]] == Out[string[i]]:
				stack.pop()
			else:
				return False
	return len(stack) == 0


string = "(((((({{{{{[[[[[([)])]]]]]}}}}}))))))"
print(balancedBrackets(string))