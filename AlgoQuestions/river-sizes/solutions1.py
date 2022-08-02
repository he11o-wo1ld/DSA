def riverSizes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    ans = []

    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited and matrix[row][col] == 1:
                size = dfs(row, col, visited, matrix)
                ans.append(size)
    return ans


def dfs(row, col, visited, matrix):
    if row not in range(len(matrix)) or col not in range(len(matrix[0])) or matrix[row][col] == 0 or (row, col) in visited:
        return 0
    visited.add((row, col))
    size = 0

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        size += dfs(row+dx, col+dy, visited, matrix)
    return size + 1