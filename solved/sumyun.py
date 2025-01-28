class UnionFind:
    def __init__(self, nodes):
        self.parents = {node:node for node in nodes}

    def find(self, a):
        if self.parents[a] == a:
            return a
        return self.find(self.parents[a])
    
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return
        
        self.parents[pb] = pa

def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    nodes = set()
    for s, e, _ in costs:
        nodes.add(s)
        nodes.add(e)
    
    union_find = UnionFind(nodes)
    
    total_cost = 0
    for s, e, c in costs:
        if union_find.find(s) != union_find.find(e):
            union_find.union(s, e)
            total_cost += c
    # print(total_cost)
    return total_cost

# [[0, 1, 1], [1, 3, 1], [0, 2, 2], [1, 2, 5], [2, 3, 8]]

solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])