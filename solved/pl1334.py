class Solution:

    def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
        distances = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]
        
        for src, dest, w in edges:
            distances[src][dest] = w
            distances[dest][src] = w
        
        for from_ in range(n):
            for src in range(n):
                for dest in range(n):
                    distances[src][dest] = min(distances[src][dest], distances[from_][src] + distances[dest][from_])

        min_travel = float('inf')
        city = -1
        
        for src in range(n):
            travel = 0
            for dest in range(n):
                if src != dest and distances[src][dest] <= distanceThreshold:
                    travel += 1
            if travel <= min_travel:
                min_travel = travel
                city = src

        return city 

s= Solution()
s.findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4)
        