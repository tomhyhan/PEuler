from collections import defaultdict

def dfs(node, graph):
    visited = set()
    max_d = traverse(node, graph, 0, visited)
    return max_d

def traverse(node, graph, distance, visited):
    """
        check if max distance node has more than 1 nodes pointing to max distance node.
        
    """
    if node in visited:
        return distance-1
    visited.add(node)
    
    nodes = graph[node]

    max_d = 0
    max_node = node
    for nnode in nodes:
        max_d = max(max_d, traverse(nnode, graph, distance+1, visited))
        
    return max_d
    
def solution(n, edges):
    graph = defaultdict(list)
    
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    distance = dfs(2, graph)
    print(distance)

solution(4,[[1,2],[2,3],[3,4]])
solution(5,[[1,5],[2,5],[3,5],[4,5]])