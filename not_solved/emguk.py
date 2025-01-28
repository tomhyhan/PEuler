def solution(n, times):
    max_time = n * max(times)
    # print("max_time", max_time)
    left = 0
    right = max_time
    
    min_time = float('inf')
    while left <= right:
        mid = (left + right) // 2

        cnt_n = 0
        for time in times:
            cnt_n += mid // time
        if cnt_n >= n:
            right = mid - 1
            min_time = min(min_time, mid) 
        else:
            left = mid + 1

    return min_time
print(solution(6, [7, 10]))
# print(solution(7, [7, 10]))