class Solution:
    def maxProfit(self, prices) -> int:
        DP = {}
        
        BUY1 = 0
        SELL1 = 1
        
        DP[(-1, BUY1)] = float("-inf")
        DP[(-1, SELL1)] = 0
        
        for day, p in enumerate(prices):
            DP[(day, BUY1)] = max(DP[(day-1, BUY1)], DP[(day-1, SELL1) - p])     
            DP[(day, SELL1)] = max(DP[(day-1 , SELL1)], DP[(day-1, BUY1) + p])

            DP[(day, BUY1)] = max(DP[(day-1, BUY1)], DP[(day-1, SELL1) - p])     
            DP[(day, SELL1)] = max(DP[(day-1 , SELL1)], DP[(day-1, BUY1) + p])

from collections import defaultdict
import math

class Solution:
    def maxProfit(self, prices) -> int:
        
        HOLD_STOCK, KEEP_CASH = 0, 1
        
        # dictionary
        # key: state, kth-transaction
        # value: corresponding profit
        dp = defaultdict(int)        
        
        # No free lunch, impoosible to have stock before first trading day
        dp[(HOLD_STOCK, 0)] = -math.inf
        dp[(HOLD_STOCK, 1)] = -math.inf
        dp[(HOLD_STOCK, 2)] = -math.inf
        

        for stock_price in prices:
            # Either we had stock already, or we just buy in stock today ( add one more transaction)
            dp[HOLD_STOCK, 1] = max(dp[HOLD_STOCK, 1],  dp[KEEP_CASH, 0] - stock_price)
            
            ## For 1st transaction:
            # Either we kept cash already, or we just sell out stock today
            dp[KEEP_CASH, 1] = max(dp[KEEP_CASH, 1], dp[HOLD_STOCK, 1] + stock_price )
            
            # Either we had stock already, or we just buy in stock today ( add one more transaction)
            dp[HOLD_STOCK, 2] = max(dp[HOLD_STOCK, 2], dp[KEEP_CASH, 1] - stock_price)
            
            ## For 2nd transaction:
            # Either we kept cash already, or we just sell out stock today
            dp[KEEP_CASH, 2] = max(dp[KEEP_CASH, 2], dp[ HOLD_STOCK, 2] + stock_price)
            print(dp[HOLD_STOCK, 0], dp[KEEP_CASH, 0])
            print(dp[HOLD_STOCK, 1], dp[KEEP_CASH, 1])
            print(dp[HOLD_STOCK, 2], dp[KEEP_CASH, 2])
            print()
        # Maximal profit must be KEEP_CASH on last day
        # (This means we cash out and sell stocks finally)
        return dp[KEEP_CASH, 2]
    
s = Solution()
s.maxProfit([3,7,0,2])