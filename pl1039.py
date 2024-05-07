class Solution:
    def minScoreTriangulation(self, values) -> int:
        score = self.helper(values)
        print(score)
        return score
    
    def helper(self, values):
        n = len(values)
        if n - 2 <= 0:
            return 0
        min_n = min(values[1:-1])
        k = values[1:-1].index(min_n) + 1

        area = values[0] * values[-1] * values[k]
        left = values[0:k+1] 
        right = values[k:n-1]
        # area, inner_values = self.get_score(values, k)

        # min_score = min(min_score, area + self.helper(inner_values))
        print(k)
        print(area)
        print(values)
        print(left, right)
        return area + self.helper(left) + self.helper(right)
    
    def get_score(self, values):
        # 1 3 1 5 1 6
        # 1 3 1 5 1 6 1
        n = len(values)
        n_outer_tris = n // 2
        start = 0
        inner_tris = deque([values[start]])
        area = 0 
        for i in range(n_outer_tris):
            idx = i * 2
            s, m, l = idx, (idx + 1) % n, (idx + 2) % n
            if l != start:
                inner_tris.append(values[l])
            area += values[s] * values[m] * values[l]         
        return area, inner_tris
    
s = Solution()
# s.minScoreTriangulation([1,2,3])
# s.minScoreTriangulation([3,7,4,5])
s.minScoreTriangulation([1,3,1,4,1,5])
# s.minScoreTriangulation([2,2,2,2,1])