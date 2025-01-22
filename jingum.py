def solution(distance, rocks, n):
    # 각 지점 사이의 거리의 최솟값 중에 가장 큰 값
    max_distance = 1_000_000_000
    rocks.sort()
    
    n_rocks = len(rocks)
    left = 0
    right = max_distance
    print(rocks)
    max_conn_distance = float('-inf')    
    while left <= right:
        mid = (left + right) // 2
        
        cnt_n = 0
        for i in range(n_rocks):
            distance_btw = distance if i == n_rocks-1 else rocks[i+1] - rocks[i]
            if mid > distance_btw:
                cnt_n += 1
        
        if cnt_n >= n:
            right = mid - 1
            if cnt_n == n:
                max_conn_distance = max(max_conn_distance, mid)
        else:
            left = mid + 1
        
    return max_conn_distance

print(solution(25, [2, 14, 11, 21, 17], 2))