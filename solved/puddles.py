def solution(m, n, puddles):
    DP = [[0 for _ in range(m)] for _ in range(n)]
    
    for row in range(n):
        if [0+1,row+1] in puddles:
            break
        DP[row][0] = 1
        
    for col in range(m):
        if [col+1,0+1] in puddles:
            break
        DP[0][col] = 1
    
    for row in range(1, n):
        for col in range(1,m):
            coord = [col+1, row+1]
            if coord in puddles:
                continue
            DP[row][col] =  DP[row-1][col] + DP[row][col-1]
    # print(DP)
    return DP[-1][-1]

def solution(m, n, puddles):
    memo = {}
    ways = helper(m,n,puddles,memo)
    return ways

def helper(m,n,puddles,memo):
    key = (m,n)
    if m == 1 and n == 1:
        return 1
    elif key in memo:
        return memo[key]
    
    if m == 0 or n == 0:
        return 0
    
    if [m,n] in puddles:
        return 0
    
    ways = helper(m,n-1,puddles,memo) + helper(m-1,n,puddles,memo)
    memo[key] = ways
    return ways

solution(4, 3, [[2, 2]])