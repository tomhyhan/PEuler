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
        # 
        # 
        pass
    
class Solution:
    def maxProfit(self, prices) -> int:
        
		# initialization
        cool_down, sell, hold = 0, 0, -float('inf')
        
        for stock_price_of_Day_i in prices:
            
            prev_cool_down, prev_sell, prev_hold = cool_down, sell, hold
            # Max profit of cooldown on Day i comes from either cool down of Day_i-1, or sell out of Day_i-1 and today Day_i is cooling day
            cool_down = max(prev_cool_down, prev_sell)
            
            # Max profit of sell on Day_i comes from hold of Day_i-1 and sell on Day_i
            sell = prev_hold + stock_price_of_Day_i
            
            # Max profit of hold on Day_i comes from either hold of Day_i-1, or cool down on Day_i-1 and buy on Day_i
            hold = max(prev_hold, prev_cool_down - stock_price_of_Day_i)
            print(cool_down, sell, hold)
            print()
        
        # The action of final trading day must be either sell or cool down
        return max(sell, cool_down)
    
s = Solution()
# s.maxProfit([1,2,3,0,2])
s.maxProfit([0,2,0,1,2])