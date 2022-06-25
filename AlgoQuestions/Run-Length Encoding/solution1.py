def runLengthEncoding(string):
    # Write your code here
	currentLength = 1
	res = []
	
	for i in range(1, len(string)):
		currentCharacter = string[i]
		previousCharacter = string[i-1]
		if currentCharacter != previousCharacter or currentLength == 9:
			res.append(str(currentLength))
			res.append(previousCharacter)
			currentLength = 0
		currentLength += 1
	res.append(str(currentLength))
	res.append(string[len(string) - 1])
	return "".join(res)