# time: O(n*k) | space: O(n)

def staircaseTraversal(height, maxSteps):
    waysToTop = [0 for _ in range(height+1)]
    waysToTop[0] = 1
    waysToTop[1] = 1
    
    for currentHeight in range(2, height+1):
        step = 1
        while step <= maxSteps and step <= currentHeight:
            waysToTop[currentHeight] = waysToTop[currentHeight] + waysToTop[currentHeight - step]
            step += 1
            
    return waysToTop[height]

height = 8
maxSteps = 2
print(staircaseTraversal(height, maxSteps))
