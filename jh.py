def solution(land, P, Q):
    max_l = max([max(l) for l in land])

    left = 0
    right = max_l
    
    while left <= right:
        mid_h = (left + right) // 2

        slope, current_cost = cost(land, mid_h, P, Q)
        if slope == 1:
            right = mid_h - 1
        elif slope == -1:
            left = mid_h + 1
        elif slope == 0:
            break

    return current_cost

def cost(land, mid_h, P, Q):
    N = len(land)
    mid_b = mid_h - 1
    mid_t = mid_h + 1
    
    mid_c = mid_bc = mid_tc = 0
    
    for row in range(N):
        for col in range(N):
            current_h = land[row][col]
            mid_c += max(mid_h - current_h, 0) * P + max(current_h - mid_h, 0) * Q
            mid_bc += max(mid_b - current_h, 0) * P + max(current_h - mid_b, 0) * Q
            mid_tc += max(mid_t - current_h, 0) * P + max(current_h - mid_t, 0) * Q
            
    if mid_c <= mid_bc and mid_c <= mid_tc:
        return 0, mid_c
    elif mid_bc <= mid_c <= mid_tc:
        return 1, mid_c
    elif mid_bc >= mid_c >= mid_tc:
        return -1, mid_c

# solution([[1, 2], [2, 3]], 3, 2)
solution([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]], 5, 3)