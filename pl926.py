class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        self.helper(0, s)
        
        
    def helper(idx, s):
        if idx == len(s) - 1:
            return 0
        
        c_s = s[idx]
        n_s = s[idx+1]

        if c_s == '0' and n_s == '1':
            # 01
            pass
        elif c_s == '1' and n_s == '0':
            # 10
            pass

        
s = Solution()
s.minFlipsMonoIncr("00110")