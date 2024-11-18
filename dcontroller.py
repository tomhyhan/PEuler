import heapq

def solution(jobs):
    stand_by = [(start_time, req_time, idx) for idx, (start_time, req_time) in enumerate(jobs)]
    queue = []
    
    heapq.heapify(stand_by)
    
    h_end = 0
    total = 0
    while stand_by:
        if not queue:
            start_time, req_time, idx = heapq.heappop(stand_by) 
            h_end = start_time
            heapq.heappush(queue, (req_time, start_time, idx)) 
        
        while queue:
            req_time, start_time, idx = heapq.heappop(queue)
            
            h_end += req_time
            total += h_end - start_time
            while stand_by and h_end >= stand_by[0][0]:
                start_time, req_time, idx = heapq.heappop(stand_by) 
                heapq.heappush(queue, (req_time, start_time, idx)) 

    return total // len(jobs)

# 8
# solution([[0, 3], [1, 9], [3, 5]])
# print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
# print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
# print(solution([[0, 3], [1, 9], [2, 6]]), 9)
# print(solution([[0, 1]]), 1)
# print(solution([[1000, 1000]]), 1000)
# print(solution([[0, 1], [0, 1], [0, 1]]), 2)
# print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
# print(solution([[0, 1], [1000, 1000]]), 500)
# print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
# print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)