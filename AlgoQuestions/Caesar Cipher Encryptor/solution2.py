def caesarCipherEncryptor(string, key):
    # Write your code here.
    newLetters = []
	newKey = key % 26
	alphabet = list("abcdefghijklmnopqrstuvwxyz")
	for letter in string:
		newLetters.append(getNewLetter(letter, newKey, alphabet))
	return "".join(newLetters)

def getNewLetter(letter, newKey, alphabet):
	newLetterCode = alphabet.index(letter) + newKey
	return alphabet[newLetterCode % 26]
