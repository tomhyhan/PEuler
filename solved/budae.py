def solution(n, roads, sources, destination):
    DP = [[float("inf") for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        DP[i][i] = 0
    
    for s, e in roads:
        DP[s][e] = 1
        DP[e][s] = 1
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    continue
                DP[i][j] = min(DP[i][j], DP[i][k]+ DP[k][j])
                
    result = []
    for source in sources:
        result.append(-1 if DP[source][destination] == float("inf") else DP[source][destination])
        
    return result

from collections import defaultdict
import heapq

def solution(n, roads, sources, destination):
    graph = defaultdict(list) 
    
    for s, e, in roads:
        graph[s].append(e)
        graph[e].append(s)
        
    visited = defaultdict(lambda: float("inf"))
    visited[destination] = 0
    queue = [(0,destination)]
    while queue:
        dist, node = heapq.heappop(queue)
        for nnode in graph[node]:
            new_dist = dist + 1
            if new_dist < visited[nnode]:
                visited[nnode] = new_dist
                heapq.heappush(queue, (new_dist, nnode))
        
    result = []        
    for source in sources:
        result.append(visited[source] if source in visited else -1)
    
    return result
# solution(3, [[1, 2], [2, 3]], [2, 3], 1)
solution(5,[[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]],[1, 3, 5],5)