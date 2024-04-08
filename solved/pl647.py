class Solution:
    def countSubstrings(self, s: str) -> int:
        len_s = len(s)
        DP = [[False for _ in range(len_s)] for _ in range(len_s)]

        total = 0
        for i in range(len_s):
            DP[0][i] = True
            total += 1
        
        for i in range(len_s - 1):
            if s[i] == s[i + 1]:
                DP[1][i] = True
                total += 1
                
        for layer in range(2, len_s):
            for i in range(len_s - layer):
                if s[i] == s[i + layer] and DP[layer-2][i + 1]:
                    DP[layer][i] = True
                    total += 1
        # print(DP)
        # print(total)
        return total
s = Solution()
s.countSubstrings("aaa")