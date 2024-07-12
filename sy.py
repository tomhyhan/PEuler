from collections import defaultdict

def solution(n, costs):
    graph = defaultdict(list)
    
    for s, e, c in costs:
        graph[s].append((e,c))
        graph[e].append((s,c))

    visited = {}
    stack = [(0, 0)]
    start = 0
    while stack:
        node, current_c = stack.pop()
        
        if node == start and len(visited) == n:
            print(current_c)
            break
        
        if node in visited:
            continue
        visited[node] = current_c
        
        for dest, next_c in graph[node]:
            stack.append((dest, current_c + next_c))

            
solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,8],[2,3,1]])