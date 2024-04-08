import numpy as np
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        conv = [1 for _ in range(k)]
        mod = 10 ** 9 + 7
        for _ in range(n-1):
            new_conv = []
            for i in range(1,len(conv)+k):
                left = max(0, i-k)
                right = min(len(conv), i)
                new_conv.append(sum(conv[left:right]) % mod)
            conv = new_conv
        return conv[target-n]
    
s = Solution()
# s.numRollsToTarget(3,6,6)
s.numRollsToTarget(2,6,3)
# s.numRollsToTarget(30,30,500)