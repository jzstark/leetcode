import copy 
import time

# assume classic 9x9 sudoku board 
_N = 3

block_l = [0,0,0,3,3,3,6,6,6]
block_u = [2,2,2,5,5,5,8,8,8]
def generate_block_id(i, j):
    il = block_l[i]; iu = block_u[i]
    jl = block_l[j]; ju = block_u[j]
    return [(i, j) for i in range(il, iu+1) for j in range(jl, ju+1)]


def find_valid(i, j, board):
    total = set([str(x) for x in range(1,10)])
    total.add('.')
    row = set(board[i])
    col = set([board[r][j] for r in range(9)])
    block = set([board[a][b] for (a,b) in generate_block_id(i,j)])
    return total - set.union(row, col, block)


# next position that is '.'
def get_next_empty_pos(i, j, board):
    idx = i * 9 + j
    while (idx < 80):
        idx += 1
        a = idx // 9; b = idx % 9
        if board[a][b] == '.':
            return (a, b)
    return None

def dfs(i, j, board): #at point i, j 
    results = []
    values = find_valid(i, j, board)
    if values == []: return False 

    pos = get_next_empty_pos(i, j, board)
    if pos is None: return False

    board = copy.deepcopy(board)
    for v in values:
        board[i][j] = v
        r = dfs(pos[0], pos[1], board) 
        results.append(r)
    return all(results)


def isValidSudoku(board) -> bool:
    c = [ x.count('.') for x in board ]
    if 81 - sum(c) <= 15 : return True

    return dfs(0, 0, board)


board1 = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
# expected: True 

board2 = \
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
# expected: False

board3 = \
[[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."]]

board4 = \
[[".",".","5",".",".",".",".",".","6"],
[".",".",".",".","1","4",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".","9","2",".","."],
["5",".",".",".",".","2",".",".","."],
[".",".",".",".",".",".",".","3","."],
[".",".",".","5","4",".",".",".","."],
["3",".",".",".",".",".","4","2","."],
[".",".",".","2","7",".","6",".","."]]

print(isValidSudoku(board4))
