
class Solution:
    def maxProfit(self, prices) -> int:
        memo = {}
        max_profit = self.helper(prices, 0, 4, True, memo)
        print(max_profit)
        
    def helper(self, prices, i, n_transactions, buy, memo):
        key = (i, n_transactions, buy)
        if i == len(prices) or n_transactions == 0:
            return 0
        elif key in memo:
            return memo[key]
        
        price = -prices[i] if buy else prices[i]
        transaction = self.helper(prices, i+1, n_transactions -1, not buy, memo) + price
        no_transaction = self.helper(prices, i+1, n_transactions, buy, memo)
        
        max_profit = max(transaction, no_transaction)
        memo[key] = max_profit
        return max_profit

    
s = Solution()
# s.maxProfit([3,3,5,0,0,3,1,4])
s.maxProfit([0,2,0,4])