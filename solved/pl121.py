class Solution:
    def maxProfit(self, prices) -> int:
        
        DP = {}
        BUY = 0
        SELL = 1
        DP[(-1, BUY)] = float('inf')
        DP[(-1, SELL)] = 0
        
        for day, p in enumerate(prices):
            DP[(day, BUY)] = min(DP[(day-1, BUY)], p)
            DP[(day, SELL)] = max(DP[(day-1, SELL)], p - DP[(day-1, BUY)])
        
        return DP[(len(prices) - 1, SELL)]    
    
s = Solution()
s.maxProfit([7,1,5,3,6,4])