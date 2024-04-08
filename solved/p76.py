def solution():
    n = 100
    DP = [0] * (n + 1)
    DP[0] = 1

    for i in range(1,n):
        for j in range(n + 1):
            if j >= i:
                DP[j] += DP[j-i]
    print(i, DP)
    print(i, DP[-1])

solution()