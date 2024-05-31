from collections import defaultdict

def solution(board):
    
    n_row = len(board)
    n_col = len(board[0])
    
    total = 0
    while True:
        fill_board(board)
        squares = 0
        for row in range(n_row):
            for col in range(n_col):
                r_end = row + 1
                c_end = col + 2
                squares += is_square(row, col, r_end, c_end, board)
                r_end = row + 2
                c_end = col + 1
                squares += is_square(row, col, r_end, c_end, board)
        if not squares:
            break
        total += squares
        next_board(board)
    # print(total)
    return total
     
def fill_board(board):
    for col in range(len(board[0])):
        for row in range(len(board)):
            if board[row][col] != 0:
                break
            board[row][col] = '.'

def next_board(board):
    for col in range(len(board[0])):
        for row in range(len(board)):
            if board[row][col] not in ['.', '@']:
                break
            board[row][col] = 0
            
def is_square(row, col, r_end, c_end, board):
    if r_end < len(board) and c_end < len(board[0]):
        cnt = defaultdict(int)
        for r in range(row, r_end+1):
            for c in range(col, c_end+1):
               cnt[board[r][c]] += 1
        
        if '.' in cnt and cnt['.'] == 2 and len(cnt) == 2 and 0 not in cnt:
            for r in range(row, r_end+1):
                for c in range(col, c_end+1):
                    board[r][c] = 0
            return 1
    return 0


solution([[0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,4,0,0,0],
          [0,0,0,0,0,4,4,0,0,0],
          [0,0,0,0,3,0,4,0,0,0],
          [0,0,0,2,3,0,0,0,5,5],
          [1,2,2,2,3,3,0,0,0,5],
          [1,1,1,0,0,0,0,0,0,5]])