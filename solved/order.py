from collections import defaultdict

def solution(n, results):
    MAX = float("inf")
    DP = [[MAX for _ in range(n + 1)] for _ in range(n + 1)]
    
    for i in range(1, n+1):
        DP[i][i] = 0
    
    for w, l in results:
        DP[w][l] = 1
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    continue
                DP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j])
                
    cnt = 0
    for i in range(1, n + 1):
        is_order = True
        for j in range(1, n +1):
            if i == j:
                continue
            if DP[i][j] == MAX and DP[j][i] == MAX:
                is_order = False
                break
        if is_order:
            cnt += 1

    return cnt
    
solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])