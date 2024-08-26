def find_block(row, col, board, visited, block_num):
    stack = [(row,col)]
    block = []
    
    while stack:
        row, col = stack.pop()
        
        key = (row,col)
        if key in visited:
            continue
        visited.add(key)
        block.append(key)
        
        for dir in [(0,1),(0,-1),(1,0),(-1,0)]:
            nrow = row + dir[0]
            ncol = col + dir[1]
            
            if 0 <= nrow < len(board) and 0 <= ncol < len(board[0]) and board[nrow][ncol] == block_num:
                stack.append((nrow, ncol))

    return block

def get_blocks(board, block_num):
    visited = set()
    blocks = []    
    for row in range(len(board)):
        for col in range(len(board[0])):
            if (row,col) in visited:
                continue
            if board[row][col] == block_num:
                blocks.append(find_block(row, col, board, visited, block_num))
    return blocks
    
def normalize_block(blocks):
    rescalers = []
    for block in blocks:
        min_x = float('inf')
        min_y = float('inf')
        max_x = -float('inf')
        max_y = -float('inf')
        for row, col in block:
            min_x = min(min_x, col)
            min_y = min(min_y, row)
            max_x = max(max_x, col)
            max_y = max(max_y, row)
        rescalers.append((min_x, min_y, max_x, max_y))

    new_blocks = []
    for block, scaler in zip(blocks, rescalers):
        min_x, min_y, max_x, max_y = scaler
        n_row = max_y - min_y + 1
        n_col = max_x - min_x + 1
        rescale_block = [(r - min_y, c - min_x) for r, c in block]
        new_block = [[0 for _ in range(n_col)] for _ in range(n_row)]
        for row in range(n_row):
            for col in range(n_col):
                if (row,col) in rescale_block:
                    new_block[row][col] = 1                     
        new_blocks.append(new_block)
    return new_blocks

def rotate_block(block):
    return [list(row) for row in zip(*block[::-1])]

def find_match_block(game_block, table_blocks, matches, used):
    for i, table_block in enumerate(table_blocks):
        if i in used:
            continue    
        rotated_t_b = rotate_block(table_block)
        for _ in range(4):
            if game_block == rotated_t_b:
                matches.append(game_block)
                used.add(i)
                return
            rotated_t_b = rotate_block(rotated_t_b)

def solution(game_board, table):
    
    game_blocks = get_blocks(game_board, 0)
    new_game_blocks = normalize_block(game_blocks)
    table_blocks = get_blocks(table, 1)
    new_table_blocks = normalize_block(table_blocks)
    
    used = set()
    matches = []
    for game_block in new_game_blocks:
        find_match_block(game_block, new_table_blocks, matches, used)
    
    match_cnt = 0 
    
    for block in matches:
        for row in block:
            match_cnt += row.count(1)
    # print(match_cnt)
    return match_cnt
    # print(new_game_blocks)
    # print(new_table_blocks)
    # print(rotate_block([[1],[1]]))
    
solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])
solution([[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]])