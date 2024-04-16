class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen: int, secondLen: int) -> int:
        left = [0 for _ in nums]
        right = [0 for _ in nums]

        short, long = (firstLen, secondLen) if firstLen < secondLen else (secondLen, firstLen) 
        n = len(nums)
        max_l, max_r = 0, 0
        for i in range(n - short + 1):
            end_i = n - i 
            max_l = max(max_l, sum(nums[i:i+short]))
            max_r = max(max_r, sum(nums[end_i-short:end_i])) 
            left[i] = max_l
            right[end_i-1] = max_r
        max_t = 0 

        for i in range(n - long + 1):
            array_sum = sum(nums[i:i+long])
            left_sum, right_sum = 0, 0
            if i - short >= 0:
                left_sum = left[i-short]
            if i+long+short < n:
                right_sum = right[i+long+short]
            max_t = max(max_t, array_sum + left_sum, array_sum + right_sum)

        return max_t
class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen: int, secondLen: int) -> int:

        nums = list(accumulate(nums, initial = 0))
        mx1 = mx2 = mx3 = 0
        
        for sm0,sm1,sm2,sm3 in zip(nums, 
                                   nums[firstLen:],
                                   nums[secondLen:],
                                   nums[firstLen+secondLen:]):

            mx1 = max(mx1, sm1 - sm0)
            mx2 = max(mx2, sm2 - sm0)
            mx3 = max(mx3, max(mx1 + sm3-sm1, mx2 + sm3-sm2))
            
        return mx3

s = Solution()
s.maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4], 1, 2)