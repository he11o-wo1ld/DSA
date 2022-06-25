# time: O(n^2*m) | space: O(n) 

def apartmentHunting(blocks, reqs):
    maxDistanceAtBlocks = [float('-inf') for i in blocks]

    for i in range(len(blocks)):
        for req in reqs:
            closestReqDistance = float("inf")
            for j in range(len(blocks)):
                if blocks[j][req] == True:
                    closestReqDistance = min(closestReqDistance, abs(i-j))
            
            maxDistanceAtBlocks[i] = max(closestReqDistance, maxDistanceAtBlocks[i])
    
    return getIndexAtMinValue(maxDistanceAtBlocks)

def getIndexAtMinValue(array):
    idxAtMax = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idxAtMax = i
    return idxAtMax


blocks = [
{
    "gym": False,
    "school": True,
    "store": False,
},
{
    "gym": True,
    "school": False,
    "store": False,
},
{
    "gym": True,
    "school": True,
    "store": False,
},
{
    "gym": False,
    "school": True,
    "store": False,
},
{
    "gym": False,
    "school": True,
    "store": True,
}
]
reqs = ["gym", "school", "store"]
print(apartmentHunting(blocks, reqs))