
import heapq

def solution(jobs):
    jobs = [[s, s+e] for s, e in jobs]
    
    heapq.heapify(jobs)
    jobs_waiting = []
    jobs_compl = []
    job_end = 0
    
    while jobs or jobs_waiting:
        if jobs_waiting:
            duration, curr_s = heapq.heappop(jobs_waiting)
            jobs_compl.append(job_end + duration - curr_s)
            job_end += duration
        else:
            curr_s, curr_e = heapq.heappop(jobs)
            if curr_s > job_end:
                job_end = curr_s
            duration = curr_e - curr_s
            jobs_compl.append(duration)
            job_end += duration
        
        while jobs and jobs[0][0] <= job_end:
            curr_s, curr_e = heapq.heappop(jobs)
            heapq.heappush(jobs_waiting, (curr_e - curr_s, curr_s))
    
    # print(jobs_compl)
    print(sum(jobs_compl) // len(jobs_compl))
    return sum(jobs_compl) // len(jobs_compl)
        
    
    
# import heapq

# def solution(jobs):
#     jobs = [(start, start + duration) for start, duration in jobs]
#     heapq.heapify(jobs)
#     jobs_waiting = []
#     jobs_compl = []
#     current_time = 0

#     while jobs or jobs_waiting:
#         if jobs_waiting:
#             duration, end = heapq.heappop(jobs_waiting)
#             jobs_compl.append(current_time + duration - (end - duration))
#             current_time += duration
#         else:
#             start, end = heapq.heappop(jobs)
#             if start > current_time:
#                 current_time = start
#             print(current_time, start, end)
#             jobs_compl.append(end - start) 
#             current_time += end - start

#         while jobs and jobs[0][0] <= current_time:
#             start, end = heapq.heappop(jobs)
#             heapq.heappush(jobs_waiting, (end - start, end))
    
#     print(sum(jobs_compl) // len(jobs_compl))
#     return sum(jobs_compl) // len(jobs_compl)


solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]])

solution([[0, 3], [1, 9], [2, 6]])
# solution([[0, 6], [2, 8], [3, 7], [7, 1], [11, 11], [19, 25], [30, 15], [32, 6], [40, 3]])