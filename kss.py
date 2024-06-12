from collections import defaultdict

"""
    DP = [0,0] + [0, sales[i]] for i in sales
    
    
    

"""
# def solution(sales, links):
#     graph = defaultdict(list)
    
#     for lead, emp in links:
#         graph[lead].append(emp) 
#     print(graph)

from collections import defaultdict

def init(links) :
    edge_dict = defaultdict(list)
    
    for a, b in links :
        edge_dict[a].append(b)
        
    return edge_dict

def dfs(node, edge_dict, dp) :
    if not edge_dict[node] :
        return
    
    cnt, zero_cnt, min_val, min_diff = 0, 0, 0, float('inf')
    for leaf in edge_dict[node] :
        dfs(leaf, edge_dict, dp)
        min_val += min(dp[leaf])
        cnt += 1
        if dp[leaf][0] < dp[leaf][1] :
            zero_cnt += 1
            min_diff = min(min_diff, dp[leaf][1] - dp[leaf][0])
    print(dp[node][1], min_val, min_diff, dp[node], zero_cnt, cnt)
    dp[node][1] += min_val
    dp[node][0] += min_val + min_diff if cnt == zero_cnt else min_val
    print(dp[node])
    print("-----------------")

def solution(sales, links):
    dp = [[0,0]] + [[0, sale] for sale in sales]
    
    edge_dict = init(links)
    dfs(1, edge_dict, dp)
    return min(dp[1])


# solution(
#     [14,17,15,18,19,14,13,16,28,17],
#     [[10,8],[1,9],[9,7],[5,4],[1,5],[5,10],[10,6],[1,3],[10,2]]
# )
# solution([5,6,5,3,4],[[2,3], [1,4], [2,5], [1,2]])
# solution([5, 6, 5, 1, 4], [[2,3], [1,4], [2,5], [1,2]])
solution([10, 10, 1, 1], [[3,2], [4,3], [1,4]])