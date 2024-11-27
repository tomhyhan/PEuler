from collections import defaultdict

def cnt(g, node, visited):
    if node in visited:
        return 
    
    visited.add(node)

    for neigh in g[node]:
        if neigh in visited:
            continue
        cnt(g, neigh, visited)

def solution(n, wires):
    g = defaultdict(list)
    
    for s, e in wires:
        g[s].append(e)
        g[e].append(s)
        
    min_diff = float('inf')
    for s, e in wires:
        visited = set([e])
        cnt(g, s, visited)
        one_side = len(visited) - 1
        other_side = n - one_side
        min_diff = min(min_diff, abs(one_side - other_side))

    return min_diff

uf = []

def find(a):
    global uf
    if uf[a] < 0: return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    print(a,b )
    print(pa, pb)
    if pa == pb: return
    uf[pa] += uf[pb]
    uf[pb] = pa

def solution(n, wires):
    global uf
    answer = int(1e9)
    k = len(wires)
    for i in range(k):
        uf = [-1 for _ in range(n+1)]
        tmp = [wires[x] for x in range(k) if x != i]
        print(tmp)
        for a, b in tmp: 
            merge(a, b)
            print(uf )
        v = [x for x in uf[1:] if x < 0]
        answer = min(answer, abs(v[0]-v[1]))
        break
    return answer

# 4 7
# solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])
# solution(4, [[1,2],[2,3],[3,4]])
# 7 3
solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])