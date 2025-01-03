def find_max_time(g, s, w, t):
    time = 0
    
    for gold, silver, weight, time in zip(g, s, w, t):
        time = max(time, ((gold + silver) // weight - 1) * 2*time + time)
    return time

def solution(a, b, g, s, w, t):
    max_time = find_max_time(g, s, w, t)
    left = 1
    right = max_time*10
    result = max_time*10
    while left <= right:
        mid = (left + right) // 2
        tg = 0
        ts = 0
        total = 0
        for gold, silver, weight, time in zip(g, s, w, t):
            moves = mid // (time*2) 
            if mid % (time*2) >= time:
                moves += 1
            tg += min(gold, weight * moves)
            ts += min(silver, weight * moves)
            total += min(gold+silver, weight * moves)
            
        if tg >= a and ts >= b and total >= a+b:
            result = min(result, mid)
            right = mid - 1
        else:
            left = mid + 1
    return result

# solution(10, 10, [100], [100], [7], [10])
solution(90, 500, [70,70,0], [0,0,500], [100,100,2], [4,8,1])