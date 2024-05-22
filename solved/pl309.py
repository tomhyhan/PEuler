class Solution:
    def maxProfit(self, prices) -> int:
        memo = {}
        max_profit = self.helper(0, False, True, prices, memo)
        print(max_profit)
        return max_profit
    
    def helper(self, i, cooldown, buy, prices, memo):
        key = (i, cooldown, buy)
        if i >= len(prices):
            return 0
        elif key in memo:
            return memo[key]
         
        price = -prices[i] if buy else prices[i]
        next_cooldown = False if buy else True
        
        transaction = float("-inf") if cooldown else self.helper(i+1, next_cooldown, not buy, prices, memo) + price
        no_transaction = self.helper(i+1, False, buy, prices, memo)
        
        max_profit = max(transaction, no_transaction)
        memo[key] = max_profit 
        return max_profit


class Solution:
    def maxProfit(self, prices) -> int:

        pass
        
class Solution:
    def maxProfit(self, prices) -> int:
        DP = {}
        
        COOL_DOWN = 0
        SELL = 1
        BUY = 2
        
        DP[(-1, COOL_DOWN)] = 0 
        DP[(-1, SELL)] = 0 
        DP[(-1, BUY)] = float('-inf')
        
        for day, p in enumerate(prices):
            DP[(day, COOL_DOWN)] = max(DP[(day-1, COOL_DOWN)], DP[(day-1, SELL)])
            DP[(day, SELL)] = DP[(day-1, BUY)] + p
            DP[(day, BUY)] = max(DP[(day-1, BUY)], DP[(day-1, COOL_DOWN)] - p)
            
        return max(DP[(day, COOL_DOWN)], DP[(day, SELL)])
             
    
s = Solution()
# s.maxProfit([1,2,3,0,2])
print(s.maxProfit([1,4,0,2]))