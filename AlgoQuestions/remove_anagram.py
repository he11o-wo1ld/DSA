def removeAnagrams(words):
    curr = words[0]
    for i in range(1, len(words)):
        if getAnagram(words[i], curr):
            words.remove(words[i])
        else:
            curr = words[i]
    return words
    
    
def getAnagram(self, word1, word2):
    if sorted(word1) == sorted(word2):
        return True
    return False


words = ["abba","baba","bbaa","cd","cd"]
print(removeAnagrams(words))