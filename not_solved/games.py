import heapq

def solution(maps):
    n_rows = len(maps)
    n_cols = len(maps[0])
    
    queue = [(0,0,0)]
    seen = set()
    
    while queue:
        distance, row, col = heapq.heappop(queue)
    
        key = (row, col)
        if (key in seen):
            continue
        seen.add(key)
        
        if row == n_rows-1 and col == n_cols-1:
            return distance+1
        
        for dir in [(1,0),(-1,0),(0,1),(0,-1)]:
            nrow = row + dir[0]
            ncol = col + dir[1]
            if 0 <= nrow < n_rows and 0 <= ncol < n_cols and maps[nrow][ncol] == 1:
                heapq.heappush(queue, (distance+1,nrow,ncol))
    return -1

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
# solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])