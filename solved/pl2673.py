class Solution:
    def minIncrements(self, n: int, cost) -> int:
        increments = 0 
        n_parent_nodes = n // 2
        
        for parent in reversed(range(1, n_parent_nodes + 1)):
            childOne = 2 * parent
            childTwo = 2 * parent + 1
            cost_balance = abs(cost[childOne-1] - cost[childTwo-1])
            increments += cost_balance
            max_cost = max(cost[childOne-1], cost[childTwo-1])
            cost[parent-1] += max_cost
        
        return increments
        print(cost)
        print(increments)
    
s = Solution()
s.minIncrements(n = 7, cost = [1,5,2,2,3,3,1])
s.minIncrements(n = 3, cost = [5,3,3])