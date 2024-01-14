import numpy as np

def solution():
    dp = np.array([0, 1])
    last = dp[dp.size-1]
    i = 2
    while last < 4000000:
        dp = np.append(dp, dp[i-1] + dp[i-2])
        last = dp[-1]
        i+=1
    print(dp[dp%2==0].sum())

solution()