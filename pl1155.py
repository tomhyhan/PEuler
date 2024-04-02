import numpy as np
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        conv = [1 for _ in range(k)]
        filter = [1 for _ in range(k)]
        mod = 10 ** 9 + 7
        for _ in range(n-1):
            conv = np.convolve(conv, filter) % mod
            # print(conv)
        # print(conv[500+30 - 2: 500+30 + 2])
        print(conv)
        print(conv[target-n] )
        return 0

s = Solution()
# s.numRollsToTarget(3,6,6)
s.numRollsToTarget(1,6,3)
s.numRollsToTarget(5,30,100)