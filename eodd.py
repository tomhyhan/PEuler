from collections import defaultdict

EVENODD = "EVENODD"
OEVENODD = "OEVENODD"

def kind(num_children, node_val):
    if (node_val % 2 == 0 and num_children % 2 == 0) or (node_val % 2 == 1 and num_children % 2 == 1):
        return EVENODD
    elif ((node_val % 2 == 0 and num_children % 2 == 1) or (node_val % 2 == 1 and num_children % 2 == 0)):
        return OEVENODD

def one_kind_tree(node, graph, visited):
    # 
    if set(graph[node])  == 0:
        print("asdf")
        return kind(0, node)
    
    if node in visited:
        return None
    
    visited.add(node)
    n_childs = 0    
    child_conditions = set()
    for child_node in graph[node]:
        condition = one_kind_tree(child_node, graph, visited)
        if condition is not None:
            child_conditions.add(condition)
        n_childs += 1
        
    print(node, child_conditions, graph[node], visited)
    if len(child_conditions) == 2:
        return False
    
    return kind(n_childs, node)

def solution(nodes, edges):
    # divide tree groups
    # use dfs 
    graph = defaultdict(list)
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
    
    print(graph)
    # for node in nodes:
    visited = set()
    print(one_kind_tree(6, graph, visited))      

solution([11, 9, 3, 2, 4, 6], [[9, 11], [2, 3], [6, 3], [3, 4]])
# solution([9, 15, 14, 7, 6, 1, 2, 4, 5, 11, 8, 10], [[5, 14], [1, 4], [9, 11], [2, 15], [2, 5], [9, 7], [8, 1], [6, 4]])