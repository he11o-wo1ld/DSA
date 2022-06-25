def firstNonRepeatingCharacter(string):
    for idx in range(len(string)):
        
        foundDuplicate = False
        
        for idx2 in range(len(string)):
            if string[idx] == string[idx2] and idx != idx2:
                foundDuplicate = True
        
        if not foundDuplicate:
            return idx
        
    return -1