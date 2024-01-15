import numpy as np

# def solution():

#     even = 0
#     def helper(first, second):
#         nonlocal even
#         if first + second > 4000000:
#             return 
#         print(first + second)
#         even += first + second if (first + second) % 2 == 0 else 0
#         helper(second, first + second)

#     helper(0,1)
#     print(even)

# dp
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