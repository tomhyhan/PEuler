def solution(a):
    right_mins = [float("inf")] * len(a)
    left_mins = [float("inf")] * len(a)
    
    for i in range(1, len(a)):
        left_mins[i] = min(left_mins[i-1], a[i-1])
    
    for i in reversed(range(0, len(a)-1)):
        right_mins[i] = min(right_mins[i+1], a[i+1])
    
    print(left_mins)
    print(right_mins)
    print(a)
    result = []
    for i in range(len(a)):
        used_chance = False
        
        if left_mins[i] < a[i]:
           used_chance = True 
        
        if used_chance and right_mins[i] < a[i]:
            continue
        
        result.append(a[i])
    
    return len(result)
    # answer = 0
    # return answer

# solution([9,-1,-5])

solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])