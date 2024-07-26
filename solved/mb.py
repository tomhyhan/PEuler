from collections import Counter

def solution(food_times, k):
    food_cnt = Counter(food_times)
    n_ft = len(food_times)
    
    cycle = 0
    prev_food = 0
    while len(food_cnt) > 0:
        min_food = min(food_cnt)
        cycle = n_ft * (min_food - prev_food)
        if cycle <= k:
            n_ft -= food_cnt[min_food]
            k -= cycle
            prev_food = min_food
            del food_cnt[min_food]
        else:
            ki = k % n_ft
            for i, food in enumerate(food_times):
                if food not in food_cnt:
                    continue
                if i == ki:
                    print(i + 1)
                    return i + 1
        # print(k, cycle, food_cnt)
    return -1
solution([3, 1, 2,500 ,22, 3 ,1], 333)