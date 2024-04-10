class Solution:
    def findLongestChain(self, pairs) -> int:
        pairs.sort(key=lambda x: x[1])
        memo = {}
        max_length = self.helper(0, pairs, memo, 1)
        return max_length
        
    def helper(self, i, pairs, memo, chains):
        if i >= len(pairs):
            return chains
        elif i in memo and memo[i] >= chains:
            return memo[i]

        max_length = chains
        current_pair = pairs[i]
        for j in range(i+1, len(pairs)):
            next_pair = pairs[j]
            if current_pair[1] < next_pair[0]:
                length = self.helper(j, pairs, memo, chains + 1)
                max_length = max(max_length, length)

        memo[i] = max_length
        return max_length
                
    
s = Solution()
# s.findLongestChain([[1,2],[2,3],[3,4]])
# s.findLongestChain([[1,2],[7,8],[4,5]])
s.findLongestChain([[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]])
s.findLongestChain([[9,10],[8,9],[-1,1],[6,9],[1,10],[3,8],[-2,4],[-7,-2],[9,10]])