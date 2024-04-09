class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7
        # [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94
        # 0 - 4 6
        # 1 - 8 6
        # 2 - 7 9 
        # 3 - 4 8
        # 4 - 3 9 0
        # 5 - x
        # 6 - 1 7 0
        # 7 - 2 6
        # 8 - 1 3
        # 9 - 2 4 

        
        
        # 2 2 2 2 3 0 3 2 2 2
        # 6 5 4 5 6 0 6 5 4 5 
        print(6+5+4+5+6+0+6+5+4+5 )
        print(2 ** 3130 % mod)
        pass
    
s = Solution()
s.knightDialer(10)