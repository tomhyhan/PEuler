# sliding window
# binary search
def solution(stones, k):
    left = 1
    right = max(stones)
    
    n = 0
    while left <= right:
        mid = (left + right) // 2

        prev_d = 0
        diff = 0
        for idx, stone in enumerate(stones):
            next_d = idx + 1
            if stone > mid:
                if next_d - prev_d > k:
                    diff = next_d - prev_d
                prev_d = next_d

        if len(stones) + 1  - prev_d > k:
            print (len(stones) + 1 , prev_d)
            diff = len(stones) + 1 - prev_d
            
        if diff > k:
            right = mid - 1
        else:
            left = mid + 1
            n = left

    return n

solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
# solution([7, 2, 8, 7, 2, 5, 9], 3)
