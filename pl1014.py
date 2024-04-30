class Solution:
    def maxScoreSightseeingPair(self, values) -> int:
        # values[i] + values[j] + i - j
        # i < j
        max_pair = (values[0], 0)
        max_diff = 0
        for j in range(1, len(values)):
            max_val, i = max_pair
            current_val = values[j]

            diff = max_val + current_val + i - j
            
            if max_diff < diff:
                max_diff = diff
            
            # print("max_val", max_val, i)
            if current_val > max_val - (j - i):
                max_pair = (current_val, j)
        # print(max_pair)
        # print(max_diff)          
        return max_diff  
    
s = Solution()
# s.maxScoreSightseeingPair([8,1,5,2,6])
# s.maxScoreSightseeingPair([1,2])
# # 14
# s.maxScoreSightseeingPair([7,2,6,6,9,4,3])
# 13
s.maxScoreSightseeingPair([6,3,7,4,7,6,6,4,9])