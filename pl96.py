class Solution:
    def numTrees(self, n: int) -> int:
        DP = {}
        DP[1] = 1
        DP[2] = 2
        num = self.helper(n, DP)
        print(num)
        return num
    
    def helper(self, n, DP):
        if n == 0:
            return 1
        elif n in DP:
            return DP[n]

        num = 0
        for left in range(n):
            # 0 2, 1 1, 2 0
            right = n - left - 1
            num += self.helper(left, DP) * self.helper(right, DP)
    
        DP[n] = num
        return num
        
class Solution:
    def numTrees(self, n: int) -> int:
        DP = [0] * (n + 1)
        DP[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                DP[i] += DP[j] * DP[i-j-1]
        return DP[n]

s = Solution()
s.numTrees(3)