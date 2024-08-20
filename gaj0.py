from collections import defaultdict
import sys
sys.setrecursionlimit(5000)

def helper(node, a, graph, visited):
    visited.add(node)
    
    curr_sum = a[node]
    curr_w = 0
    for nnode in graph[node]:
        if nnode in visited:
            continue
        next_sum, next_w = helper(nnode, a, graph, visited)
        curr_sum += next_sum 
        curr_w += next_w
        
    return curr_sum, abs(curr_sum) + curr_w

def solution(a, edges):
    if sum(a) != 0:
        return -1
    
    graph = defaultdict(list)
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
    
    s, w = helper(0, a, graph, set())
    # print(w)
    return w
    
    print(s, w)
solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])