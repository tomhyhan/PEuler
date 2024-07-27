def solution(sequence):
    
    p = -1
    current_max = 0
    max_so_far = 0
    for num in sequence:
        current_max = max(0, current_max + num * p)
        max_so_far = max(max_so_far, current_max)
        p *= -1
        print(max_so_far)
    print()
    p = 1
    current_max = 0
    max_so_far2 = 0
    for num in sequence:
        current_max = max(0, current_max + num * p)
        max_so_far2 = max(max_so_far2, current_max)
        p *= -1
        print(max_so_far2)
    
    # print(max_so_far, max_so_far2)
    
    return max(max_so_far, max_so_far2)
