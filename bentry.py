def solution(n, times):
    times.sort()
    left = 1
    right = max(times) * n
    
    while left < right:
        mid = (left + right) // 2

        cnt = 0
        for time in times:
            cnt += mid // time

        if cnt >= n :
            right = mid
        else :
            left = mid + 1
            
    print(left, right)
    return left

solution(6, [7, 10]) # 28

# solution(6, [10, 1])
# solution(6, [2, 5])
# solution(59, [1,1])