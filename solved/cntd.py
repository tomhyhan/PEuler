from collections import deque
#  one more with point target reverse
#  find optimal
def solution(target):
    result = [[float("inf"),0] for _ in range(target+1)]
    singles = [s for s in range(1,21)]
    doubles = [s*2 for s in range(1,21)]
    triples =[s*3 for s in range(1,21)]
    points = singles + doubles + triples + [50]
    # print(points)
    result[0][0] = 0
    for i, p in enumerate(points):
        for s in range(target+1):
            if s >= p:
                new_result = [r for r in result[s-p]]
                new_result[0] += 1
                if 0 <= i < 20 or  p == 50: 
                    new_result[1] += 1
                print(s,p, new_result)
                result[s] = min(result[s], new_result, key=lambda x: (x[0], -x[1]))
    
    return result[target]
    print(result)
            
            
# solution(2)
# solution(21)
# solution(58)
# solution(23)