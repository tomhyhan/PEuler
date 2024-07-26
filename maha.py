from collections import defaultdict
def solution(sales, links):
    graph = defaultdict(list)
    sales = [[0,0]]+ [[0,s] for s in sales]
    print(sales)
    for p, c in links:
        graph[p].append(c)
        
    helper(1, graph, sales)
    return min(sales[1])
    
def helper(lead, graph, sales):
    if not graph[lead]:
        return
    
    min_sales = 0
    min_leader_mem_diff = float('inf')
    for member in graph[lead]:
        helper(member, graph, sales)
        min_sales += min(sales[member])
        min_leader_mem_diff = min(min_leader_mem_diff, sales[member][1] - sales[member][0])

    sales[lead][1] += min_sales
    sales[lead][0] = min_sales if min_leader_mem_diff < 0 else min_sales + min_leader_mem_diff
    
    
    
solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]])