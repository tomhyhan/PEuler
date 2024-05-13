class Solution:
    def maxProfit(self, prices) -> int:
        buy = float("-inf")
        sell = 0
        
        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, price + buy)
            print(buy, sell)
        return sell
    
s = Solution()
# s.maxProfit([7,1,5,0,6,4])
s.maxProfit([0,6,1,3])