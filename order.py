from collections import defaultdict

def solution(n, results):
    graph = defaultdict(list)
    for w, l in results:
        graph[w].append(l)

    print(graph)
    # [0,w,0,0,0]
    # [0,0,w,w,w]
    # [0,l,0,0,0]
    # [0,l,0,0,0]
    # [0,l,0,0,0]

solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])