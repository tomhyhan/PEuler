class Solution:
    def integerBreak(self, n: int) -> int:
        DP = [1 for _ in range(n+1)]
        DP[2] = 2
        DP[3] = 3

        for i in range(4, n+1):
            DP[i] = max(DP[i-2] * 2, DP[i-3] * 3)

        return DP[n]
    
    # 0 1 2 3 4 5 6   
    
    # 1 1 2 3 6 9
    
s = Solution()
# s.integerBreak(2)
s.integerBreak(7)
# s.integerBreak(6)