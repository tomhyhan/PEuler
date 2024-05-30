import heapq

def solution(food_times, k):
    
    heap = []
    for idx, food_time in enumerate(food_times):
        heapq.heappush(heap, (food_time, idx+1))

    prev_min = 0
    n_foods = len(food_times)
    while heap:
        min_food_time, _ = heap[0]
        current_iter = n_foods * (min_food_time - prev_min)  
        # k = 5 n_foods = 3
        # k = 2 n_foods = 2
        # k = 0 n_foods = 1
        
        if current_iter <= k:
            n_foods -= 1
            k -= current_iter
            min_food_time, _ = heapq.heappop(heap)
            prev_min = min_food_time
        else:
            _, min_i = sorted(heap, key=lambda x: x[1])[k % n_foods]
            # print(min_i)
            return min_i
    return -1


solution([3, 1, 2], 5)