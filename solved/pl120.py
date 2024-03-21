class Solution:
    def minimumTotal(self, triangle):
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i-1][0] 
            triangle[i][i] += triangle[i-1][i - 1] 

        for row in range(2, len(triangle)):
            for col in range(1, row):
                triangle[row][col] += min(triangle[row-1][col], triangle[row-1][col-1])

        return min(triangle[len(triangle) - 1])

s = Solution()
s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])