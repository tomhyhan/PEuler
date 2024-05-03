class Solution:
    def minScoreTriangulation(self, values) -> int:
        self.helper(values)
        
    def helper(self, values):
        if len(values) < 3:
            return 0
        
        odd_trig = None
        pass
    
    
s = Solution()
# s.minScoreTriangulation([1,2,3])
# s.minScoreTriangulation([3,7,4,5])
s.minScoreTriangulation([1,3,1,4,1,5])