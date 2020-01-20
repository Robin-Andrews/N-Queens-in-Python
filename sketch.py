board = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]


def check_diagonals(pos, board):
    """
    Check all 4 diagonals from given position in a 2d list separately.
    Returns True if there is a collison, else False.
    """
    num_rows, num_cols = len(board), len(board[0])
    row_num, col_num = pos
    collision = False

    # Lower-right diagonal from (row_num, col_num)
    i, j = row_num + 1, col_num + 1
    while i < num_rows and j < num_cols:
        if board[i][j] == 1:
            collision = True
        i, j = i + 1, j + 1

    # Upper-left diagonal from (row_num, col_num)
    i, j = row_num - 1, col_num - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            collision = True
        i, j = i - 1, j - 1

    # Upper-right diagonal from (row_num, col_num)
    i, j = row_num - 1, col_num + 1
    while i >= 0 and j < num_cols:
        if board[i][j] == 1:
            collision = True
        i, j = i - 1, j + 1

    # Lower-left diagonal from (row_num, col_num)
    i, j = row_num + 1, col_num - 1
    while i < num_cols and j >= 0:
        if board[i][j] == 1:
            collision = True
        i, j = i + 1, j - 1

    return collision


print(check_diagonals((1, 2), board))


# W, H = len(mat[0]), len(mat) 
# idx = list(range(W-1)) + list(range(W-1, W*H, W))
# rng = list(range(1, W)) + list(range(H, 0, -1))
# rng = map(lambda x: x if (x < min(W, H)) else min(W, H), rng)
# dia = [[i + (W-1) * m for m in range(r)] for i, r in zip(idx, rng)]

# arr = [e for row in mat for e in row] #Flatten the matrix
# for d in dia:
    # print([arr[e] for e in d][::-1])
    
    
# arr2 = [e for row in zip(*mat[::-1]) for e in row] #Flatten and rotate the matrix by 90°
# for d in dia[::-1]:
    # print([arr2[e] for e in d])
    
    
# test = [[1, 2, 3],
        # [4, 5, 6],
        # [7, 8, 9],
        # [10,11,12]]

# max_col = len(test[0])
# max_row = len(test)
# cols = [[] for _ in range(max_col)]
# rows = [[] for _ in range(max_row)]
# fdiag = [[] for _ in range(max_row + max_col - 1)]
# bdiag = [[] for _ in range(len(fdiag))]
# min_bdiag = -max_row + 1

# for x in range(max_col):
    # for y in range(max_row):
        # cols[x].append(test[y][x])
        # rows[y].append(test[y][x])
        # fdiag[x+y].append(test[y][x])
        # bdiag[x-y-min_bdiag].append(test[y][x])

# print(cols)
# print(rows)
# print(fdiag)
# print(bdiag)

    
