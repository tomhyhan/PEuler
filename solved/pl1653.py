class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletions = [0] * len(s)
        
        As = 0
        Bs = 0
        for c in s:
            if c == 'a':
                As += 1
            else:
                Bs += 1
                
        for i, c in enumerate(s):
            if c == 'a':
                As -= 1
            deletions[i] += As
        
        for i, c in enumerate(reversed(s)):
            i_rev = len(s) - i - 1
            if c == 'b':
                Bs -= 1
            deletions[i_rev] += Bs

        return min(deletions)                
    
s = Solution()
# s.minimumDeletions("aababbab")
s.minimumDeletions("bbaab")