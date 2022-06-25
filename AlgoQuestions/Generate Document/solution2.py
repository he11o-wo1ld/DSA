def generateDocument(characters, document):
    # Write your code here
	alreadyCounted = set()
    for character in document:
        if character in alreadyCounted:
            continue
        documentFrequency = countCharacterFrequency(character, document)
        charactersFrequency = countCharacterFrequency(character, characters)
        
        if documentFrequency > charactersFrequency:
            return False
        alreadyCounted.add(character)
    return True


def countCharacterFrequency(character, target):
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1
    return frequency
