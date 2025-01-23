def solution(distance, rocks, n):
    # 각 지점 사이의 거리의 최솟값 중에 가장 큰 값
    rocks = [0] + rocks + [distance]
    rocks.sort()

    n_rocks = len(rocks)
    left = 1
    right = distance
    min_distance = float('inf')

    while left <= right:
        mid = (left + right) // 2

        cnt_n = 0
        curr_rock = rocks[0]
        min_diff = float('inf')
        for i in range(1, n_rocks):
            next_rock = rocks[i]
            diff = next_rock - curr_rock 
            if diff < mid:
                cnt_n += 1
            else:
                curr_rock = next_rock
                min_diff = min(min_diff, diff)
        print(left, right)
        if cnt_n > n:
            right = mid - 1
        else:
            min_distance = mid
            left = mid + 1

    return min_distance

# print(solution(25, [2, 14, 11, 21, 17], 2))
print(solution(25, [2, 4, 6, 8, 10], 2))