class Solution:
    def maxProfit(self, prices) -> int:
        
        cool_down, sell, hold = 0, 0, -float('inf')
        
        for stock_price_of_Day_i in prices:
            
            prev_cool_down, prev_sell, prev_hold = cool_down, sell, hold
            print(prev_cool_down, prev_sell, prev_hold)
            cool_down = max(prev_cool_down, prev_sell)

            sell = prev_hold + stock_price_of_Day_i
            
            hold = max(prev_hold, prev_cool_down - stock_price_of_Day_i)
        print(cool_down, sell, hold)
    
s = Solution()
s.maxProfit([1,2,3,0,2])