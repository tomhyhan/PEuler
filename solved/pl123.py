from collections import defaultdict
import math

class Solution:
    def maxProfit(self, prices) -> int:
        buy1 = -float('inf')
        buy2 = -float('inf')
        sell1 = 0
        sell2 = 0
        
        for price in prices:
            buy1 = max(buy1, 0 - price)
            sell1 = max(sell1, price + buy1)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, price + buy2)
        return sell2

s = Solution()
# s.maxProfit([3,3,5,0,0,3,1,4])
# s.maxProfit(prices = [1,2,3,4,5])
s.maxProfit([3,6,4,8])
