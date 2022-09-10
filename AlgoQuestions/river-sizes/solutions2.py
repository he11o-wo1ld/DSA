class Size:
    def __init__(self, value=0):
        self.value = value


def riverSizes(matrix):
    sizes = []
    for r, row in enumerate(matrix):
        for c, cell in enumerate(row):
            if cell == 1:
                sizes.append(get_river(r, c, matrix, Size()))
    return sizes


def get_river(i, j, matrix, size):
    size.value += 1
    matrix[i][j] = 0

    for n, m in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if 0 <= n < len(matrix) and 0 <= m < len(matrix[n]) and matrix[n][m]:
            get_river(n, m, matrix, size)
    return size.value
