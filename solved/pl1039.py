class Solution:
    def minScoreTriangulation(self, values) -> int:
        memo = {}
        min_area = self.helper(0, len(values) - 1, values, memo)
        # print("min_area", min_area)
        return min_area
    
    def helper(self, left, right, values, memo):
        key = (left, right)
        if right-left ==  + 1:
            return 0
        elif key in memo:
            return memo[key]
         
        min_area = float('inf')
        for mid in range(left+1, right):
            current_area = values[left] * values[right] * values[mid]
            min_area = min(min_area, current_area + self.helper(left, mid, values, memo) + self.helper(mid, right, values, memo))

        memo[key] = min_area
        return min_area
    
    def get_score(self, values):
        pass
    
s = Solution()
s.minScoreTriangulation([1,2,3])
s.minScoreTriangulation([3,7,4,5])
s.minScoreTriangulation([1,3,1,4,1,5])
s.minScoreTriangulation([2,2,2,2,1])