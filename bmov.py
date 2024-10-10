# use backtracking

def solution(n, m, x, y, queries):
    # 0 - left, 1 - right, 2 - up, 3 - down
    # up left right left up
    
    # go first and reverse turn, check if +1 step is in border
    directions = [(0,-1),(0,1),(-1,0),(1,0)]
    destinations = 0
    
    for query in reversed(queries):
        dir, steps = query
        str_dir = directions[dir]
        rev_dir = (-directions[dir][0], -directions[dir][1])
        dy = min(max(y + rev_dir[0] * steps, 0 ), n-1)
        dx = min(max(x + rev_dir[1] * steps, 0), m-1)
        
        by = dy + str_dir[0] * (steps+1)
        bx = dx + str_dir[1] * (steps+1)
        
        if 0 > bx or bx >= n or 0 > by or by >= y:
            destinations += abs((x + y) - (dy + dx))
        print(y, x)
        print(dy, dx)
        print(by, bx)
        print(str_dir, rev_dir)
        print()
        y = dy
        x = dx
        
        # break
    print(destinations)
    print([0,1] * -1)
# solution(2, 2, 0, 0, [[2,1],[0,1],[1,1],[0,1],[2,1]])
solution(2, 5, 0, 1, [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]])