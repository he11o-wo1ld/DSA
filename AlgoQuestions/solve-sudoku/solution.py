def solveSudoku(board):
    # Write your code here.
    digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    rows = [{*digits} for _ in range(9)]
    cols = [{*digits} for _ in range(9)]
    boxes = [{*digits} for _ in range(9)]

    def solve():
        if not to_visit:
            return True
            
        x, y = 0, 0
        mincandidates = 10
        choices = None

        for i, j in to_visit:
            row, col, box = rows[i], cols[j], boxes[(i//3)*3 + j//3]
            candidates = row & col & box
            if len(candidates) < mincandidates:
                mincandidates = len(candidates)
                choices = candidates
                xrow, xcol, xbox = row, col, box
                x, y = i, j
        to_visit.discard((x, y))
        for choice in choices:
            board[x][y] = choice
            xrow.discard(choice)
            xcol.discard(choice)
            xbox.discard(choice)
            if solve():
                return True

            xrow.add(choice)
            xcol.add(choice)
            xbox.add(choice)
        to_visit.add((x, y))

    to_visit = set()
    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == 0:
                to_visit.add((i,j))
            else:
                rows[i].discard(val)
                cols[j].discard(val)
                boxes[(i//3)*3+j//3].discard(val)

    solve()
    
    return board


board = [
  [7, 8, 0, 4, 0, 0, 1, 2, 0],
  [6, 0, 0, 0, 7, 5, 0, 0, 9],
  [0, 0, 0, 6, 0, 1, 0, 7, 8],
  [0, 0, 7, 0, 4, 0, 2, 6, 0],
  [0, 0, 1, 0, 5, 0, 9, 3, 0],
  [9, 0, 4, 0, 6, 0, 0, 0, 5],
  [0, 7, 0, 3, 0, 0, 0, 1, 2],
  [1, 2, 0, 0, 0, 7, 4, 0, 0],
  [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
print(solveSudoku(board))




















