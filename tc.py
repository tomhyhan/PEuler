import heapq
from collections import defaultdict

def solution(n, start, end, roads, traps):
    ngraph = defaultdict(lambda: {"st":[], "opp": []}) 
    distances = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    # 1 → 2 → 3 → 2 → 4
    for s, e, d  in roads:
        ngraph[s]["st"].append(e)
        ngraph[e]["opp"].append(s)
        distances[s][e] = d
        distances[e][s] = d 

    print(ngraph)
    return
    # 1. Create a copy of graph in each iteration
    # 2. fix: find others ways without copying graph
    heap = [(0, start, True)]
    cnt = 0
    while heap:
        distance, node, straight = heapq.heappop(heap)
        
        if node == end:
            print(distance)
            break

        graph = sgraph if straight else ograph
        
        for nnode in graph[node]:
            next_d = distance + distances[node][nnode]
            next_s = not straight if nnode in traps else straight
            
            print(node, nnode, next_d, next_s)
            heapq.heappush(heap, (next_d, nnode, next_s))
            
        if cnt == 10:
            break
        cnt+= 1

# solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])

solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])