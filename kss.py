from collections import defaultdict

def solution(sales, links):
    graph = defaultdict(list)
    
    for lead, emp in links:
        graph[lead].append(emp) 
    print(graph)



solution(
    [14,17,15,18,19,14,13,16,28,17],
    [[10,8],[1,9],[9,7],[5,4],[1,5],[5,10],[10,6],[1,3],[10,2]]
)
# solution([5,6,5,3,4],[[2,3], [1,4], [2,5], [1,2]])