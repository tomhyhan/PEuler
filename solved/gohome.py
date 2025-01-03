DIV = 1_000_000_007
# try 1
def solution(m, n, puddles):
    memo = {}
    return helper(m, n, puddles, memo)

def helper(m, n, puddles, memo):
    if (m,n) in memo:
        return memo[(m,n)]
    if [m, n] in puddles or m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    memo[(m,n)] = (helper(m-1, n, puddles, memo) +  helper(m, n-1, puddles, memo)) % DIV 
    return memo[(m,n)]

def solution(m, n, puddles):
    DP = [[0 for _ in range(m+1)] for _ in range(n+1)]
    DP[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if (i,j) == (1,1):
                continue
            if [j,i] in puddles:
                DP[i][j] = 0
                continue    
            DP[i][j] = (DP[i-1][j] + DP[i][j-1]) % DIV 
    
    return DP[-1][-1]

print(solution(4, 3, [[2, 2]]))