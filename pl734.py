class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        buy = float('-inf')
        sell = 0

        for price in prices:
            # 0 - 4 = -1
            # 0
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)
            print(price, "buy", buy, "sell", sell )
        return sell
    
    
s = Solution()
s.maxProfit([1,4,5,8,4,9], 2)