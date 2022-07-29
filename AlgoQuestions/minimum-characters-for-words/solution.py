def minimumCharactersForWords(words):
    maximumCharacterFrequencies = {}

    for word in words:
        characterFrequencies = countCharacterFrequencies(word)
        updateMaximumFrequecies(characterFrequencies, maximumCharacterFrequencies)

    return makeArrayFromCharacterFrequencies(maximumCharacterFrequencies)

def countCharacterFrequencies(string):
    characterFrequencies = {}

    for character in string:
        if character not in characterFrequencies:
            characterFrequencies[character] = 0

        characterFrequencies[character] += 1
    return characterFrequencies

def updateMaximumFrequecies(frequencies, maximumFrequencies):
    for character in frequencies:
        frequency = frequencies[character]

        if character in maximumFrequencies:
            maximumFrequencies[character] = max(frequency, maximumFrequencies[character])
        else:
            maximumFrequencies[character] = frequency

def makeArrayFromCharacterFrequencies(characterFrequencies):
    characters = []

    for character in characterFrequencies:
        frequency = characterFrequencies[character]

        for _ in range(frequency):
            characters.append(character)
    return characters


words = ["this", "that", "did", "deed", "them!", "a"]
print(minimumCharactersForWords(words))
