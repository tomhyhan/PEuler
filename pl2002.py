# solv 1 works, but slowish barely not passing
# from itertools import product
# class Solution:
#     def maxProduct(self, s: str) -> int:
#         memo = {}
#         max_mul = 1

#         ps = list(product([0,1], repeat=len(s)))
#         for p in ps[1: -1]:
#             palin1 = [s[i] for i in range(len(s)) if p[i] == 1]
#             palin2 = [s[i] for i in range(len(s)) if p[i] == 0]
        
#             p1 = len(palin1) if self.is_palin(palin1) else self.max_sub_palin_length(palin1, memo)
#             p2 = len(palin2) if self.is_palin(palin2) else  self.max_sub_palin_length(palin2, memo)
#             max_mul = max(max_mul, p1 * p2)

#         # print(max_mul)
#         return max_mul
        
        
#     def max_sub_palin_length(self, line, memo):
#         # print(line)
#         key = tuple(line)
#         if len(line) == 1:
#             return 1
#         elif key in memo:
#             return memo[key]
            
#         max_len = 1
#         ps = list(product([0,1], repeat=len(line)))
#         for p in ps[1: -1]:
#             palin1 = [line[i] for i in range(len(line)) if p[i] == 1]
#             palin2 = [line[i] for i in range(len(line)) if p[i] == 0]
            
#             max_p1 = len(palin1) if self.is_palin(palin1) else self.max_sub_palin_length(palin1, memo)
#             max_p2 = len(palin2) if self.is_palin(palin2) else self.max_sub_palin_length(palin2, memo)
#             max_len = max(max_len, max_p1, max_p2)

#         memo[key] = max_len
#         return max_len    

#     def is_palin(self, line):
#         return line == line[::-1]

# sov2 
from itertools import product
class Solution:
    def maxProduct(self, s: str) -> int:
        memo = {}
        max_mul = 1

        ps = list(product(['0','1'], repeat=len(s)))
        for p in ps:
            sub_s = [s[i] for i in range(len(s)) if p[i] == '1']
            if self.is_palin(sub_s):
                key = int(''.join(p), 2)
                memo[key] = len(sub_s)
                
        for mask1, n_p1 in memo.items():
            for mask2, n_p2 in memo.items():
                if mask1 & mask2 == 0:
                    max_mul = max(max_mul, n_p1 * n_p2)

        return max_mul

    def is_palin(self, line):
        return line == line[::-1]
    
s = Solution()
s.maxProduct("leetcodecom")
s.maxProduct("accbcaxxcxx")
s.maxProduct("jgvthvrj")
s.maxProduct("spgttgpsvqv")
s.maxProduct("abba")