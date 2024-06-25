# 1000000
from collections import defaultdict
def solution(n, path, order):
    graph = defaultdict(list)
    for s, e in path:
        graph[s].append(e)
        graph[e].append(s)
    
    key = [0] * n
    lock = [0] * n 
    # 8 - 5, 6 - 7, 4 - 1
    # key - lock
    
    for k, l in order:
        key[k] = l
        lock[l] = k
    
    stack = [0]
    visited = set()
    visited_lock = set()
    
    while stack:
        node = stack.pop()
        
        if lock[node] != 0 and lock[node] not in visited:
            visited_lock.add(lock[node])
            continue
        
        if node in visited:
            continue
        visited.add(node)
        
        for nnode in graph[node]:
            stack.append(nnode)
            
        if node in visited_lock:
            stack.append(key[node])
    
    # print(visited)
    return True if len(visited) == n else False

solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]])

# solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]])