def minimumPassesOfMatrix(matrix):
    passes = convertNegetive(matrix)
    return passes - 1 if not convertNegetive(matrix) else -1


def convertNegetive(matrix):
    Queue = getAllPositivePositions(matrix)

    passes = 0

    while len(Queue) > 0:
        currentSize = len(Queue)

        while currentSize > 0:
            currentRow, currentCol = Queue.pop(0)

            adjacentPositions = getAdjacentpositions(currentRow, currentCol, matrix)

            for position in adjacentPositions:
                row, col = position

                if matrix[row][col] < 0:
                    matrix[row][col] *= -1
                    Queue.append([row, col])

            currentSize -= 1

        passes += 1

    return passes


def getAllPositivePositions(matrix):
    positivePositions = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            # value = matrix[row][col]

            if matrix[row][col] > 0:
                positivePositions.append([row, col])
                
    return positivePositions


def getAdjacentpositions(row, col, matrix):
    adjacentPositions = []

    if row > 0:
        adjacentPositions.append([row - 1, col])

    if row < len(matrix) - 1:
        adjacentPositions.append([row + 1, col])

    if col > 0:
        adjacentPositions.append([row, col - 1])

    if col < len(matrix[0]) - 1:
        adjacentPositions.append([row, col + 1])

    return adjacentPositions


def containNegetive(matrix):
    for row in matrix:
        for value in row:
            if value < 0:
                return True

    return False