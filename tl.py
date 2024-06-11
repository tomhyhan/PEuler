from collections import defaultdict

def dfs(start_node, graph):
    visited = set()

    stack = [(start_node, 0)]
    max_d = 0
    max_nodes = []
    while stack:
        node, distance = stack.pop()
        
        if node in visited:
            continue
        visited.add(node)
        
        if distance > max_d:
            max_d = distance
            max_nodes = [node]
        elif distance == max_d:
            max_nodes.append(node)

        for nnode in graph[node]:
            stack.append((nnode, distance+1))

    return max_d, max_nodes
    
def solution(n, edges):
    graph = defaultdict(list)
    
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    distance, max_nodes = dfs(1, graph)
    distance, max_nodes = dfs(max_nodes[0], graph)
    
    if len(max_nodes) > 1:
        return distance
    
    distance, max_nodes = dfs(max_nodes[0], graph)
    
    return distance -1 if len(max_nodes) == 1 else distance
    
    
    print(distance, max_nodes)

# solution(4,[[1,2],[2,3],[3,4]])
solution(5,[[1,5],[2,5],[3,5],[4,5]])