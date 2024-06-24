import heapq
def solution(n, works):
    if sum(works) <= n:
        return 0
    
    for i in range(len(works)):
        works[i] *= -1
      
    heapq.heapify(works)
      
    for _ in range(n):
        high = heapq.heappop(works)
        heapq.heappush(works, min(0,high+1))    
        
    return sum([w*w for w in works])


solution( 4,[4, 3, 3])