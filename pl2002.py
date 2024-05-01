from itertools import product
import numpy as np
class Solution:
    def maxProduct(self, s: str) -> int:
        max_mul = 1
        for p in product([0,1], repeat=len(s)):
            if all(p) or all([e == 0 for e in p]):
                continue
            palin1 = [s[i] for i in range(len(s)) if p[i] == 1]
            palin2 = [s[i] for i in range(len(s)) if p[i] == 0]
        
            if self.is_palin(palin1) and self.is_palin(palin2):
                max_mul = max(max_mul, len(palin1) * len(palin2))

        print(max_mul)
        return max_mul

    def sub_palin(self, line):
        for i in range(line):
            pass
        pass
    
    def is_palin(self, line):
        left = 0
        right = len(line) - 1
        
        while left < right:
            if line[left] != line[right]:
                return False
            left += 1
            right -= 1
            
        return True
    
s = Solution()
s.maxProduct("leetcodecomc")