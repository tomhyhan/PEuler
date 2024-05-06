from functools import reduce
from collections import deque
class Solution:
    def minScoreTriangulation(self, values) -> int:
        # self.helper(values)
        print(self.even_area_score([1,2,1,3,1,4], 0))
        print(self.even_area_score([1,2,1,3,1,4], 1))
        
    def even_area_score(self, values, start_idx):
        # even -> add first
        # odd -> start with first, add last
        next_pts = []
        area = 0
        n_outer = len(values) // 2
        # 0 2 4
        # 1 3 5 
        for i in range(start_idx, n_outer+start_idx):
            i = i * 2
            area += reduce(lambda x, y: x * y, [values[(i + j) % len(values)]  for j in range(3)])
            next_pts.append(values[i])
        
        return area, next_pts
    
    def odd_area_score(self, values, start_idx):

        pass
    def helper(self, values):
        if len(values) - 2 == 0:
            return 0
        
        odd_trig = self.area_score(values)
        even_trig = self.area_score(values) 
    
    
s = Solution()
# s.minScoreTriangulation([1,2,3])
# s.minScoreTriangulation([3,7,4,5])
s.minScoreTriangulation([1,3,1,4,1,5])