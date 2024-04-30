class Solution:
    def maxAlternatingSum(self, nums) -> int:
        memo = {}
        max_num = self.helper(0, nums, True, memo)
        print(max_num)
        return max_num
        
    def helper(self, idx, nums, sign, memo):
        key = (idx, sign)
        if idx == len(nums):
            return 0
        elif key in memo:
            return memo[key]
            
        curret_num = nums[idx] if sign else -nums[idx]
        
        with_current = curret_num + self.helper(idx + 1, nums, not sign, memo)
        
        without_current = self.helper(idx + 1, nums, sign, memo)
        
        print(idx, with_current, without_current, sign)

        max_num = max(with_current, without_current)
        
        memo[key] = max_num
        return max_num
        
s = Solution()
s.maxAlternatingSum([4,2,5,3])
# s.maxAlternatingSum([6,2,1,2,4,5])