
import heapq

def solution(jobs):
    
    i = 0
    heapq.heapify(jobs)
    jobs_waiting = []
    # 0- 3  5 - 7
    jobs_compl = []
    while len(jobs) > 0  or len(jobs_waiting) > 0:
        if jobs_waiting:
            _, next_start, next_end = heapq.heappop(jobs_waiting)
            jobs_compl.append(next_end - next_start)
        else:
            curr_start, curr_end = heapq.heappop(jobs)
            jobs_compl.append(curr_end - curr_start)
            print(jobs[0][0])
            while jobs and jobs[0][0] < curr_end:
                next_start, next_end = heapq.heappop(jobs)
                curr_end += next_end
                heapq.heappush(jobs_waiting, (next_end - next_start, next_start, next_end))
                print(jobs)
    
    print(sum(jobs_compl) // len(jobs_compl))
    return sum(jobs_compl) // len(jobs_compl)
    
solution([[0, 3], [1, 9], [2, 6]])
# solution([[0, 3], [1, 9], [5, 6]])