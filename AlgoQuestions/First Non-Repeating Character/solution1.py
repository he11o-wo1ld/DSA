def firstNonRepeatingCharacter(string):
    # Write your code here.
	characterDict = {}
    for character in string:
        if character in characterDict:
            characterDict[character] += 1
        else:
            characterDict[character] = 1
    for i in characterDict:
        if characterDict[i] == 1:
            return string.index(i)
	return -1
