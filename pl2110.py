class Solution:
    def getDescentPeriods(self, prices) -> int:
        dp = [0] * len(prices)
        dp[0] = 1
        prev_p = prices[0]
        for i in range(1, len(prices)):
            current_p = prices[i]
            if prev_p - current_p == 1:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 1
            prev_p = current_p
        return sum(dp) 
s = Solution()
s.getDescentPeriods([3,2,1,4])
    