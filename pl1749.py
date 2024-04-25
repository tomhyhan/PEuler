class Solution:
    def maxAbsoluteSum(self, nums) -> int:

        current_min = 0
        current_max = 0
        min_so_far = 0
        max_so_far = 0

        for num in nums:
            current_min = min(current_min + num, 0)
            current_max = max(current_max + num, 0)
            min_so_far = min(min_so_far, current_min)
            max_so_far = max(max_so_far, current_max)

        return abs(min_so_far) if abs(min_so_far) > abs(max_so_far) else abs(max_so_far)
        
s = Solution()

# s.maxAbsoluteSum([1,-3,2,3,-4])
s.maxAbsoluteSum([2,-5,1,-4,3,-2])