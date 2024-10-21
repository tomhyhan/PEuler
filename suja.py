def solution(numbers):
    nums = {f"{i+1}":(i//3, i%3) for i in range(9)}
    nums['0'] = (3,1)
    
    stack = [(0, 0, (1,0), (1,2))]
    min_moves = float('inf')
    while stack:
        moves, idx, left, right = stack.pop()
        
        if idx >= len(numbers):
            min_moves = min(min_moves, moves)
            continue
        
        num = numbers[idx]
        num_pos = nums[num]
        left_distance = clac_distance(num_pos, left)
        right_distance = clac_distance(num_pos, right)
        # if left_distance == right_distance:
        #     stack.append((moves + left_distance, idx+1, num_pos, right))
        #     stack.append((moves + right_distance, idx+1, left, num_pos))
        # el
        if left_distance > right_distance:
            stack.append((moves + right_distance, idx+1, left, num_pos))
        else:
            stack.append((moves + left_distance, idx+1, num_pos, right))
        print(left, right)
    print(min_moves)
    return min_moves

def clac_distance(num_pos, hand_pos):
    if num_pos == hand_pos:
        return 1
    
    nrow, ncol = num_pos
    hrow, hcol = hand_pos
    
    trow = abs(nrow - hrow)
    tcol = abs(ncol - hcol)
    
    diagnol = trow if trow < tcol else tcol
    straight = abs(trow - tcol)
    return diagnol * 3 + straight * 2
    # 0,0 -> 1,2    
    

# solution("1756")
solution("5123")