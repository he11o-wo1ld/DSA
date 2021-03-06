# from dis import dis
#
#
# def appartmentHunting(blocks, reqs):
#     Blocks = [float('-inf') for block in blocks]
#     for i in range(len(blocks)):
#         for req in reqs:
#             distance = float('inf')
#             for j in range(len(blocks)):
#                 if blocks[j][req]:
#                 # if blocks item is True.
#                     distance = min(distance, abs(i - j))
#                     # minimum distance between required blocks.
#             Blocks[i] = max(Blocks[i], distance)
#
#     val = float('inf')
#     idx = 0
#
#     for i, v in enumerate(Blocks):
#         if v < val:
#             val = v
#             idx = i
#     return idx
#
#     return idx
#
#
# blocks = [
# {
#     "gym": False,
#     "school": True,
#     "store": False,
# },
# {
#     "gym": True,
#     "school": False,
#     "store": False,
# },
# {
#     "gym": True,
#     "school": True,
#     "store": False,
# },
# {
#     "gym": False,
#     "school": True,
#     "store": False,
# },
# {
#     "gym": False,
#     "school": True,
#     "store": True,
# }
# ]
# reqs = ["gym", "school", "store"]
# print(appartmentHunting(blocks, reqs))




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

"""This is Brute-force solution using three for loops, if the n is length of the blocks and m is length of reqs then, 
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
    minDistances = list(map(lambda req: MinDistances(blocks, req), reqs))
    maxDistances = MaxDistances(blocks, minDistances)
    return findIndex(maxDistances)


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


"""This optimize time but using extra space for storing block data, In this solution the time complexity is O(n*m) and space complexity is O(n*m), where n = length of blocks and m = length of requirements."""

"""
step 1: First we are creating two list, 1. minimumDistance, 2.maximumDistance. The minimumDistance will get the minimum distance between blocks based on requirements, and the maximumDistance list contains the max of every minimumDistance array.
step 2: In the maxDistance function creating a list of length blocks, here the first loop will run get the minimum distance between blocks from accending order, then the second loop will run in a reversed order get the minimum distance between blocks.
Ex:
1st loop:
gym : [inf, 0, 0, 1, 2]
school : [1, 0, 0, 1, 2]
store : [0, 1, 0, 0, 0]
2nd loop:
gym : [0, 1, 0, 0, 0]
school : [inf, inf, inf, inf, 0]
store : [4, 3, 2, 1, 0]

minDistance function will return this array of list : [[1, 0, 0, 1, 2], [0, 1, 0, 0, 0], [4, 3, 2, 1, 0]]

step 3: maxDistance function will get call with blocks and min distance array,
step 4: In the maxDistance function define an array maxDistances of length blocks, then run a loop on minDistance array and get the max element and assign to the maxDistances arraty index.
Ex:
In the maxDistance array contains all the maximum element of minimumDistance array, it'll return [4, 3, 2, 1, 2] array.

step 5: Run another loop on maxDistance array to get the minimum distance which is 1 at index 3, so the helper function findIndex will return 3 as output.
step 6: Finally return the findIndex output as 3.

"""

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
print(apartmentHunting1(blocks, reqs))
