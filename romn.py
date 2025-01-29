from collections import deque

def solution(arrows):
    DIRS = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    
    a_map = set()
    seen = set()
    
    n_rooms = 0
    
    r, c = 0, 0
    for arrow in arrows:
        nr = r + DIRS[arrow][0]
        nc = c + DIRS[arrow][1]
        a_map.add(((r,c), (nr,nc)))
        
        seen.add((r,c))
        
        if (nr, nc) in seen:
            n_rooms += 1
        
        r = nr
        c = nc
    
    # print(n_rooms)
    return n_rooms

solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0])