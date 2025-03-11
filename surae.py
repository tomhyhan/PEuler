
# 1 -> 3
# 2 -> 4
# 0 -> blank
# 5 -> wall

def is_blank(row, col, maze):
    if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != 5:
        return True
    return False

def move(moves, red, blue, r_end, b_end, r_visited, b_visited, maze):
    if red == blue:
        return float('inf')
    
    if red == r_end and blue == b_end:
        return moves
    
    r_moves = [(0,0)] if red == r_end else [(0,1),(0,-1),(1,0),(-1,0)]
    b_moves = [(0,0)] if blue == b_end else [(0,1),(0,-1),(1,0),(-1,0)]
    
    lowest_moves = float('inf')
    for rd in r_moves:
        rrow = red[0] + rd[0]
        rcol = red[1] + rd[1]
        nred = (rrow, rcol) 
        if is_blank(rrow, rcol, maze) and (red == nred or nred not in r_visited):
            r_visited.add(nred)
            for bd in b_moves:
                brow = blue[0] + bd[0]
                bcol = blue[1] + bd[1]
                nblue = (brow, bcol) 
                if nblue == red and nred == blue:
                    continue
                if is_blank(brow, bcol, maze) and (blue == nblue or nblue not in b_visited):
                    b_visited.add(nblue)
                    cmoves = move(moves+1, nred, nblue, r_end, b_end, r_visited, b_visited, maze)
                    lowest_moves = min(lowest_moves, cmoves)
                    if nblue in b_visited: 
                        b_visited.remove(nblue)
            if nred in r_visited:
                r_visited.remove(nred)
    
    return lowest_moves

def solution(maze):
    r_start = None
    b_start = None
    r_end = None
    b_end = None
    
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                r_start = (i,j)             
            if maze[i][j] == 2:
                b_start = (i,j)             
            if maze[i][j] == 3:
                r_end = (i,j)             
            if maze[i][j] == 4:
                b_end = (i,j)             
    
    b_visited = set([r_start])
    r_visited = set([b_start])

    moves = move(0, r_start, b_start, r_end, b_end, b_visited, r_visited, maze)    
    # print(moves)
    return moves if moves != float('inf') else 0

# 3
solution([[1, 4], [0, 0], [2, 3]])
solution([[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]])
solution([[1, 5], [2, 5], [4, 5], [3, 5]])
solution([[4, 1, 2, 3]])