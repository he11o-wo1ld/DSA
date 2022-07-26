def setZeroes(matrix):
    col0 = 1
    row = len(matrix)
    cols = len(matrix[0])
    
    for i in range(row):
        if matrix[i][0] == 0:
            col0 = 0
        
        for j in range(1,cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0 
                matrix[0][j] = 0
    
    for i in range((row-1), -1, -1):
        for j in range((cols - 1), 0, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        
        if col0 == 0:
            matrix[i][0] = 0
    print(matrix)

# matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(setZeroes(matrix))