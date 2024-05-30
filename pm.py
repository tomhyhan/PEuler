def solution(arr):
    
    INF = int(1e9)
    min_dp = [[INF for _ in range(len(arr)//2 + 1)] for _ in range(len(arr) //2 +1)]
    max_dp = [[-INF for _ in range(len(arr)//2 + 1)] for _ in range(len(arr) //2 +1)]
    
    for i in range(len(arr) //2 + 1):
        min_dp[i][i] = int(arr[i * 2])
        max_dp[i][i] = int(arr[i * 2])
    
    for c in range(1,len(max_dp)):
        for i in range(len(max_dp) - c):
            j = i + c
            for k in range(i,j):
                if arr[k*2 + 1] == "+":
                    max_dp[i][j] = max(max_dp[i][j],max_dp[i][k] + max_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j],min_dp[i][k] + min_dp[k+1][j])
                elif arr[k*2 +1] =='-':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j])
                print(c,i,j,k)
                print(i,k)
                print(k+1, j)
    return max_dp[0][-1]


def solution(arr):
    n_nums = (len(arr) // 2) + 1
    MIN_DP = [[float('inf') for _ in range(n_nums)] for _ in range(n_nums)]
    MAX_DP = [[float('-inf') for _ in range(n_nums)] for _ in range(n_nums)]

    for i in range(n_nums):
        MIN_DP[i][i] = int(arr[i*2])
        MAX_DP[i][i] = int(arr[i*2])


    for d in range(1, n_nums):
        for i in range(n_nums-d):
            j = i + d
            for k in range(i,j):
                signi = k*2 + 1
                if arr[signi] == '+':
                    MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k] + MAX_DP[k+1][j])
                    MIN_DP[i][j] = min(MIN_DP[i][j], MIN_DP[i][k] + MIN_DP[k+1][j])
                else:
                    MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k] - MIN_DP[k+1][j])
                    MIN_DP[i][j] = min(MIN_DP[i][j], MIN_DP[i][k] - MAX_DP[k+1][j])
                    

    return MAX_DP[0][-1]

solution(["1", "-", "3", "+", "5", "-", "8"])