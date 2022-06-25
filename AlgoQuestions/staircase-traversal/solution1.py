# time: O(n*k) | space: O(n)

def staircaseTraversal(height, maxSteps):
    return numberOfWaysToTop(height, maxSteps)
    
def numberOfWaysToTop(height, maxSteps):
    if height <= 1:
        return 1
    numberOfWay = 0
    for step in range(1, min(maxSteps, height) + 1):
        numberOfWay += numberOfWaysToTop(height-step, maxSteps)
    return numberOfWay


height = 8
maxSteps = 2
print(staircaseTraversal(height, maxSteps))
