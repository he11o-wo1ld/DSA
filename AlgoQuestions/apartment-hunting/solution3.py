def apartmentHunting(blocks, reqs):
    distance = {}

    def calcDist(buildings, blockNum):
        currentBuildingDist = len(blocks)
        for idx, othrtBlocks in enumerate(blocks):
            if othrtBlocks[buildings]:
                tmpBuildingDist = abs(idx - blockNum)

                if currentBuildingDist > tmpBuildingDist:
                    currentBuildingDist = tmpBuildingDist
        # minBuildingDist.append(currentBuildingDist)


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