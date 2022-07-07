# time O(W * n * log(n) + )
def groupAnagrams(strs):
    anagrams = {}
    res = []
    for word in strs:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]

    for i in anagrams:
        res.append(anagrams[i])
    print(res)
    # return list(anagrams.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))