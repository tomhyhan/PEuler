# from collections import defaultdict
# try 1
# def solution(n, lighthouse):
#     graph = defaultdict(list)
    
#     for s, e in lighthouse:
#         graph[s].append(e)
#         graph[e].append(s)

#     ordered_graph = sorted(graph.items(), key=lambda x: -len(x[1])) 
#     print(ordered_graph)
#     covered = set()
#     lighted = 0
#     for node, others in ordered_graph:
#         node_list = set([node]) | set(others)
#         do_light = node_list - covered 
#         if do_light:
#             print(node_list)
#             print(do_light)
#             lighted += 1
#             covered |= node_list
#     # print(lighted) 
#     return lighted

import sys
from collections import defaultdict

sys.setrecursionlimit(1e6)

def solution(n, lighthouse):
    graph = defaultdict(list)
    
    for s, e in lighthouse:
        graph[s].append(e)
        graph[e].append(s)

    lights = set()
    
    n_lights = dfs(1, 1, graph, lights)
    return n_lights
    
def dfs(node, parent, graph, lights):
    n_lights = 0
    for child in graph[node]:
        if child == parent:
            continue
        n_lights += dfs(child, node, graph, lights)
        
        if node not in lights and child not in lights:
            lights.add(node)
            n_lights += 1
    return n_lights

solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]])
solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]])