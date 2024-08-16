import heapq

def solution(n, cores):
    if n < len(cores):
        return cores[n-1]

    scheduler = []
    jobs_done = 0
    for idx, core in enumerate(cores):
        heapq.heappush(scheduler, (core, idx+1, core))        
        jobs_done += 1
        
    time = 1
    while True:
        while time == scheduler[0][0]:
            end_time, label, process_time = heapq.heappop(scheduler)
            jobs_done += 1
            heapq.heappush(scheduler, (end_time + process_time, label, process_time))
            # print(time, end_time, process_time)
            if n == jobs_done:
                return label
        time += 1


def solution(n, cores):
    n -= len(cores)
    left = 1
    right = max(cores) * n

    while left < right:
        mid = (left + right) // 2
        capacity = 0
        for c in cores:
            capacity += mid // c
        if capacity >= n:
            right = mid
        else:
            left = mid + 1    
    
    print(left, right)
       
# [2,1]
# 1 2 3 4 5 6 
# 1 
solution(6, [1,2,3])