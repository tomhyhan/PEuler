class Solution:
    def countSubstrings(self, s: str) -> int:
        DP = {}
        # aaaa
        # aaa aaa
        # aa aa
        # a a
        # palins = self.helper(s, len(s), DP)
        # print(palins + len(s)) 
        self.helper(0, 0, s, DP)
        
    def helper(self, row, col, s, DP):
        if not s:
            return
        elif s in DP:
            return DP[s]
            
        left_s, right_s = s[:-1], s[1:]
        
        DP[(row,col)] = self.helper(left_s, row+1, col) + self.helper(right_s,row+1, col+1)

        return DP[(row,col)]

    def is_palin(self, s):
        # aaa 3 // 2 = 1
        # aaaaa 5 // 2 = 2 
        len_s = len(s)
        left, right = (len_s // 2 - 1, len_s // 2) if len_s % 2 == 0 else (len_s // 2, len_s // 2)
        while left >=0 and right < len_s:
            if s[left] != s[right]:
                return False
            left -= 1
            right += 1
            
        return True
    
        # for window in range(2, len(s)):
        #     for left in range(len(s) - window):
        #         subs = s[left: left + window]
        #         if self.is_palin(subs):
        #             pass
s = Solution()
s.countSubstrings("aaaa")