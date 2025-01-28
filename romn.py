def solution(arrows):
    DIRS = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    
    
    a_map = set()
    a_map.add((0,0))
    r, c = 0, 0
    for arrow in arrows:
        nr, nc = DIRS[arrow]
        r += nr
        c += nc
        a_map.add((r,c))
    
    
    return 

solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0])