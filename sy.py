from collections import defaultdict, deque

class Disjoint:
    def __init__(self, verticies):
        self.parents = {v:v for v in verticies}
        self.rank = {v:0 for v in verticies}
    
    def find(self, node):
        if self.parents[node] != node:
            node = self.find(self.parents[node])
        return node
        
    def union(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)
        
        if self.rank[roota] > self.rank[rootb]:
            self.parents[rootb] = roota
        elif self.rank[roota] < self.rank[rootb]:
            self.parents[roota] = rootb 
        else:
            self.parents[rootb] = roota
            self.rank[roota] += 1

def solution(n, costs):
    costs = sorted(costs, key=lambda x: x[2])

    verticies = set()
    
    for s, e, _ in costs:
        verticies.add(s)
        verticies.add(e)
    print(costs)
    disjoint = Disjoint(verticies)
    total_cost = 0
    for s, e, c in costs:
        if disjoint.find(s) != disjoint.find(e):
            disjoint.union(s,e)
            total_cost += c
            # print(disjoint.parents)
            
    return total_cost

import heapq as hq

def solution(n, costs):
    answer = 0
    from_to = list(list() for _ in range(n))
    visited = [False] * n
    priority = []

    for a, b, cost in costs:
        from_to[a].append((b, cost))
        from_to[b].append((a, cost))
        
    print(from_to)
    
    hq.heappush(priority, (0, 0))
    while False in visited:
        cost, start = hq.heappop(priority)
        if visited[start]: continue

        visited[start] = True
        answer += cost
        for end, cost in from_to[start]:
            if visited[end] : continue
            else:
                hq.heappush(priority, (cost, end))

    return answer

# solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,8],[2,3,1]])
# solution(7, [[2, 3, 7], [3, 6, 13], [3, 5, 23], [5, 6, 25], [0, 1, 29], [1, 5, 34], [1, 2, 35], [4, 5, 53], [0, 4, 75]])
# solution(5,[[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]])
solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]])
# solution(5,[[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]])
# solution(5,[[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 3], [2, 3, 8], [3, 4, 1]])
# solution(6,[[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]])