def generateDocument(characters, document):
    # Write your code here.
	for character in document:
        documentFrequency = countCharacterFrequency(character, document)
        charactersFrequency = countCharacterFrequency(character, characters)
        
        if documentFrequency > charactersFrequency:
            return False
    return True


def countCharacterFrequency(character, target):
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1
    return frequency
