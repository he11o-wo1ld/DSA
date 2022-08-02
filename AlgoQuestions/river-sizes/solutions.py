def riverSizes(matrix):
    sizes = []
    visited = [[False for i in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, sizes)
    return sizes

def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    nodesToExplore = [[i, j]]

    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]

        if visited[i][j]:
            continue

        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1
        unvisitedNeighbors = getUnvisited(i, j, matrix, visited)

        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)

    if currentRiverSize > 0:
        sizes.append(currentRiverSize)

def getUnvisited(i, j, matrix, visited):
    unvisited = []
    if i > 0 and not visited[i-1][j]:
        unvisited.append([i-1, j])

    if i < len(matrix) - 1 and not visited[i+1][j]:
        unvisited.append([i+1, j])

    if j > 0 and not visited[i][j-1]:
        unvisited.append([i, j-1])

    if j < len(matrix) - 1 and not visited[i][j+1]:
        unvisited.append([i, j+1])

    return unvisited


matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
    ]

print(riverSizes(matrix))
