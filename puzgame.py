def solution(diffs, times, limit):
    left = 1
    right = 100_000 * 10_000 * 300_000
    
    min_level = float('inf')
    while left <= right:
        level = (left + right) // 2 
        
        total_time = 0
        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            if diff <= level:
                total_time += time_cur
            else:
                time_prev = times[i-1]
                repeat = diff - level
                total_time += repeat * (time_prev + time_cur) + time_cur
        #  12 10 
        # 
        if total_time <= limit:
            right = level - 1
            min_level = min(min_level, level)
        else:
            left = level + 1   
    return min_level
solution([1, 5, 3], [2, 4, 7], 30)
solution([1, 4, 4, 2], [6, 3, 8, 2], 59)
solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723)