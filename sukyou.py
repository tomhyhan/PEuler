from collections import defaultdict

def fill_land(row, col, land, seen):
    visited = set()
    tops = defaultdict(list)
    area = 0
    stack = [(row, col)]
    while stack:
        key = stack.pop()
        row, col = key
        
        if key in seen:
            continue    
        seen.add(key)
        visited.add(key)
        area += 1
        
        trow = row + -1
        tcol = col
        if trow < 0 or trow >= len(land) or land[trow][tcol] == 0:
            tops[col].append(row)

        for dir in [(0,1),(0,-1),(1,0),(-1,0)]:
            nrow = row + dir[0]
            ncol = col + dir[1]
            if 0 <= nrow < len(land) and 0 <= ncol < len(land[0]) and land[nrow][ncol] == 1:
                
                stack.append((nrow, ncol))   
    tops = set([(min(rows), col) for col, rows in tops.items()])
    
    for key in visited:
        r, c = key
        land[r][c] = area if key in tops else 0

def solution(land):

    seen = set()
    
    for row in range(len(land)):
        for col in range(len(land[0])):
            if land[row][col] == 0 or (row,col) in seen:
                continue
            fill_land(row, col, land, seen)
        
    max_area = 0
    for col in range(len(land[0])):
        curr_area = 0
        for row in range(len(land)):
            curr_area += land[row][col]
        max_area = max(max_area, curr_area)
        
    return max_area

solution([[0, 0, 0, 1, 1, 1, 0, 0], 
          [0, 0, 0, 0, 1, 1, 0, 0], 
          [1, 1, 0, 0, 0, 1, 1, 0], 
          [1, 1, 1, 0, 0, 0, 0, 0], 
          [1, 1, 1, 0, 0, 0, 1, 1]])