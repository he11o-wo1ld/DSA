def shiftGrid(grid, k):
    m = len(grid)
    n = len(grid[0])
    
    def getVal(p, v):
        return p * n + v
    
    def getPos(v):
        return [v // n, v % n]
    
    res = [[0 for _ in range(n)] for _ in range(m)]
    # res = [[0] * n for i in range(m)]
    
    for i in range(m):
        for j in range(n):
            newVal = (getVal(i, j) + k) % (m * n)
            newRow, newCol = getPos(newVal)
            res[newRow][newCol] = grid[i][j]
    return res


grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1

print(shiftGrid(grid, k))