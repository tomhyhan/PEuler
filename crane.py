def remove(container, containers):
    visited = set()
    remove_list = set()
    
    stack = [(0,0)]
    while stack:
        key = stack.pop()
        row, col = key

        if key in visited:
            continue
        visited.add(key)
        
        for dir in [(0,1),(0,-1),(1,0),(-1,0)]:
            nrow = row + dir[0]           
            ncol = col + dir[1]           

            if 0 <= nrow < len(containers) and 0 <= ncol < len(containers[0]):
                if containers[nrow][ncol] == '@':
                    stack.append((nrow, ncol)) 
                if containers[nrow][ncol] == container:
                    remove_list.add((nrow, ncol))
    return remove_list
    
def solution(storage, requests):
    n_rows = len(storage)
    n_cols = len(storage[0])
    pad_size = 1
    containers = [['@' for _ in range(n_cols + pad_size*2)] for _ in range(n_rows + pad_size * 2)]
    
    for i in range(n_rows):
        for j in range(n_cols):
            containers[i+pad_size][j+pad_size] = storage[i][j]
            
    for request in requests:
        container = request[0]
        if len(request) == 2:
            for i in range(n_rows):
                for j in range(n_cols):
                    if containers[i+pad_size][j+pad_size] == container:
                        containers[i+pad_size][j+pad_size] = '@'
        else:
            remove_list = remove(container, containers)
            for r, c in remove_list:
                containers[r][c] = '@'
    
    n_containers = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if containers[i+pad_size][j+pad_size] != '@':
                n_containers += 1
    # print(n_containers)
    return n_containers
        
solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"])
solution(["HAH", "HBH", "HHH", "HAH", "HBH"], ["C", "B", "B", "B", "B", "H"])