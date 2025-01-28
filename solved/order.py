from collections import defaultdict

def solution(n, results):
    DP = [[float('inf') if r != c else 0 for c in range(n+1)] for r in range(n+1)]
    
    for w,l in results:
        DP[w][l] = 1
        

    for k in range(2, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    continue
                DP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j])

    cnt = 0
    for i in range(1, n+1):
        conn = True
        for j in range(1, n+1):
            if i == j: continue
            if DP[i][j] == float('inf') and DP[j][i] == float('inf'):
                conn = False
                break
        if conn:
            cnt += 1
    
    return cnt

# [0, inf, inf, inf, inf, inf]
# [inf, 0, 1, inf, inf, inf]
# [inf, inf, 0, inf, inf, 1]
# [inf, inf, 1, 0, inf, inf]
# [inf, inf, 1, 1, 0, inf]
# [inf, inf, inf, inf, inf, 0]

solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])