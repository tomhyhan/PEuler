class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        buy = float('-inf')
        sell = 0

        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)
            print(price, buy, sell)
        return sell
    
    
s = Solution()
s.maxProfit([1,3,2,8,4,9], 2)