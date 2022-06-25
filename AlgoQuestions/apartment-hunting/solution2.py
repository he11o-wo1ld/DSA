# n = size of blocks
# m = size of reqs
# time: O(n*m) | space: O(n*m) 


def apartmentHunting(blocks, reqs):
    minDistances = list(map(lambda req: MinDistances(blocks, req), reqs))       #O(n*m)
    maxDistances = MaxDistances(blocks, minDistances)                #O(n*m)
    return findIndex(maxDistances)                                     #O(n*m)


def MinDistances(blocks, req):
    minDistances = [0 for i in blocks]
    closestIdx = float("inf")

    for i in range(len(blocks)):
        if blocks[i][req] == True:
            closestIdx = i
        minDistances[i] = abs(i - closestIdx)

    # print(minDistances)

    for i in reversed(range(len(blocks))):
        if blocks[i][req] == True:
            closestIdx = i
        minDistances[i] = min(minDistances[i], abs(closestIdx - i))
    # print(minDistances)
    return minDistances


def MaxDistances(blocks, minDistancesFromBlocks):
    maxDistances = [0 for i in blocks]

    for i in range(len(blocks)):
        minDistances = list(map(lambda distances: distances[i], minDistancesFromBlocks))
        maxDistances[i] = max(minDistances)
    print(maxDistances)
    return maxDistances


def findIndex(blocks):
    idx = 0
    minValue = float("inf")

    for i, v in enumerate(blocks):
        if v < minValue:
            minValue = v
            idx = i
    return idx


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