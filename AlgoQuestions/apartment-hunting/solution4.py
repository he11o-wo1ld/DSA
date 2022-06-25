# Solution 1 :
def apartmentHunting(blocks, reqs):
    Blocks = [float('-inf') for block in blocks]
    for i in range(len(blocks)):
        for req in reqs:
            distance = float('inf')
            for j in range(len(blocks)):
                if blocks[j][req]:  
                # if blocks item is True.
                    distance = min(distance, abs(i - j))    
                    # minimum distance between required blocks.
            Blocks[i] = max(Blocks[i], distance)

    val = float('inf')
    idx = 0

    for i, v in enumerate(Blocks):
        if v < val:
            val = v
            idx = i
    return idx

    return idx

"""for this solution, if the n is length of the blocks and m is length of reqs then, 
the time complexity is O(n^2*m) and the space complexity is O(n)."""

"""
step 1: Set a Block array for store the distance between the blocks.
step 2: First loop for getting the initial blocks index.
step 3: Second loop will get the requirements for the initial block, and define distance as infinite.
step 4: Third loop again loop threw blocks for perticular requirements and it'll check wheather it's True or False,
step 5: If the block requirements is True then we store the minimum distance between initial block and Second block index.
step 6: If distance between initial block and second block is less than current distance, distance'll overwrite by the minimum distance.
step 7: When the loop is over then it'll come outside and replace the value at perticular index of Blocks.
stpe 8: Initialize a val as infinite and idx as 0.
step 9: Run a loop in Blocks and get minimum value index and return the index as answer.
"""


# Solution 2:
def apartmentHunting1(blocks, reqs):
    minDistances = list(map(lambda req: MinDistances(blocks, req), reqs))       #O(n*m)
    maxDistances = MaxDistances(blocks, minDistances)                #O(n*m)
    return findIndex(maxDistances)                                     #O(n*m)


def MinDistances(blocks, req):
    minDistances = [0 for i in blocks]
    closestReqIdx = float("inf")

    for i in range(len(blocks)):
        if blocks[i][req] == True:
            closestReqIdx = i
        minDistances[i] = abs(i - closestReqIdx)

    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = min(minDistances[i], abs(closestReqIdx - i))
    return minDistances


def MaxDistances(blocks, minDistancesFromBlocks):
    maxDistances = [0 for i in blocks]

    for i in range(len(blocks)):
        minDistances = list(map(lambda distances: distances[i], minDistancesFromBlocks))
        maxDistances[i] = max(minDistances)
    return maxDistances


def findIndex(blocks):
    idx = 0
    minValue = float("inf")

    for i, v in enumerate(blocks):
        if v < minValue:
            minValue = v
            idx = i
    return idx


"""In this solution the time complexity is O(n*m) and space complexity is O(n*m), where n = length of blocks and m = length of requirements."""

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
print(apartmentHunting1(blocks, reqs))