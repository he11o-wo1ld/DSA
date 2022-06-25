def caesarCipherEncryptor(string, key):
    # Write your code here.
	newLetter = []
	newKey = key % 26
	for letter in string:
		newLetter.append(getNewLatter(letter, newKey))
	return "".join(newLetter)

def getNewLatter(letter, newKey):
	newLetterCode = ord(letter) + newKey
	return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode %122)