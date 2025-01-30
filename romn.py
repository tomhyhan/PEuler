from collections import defaultdict

def solution(arrows):
    DIRS = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    
    a_map = defaultdict(set)
    n_rooms = 0
    row, col = 0, 0
    
    for arrow in arrows:
        for _ in range(2):
            nrow = row + DIRS[arrow][0]
            ncol = col + DIRS[arrow][1]

            prev = (row, col)
            curr = (nrow, ncol)
            if curr in a_map and prev not in a_map[curr]:
                n_rooms += 1
            a_map[curr].add(prev)            
            a_map[prev].add(curr)            

            row = nrow
            col = ncol
    
    return n_rooms

# print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
print(solution([5, 2, 7, 1, 6, 3]))
print(solution([6, 5, 2, 7, 1, 4, 2, 4, 6]))

print(solution([6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0] ))