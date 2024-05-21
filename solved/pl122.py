class Solution:
    def maxProfit(self, prices) -> int:
        DP = {}
        
        MIN_BUY_PRICE = 0
        MAX_SOLD_PRICE = 1
        
        # MIN_BUY_PRICE is relative minimum buy price with respect to MAX_SOLD_PRICE
        DP[(-1, MIN_BUY_PRICE)] = float('-inf')
        # MAX_SOLD_PRICE is accumulated selling price at each hike
        DP[(-1, MAX_SOLD_PRICE)] = 0
        
        for day, price in enumerate(prices):
            DP[(day, MIN_BUY_PRICE)] = max(DP[(day-1, MIN_BUY_PRICE)], DP[(day-1, MAX_SOLD_PRICE)] - price)
            DP[(day, MAX_SOLD_PRICE)] = max(DP[(day-1, MAX_SOLD_PRICE)], price + DP[(day-1, MIN_BUY_PRICE)])

        print(DP)
    
s = Solution()
s.maxProfit([7,1,5,3,6,4])
s.maxProfit([0,1,5,2,6])