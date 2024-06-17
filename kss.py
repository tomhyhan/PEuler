from collections import defaultdict

def dfs(node, DP, graph, sales):
    if not graph[node]:
        return
    
    sum_child = 0
    min_diff = float("inf")
    include_leader = False
    for nnode in graph[node]:
        dfs(nnode, DP, graph, sales)
        sum_child += min(DP[nnode])
        min_diff = min(min_diff, DP[nnode][1] - DP[nnode][0])
        if DP[nnode][0] > DP[nnode][1]:
            include_leader = True
            
    DP[node][1] += sum_child
    DP[node][0] = sum_child if include_leader else sum_child + min_diff
    
def solution(sales, links):
    graph = defaultdict(list)

    for lead, emp in links:
        graph[lead].append(emp) 

    DP =[[0,0]] + [[0,sales[i]] for i in range(len(sales))]
    dfs(1, DP, graph, sales)
    return min(DP[1])


solution(
    [14,17,15,18,19,14,13,16,28,17],
    [[10,8],[1,9],[9,7],[5,4],[1,5],[5,10],[10,6],[1,3],[10,2]]
)
# solution([5,6,5,3,4],[[2,3], [1,4], [2,5], [1,2]])
# solution([5, 6, 5, 1, 4], [[2,3], [1,4], [2,5], [1,2]])
# solution([10, 10, 1, 1], [[3,2], [4,3], [1,4]])