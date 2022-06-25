# time: O(n * k) | space: O(n)

def staircaseTraversal(height, maxSteps):
    return numberOfWaysToTop(height, maxSteps, {0:1, 1:1})
    
    
def numberOfWaysToTop(height, maxSteps, memoize):
    if height in memoize:
        return memoize[height]
    
    numberOfWay = 0
    for step in range(1, min(maxSteps, height) + 1):
        numberOfWay += numberOfWaysToTop(height-step, maxSteps, memoize)
        
    memoize[height] = numberOfWay
    return numberOfWay
    
    
height = 6
maxSteps = 2
print(staircaseTraversal(height, maxSteps))
