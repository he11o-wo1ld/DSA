def generateDocument(characters, document):
    # Write your code here.
	characters_dict = {}
	for i in characters:
		if i in characters_dict:
			characters_dict[i] += 1
		else:
			characters_dict[i] = 1
	for i in document:
		if i not in characters_dict or characters_dict[i] == 0:
			return False
		characters_dict[i] -= 1
	return True
			