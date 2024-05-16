class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        memo = {}
        max_profit = self.helper(0, fee, True, prices, memo)
        return max_profit
    
    def helper(self, i, fee, buy, prices, memo):
        key = (i, buy)
        if i >= len(prices):
            return 0
        elif key in memo:
            return memo[key]
        
        price = -prices[i] if buy else  prices[i] - fee
        transaction = self.helper(i+1, fee, not buy, prices, memo) + price
        no_transaction = self.helper(i+1, fee, buy, prices, memo) 
        
        max_profit = max(transaction, no_transaction)
        memo[key] = max_profit
        return max_profit

class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        DP = {}
        
        BUY = 0
        SELL = 1
        
        DP[(-1, BUY)] = float("inf")
        DP[(-1, SELL)] = 0
        
        for day, p in enumerate(prices):
            DP[(day, BUY)] = min(DP[(day-1, BUY)], p - DP[(day-1, SELL)] )
            DP[(day, SELL)] = max(DP[(day-1, SELL)], p - DP[(day-1, BUY)] - fee)
            
        print(DP[(day, SELL)])
        return DP[(day, SELL)]
        
    
s = Solution()
s.maxProfit([1,3,2,8,4,9], 2)