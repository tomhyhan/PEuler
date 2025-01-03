import heapq
from itertools import product

def solution(k, n, reqs):
    min_wait_time = float("inf")
    
    for coach_list in product(range(1,n-k+2), repeat=k):
        if sum(coach_list) == n:
            queues = [[0] * n_c for n_c in coach_list]
            wait_time = 0
            for start, end, class_ in reqs:
                c_end_time = heapq.heappop(queues[class_-1]) 
                if c_end_time - start >= 0:
                    wait_time += c_end_time - start 
                    c_end_time += end
                else:
                    c_end_time = start + end
                heapq.heappush(queues[class_-1], c_end_time)
            min_wait_time = min(min_wait_time, wait_time)
                
    return min_wait_time

solution(3,5,[[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]])
# solution(4,6,[])