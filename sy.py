from collections import defaultdict, deque

def solution(n, costs):
    graph = defaultdict(list)
    
    for s, e, c in costs:
        graph[s].append((e,c))
        graph[e].append((s,c))

    # visited = {}
    min_cost = float("inf")
    for node in range(n):
        queue = deque([(node, 0)])
        visited = {}
        total_cost = 0 
        
        while queue:
            current_n, cost = queue.popleft()

            if current_n in visited:
                total_cost = current_n
                continue
            visited.add(current_n)

            for nnode, ncost, in graph[current_n]:
                queue.append((nnode,cost + ncost))                
        min_cost = min(min_cost, total_cost)

    print(min_cost)
    return min_cost            

# solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,8],[2,3,1]])
# solution(7, [[2, 3, 7], [3, 6, 13], [3, 5, 23], [5, 6, 25], [0, 1, 29], [1, 5, 34], [1, 2, 35], [4, 5, 53], [0, 4, 75]])
# solution(5,[[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]])
# solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]])
# solution(5,[[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]])
# solution(5,[[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 3], [2, 3, 8], [3, 4, 1]])
solution(6,[[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]])