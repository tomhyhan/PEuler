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
    left = 0
    right = max(cores) * n
    
    while left < right:
        mid_time = (left + right) // 2
        
        current_n = 0
        for core in cores:
            current_n += mid_time // core

        if current_n >= n:
            right = mid_time
        else:
            left = mid_time + 1

    less_right = right - 1
    for core in cores:
        n -= less_right // core 
        
    for idx, core in enumerate(cores):
        if right % core == 0:
            n -= 1
            if n == 0:
                return idx + 1
# [2,1] 
# 1 2 3 4 5 6 
# 1 
solution(6, [1,2,3]) 