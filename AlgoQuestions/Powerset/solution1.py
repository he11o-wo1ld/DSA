# time complexity: O(n*2^n) | space complexity: O(n*2^n)

def powerset(array, idx=None):
    if array == []:
        return [[]]
        
    if idx is None:
        idx = len(array) - 1
        
    elif idx < 0:
        return [[]]
        
    ele = array[idx]

    subsets = powerset(array, idx-1)

    for i in range(len(subsets)):
        currentSubsets = subsets[i]
        subsets.append(currentSubsets + [ele])
    return subsets