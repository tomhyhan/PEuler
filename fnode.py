# solution 1
from collections import defaultdict
def solution(n, edge):
    graph = defaultdict(list)
    for s, d in edge:
        graph[s].append(d)
        graph[d].append(s)
    
    visits = [float('inf') for _ in range(n+1)]
    
    stack = [(0, 1)]
    
    max_distance = float('-inf')
    while stack:
        distance, node = stack.pop()

        if distance >= visits[node]:
            continue
        visits[node] = distance
        max_distance = max(max_distance, distance)
        for nnode in graph[node]:
            stack.append((distance+1, nnode))

    return visits.count(max([v for v in visits if v != float('inf')]))

# solution 2
from collections import defaultdict, deque

def solution(n, edge):
    graph = defaultdict(list)
    for s, d in edge:
        graph[s].append(d)
        graph[d].append(s)
    
    visits = [float('inf') for _ in range(n+1)]
    seen = set()
    
    queue = deque([(0, 1)])
    
    while queue:
        distance, node = queue.pop()
        
        if node in seen:
            continue
        seen.add(node)
        
        visits[node] = distance
        for nnode in graph[node]:
            queue.appendleft((distance+1, nnode))
            
    return visits.count(max([v for v in visits if v != float('inf')]))

    print(visits)
    
    # [1, i, i, i, i, i, i]
    # [i, 1, 2, 2, i, i, i]
    # [i, 2, 1, 2, 2, 2, i]
    # [i, 2, 2, 1, 2, i, 2]
    # [i, i, 2, 2, 1, i, i]
    # [i, i, 2, i, i, 1, i]
    # [i, i, i, 2, i, i, 1]

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])