# time complexity: O(n*2^n) | space complexity: O(n*2^n)

def powerset(array):
    subsets = [[]]
    for idx in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [idx])
    return subsets
