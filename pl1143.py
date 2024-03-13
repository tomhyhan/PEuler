class Solution:
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     dp = [[0  for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

    #     for row in range(1, len(text1) + 1):
    #         for col in range(1, len(text2) + 1):
    #             if text1[row-1] == text2[col-1]:
    #                 dp[row][col] = dp[row-1][col-1] + 1
    #             else:
    #                 dp[row][col] += max(dp[row-1][col], dp[row][col-1])

    #     return dp[-1][-1]
    def helper(self, text1, text2, t1, t2):
        if t1 >= len(text1) or t2 >= len(text2):
            return 0

        if text1[t1-1] == text2[t2-1]:
            return 1 + self.helper(text1, text2, t1+1, t2+1)
        else:
            return max(self.helper(text1, text2, t1+1, t2), self.helper(text1, text2, t1, t2+1))

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = self.helper(text1, text2, 0, 0)    
        print(n)
        return 
    
    
s = Solution()

s.longestCommonSubsequence("bl", "yby")
s.longestCommonSubsequence("ace", "abcde")
s.longestCommonSubsequence("bsbininm", "jmjkbkjkv")
s.longestCommonSubsequence("aaa", "aaaa")