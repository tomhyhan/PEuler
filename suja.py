# try 1
# def solution(numbers):
#     nums = {f"{i+1}":(i//3, i%3) for i in range(9)}
#     nums['0'] = (3,1)
    
#     stack = [(0, 0, (1,0), (1,2))]
#     min_moves = float('inf')
#     while stack:
#         moves, idx, left, right = stack.pop()
        
#         if idx >= len(numbers):
#             min_moves = min(min_moves, moves)
#             continue
        
#         num = numbers[idx]
#         num_pos = nums[num]
#         left_distance = clac_distance(num_pos, left)
#         right_distance = clac_distance(num_pos, right)
#         if left_distance == right_distance:
#             stack.append((moves + left_distance, idx+1, num_pos, right))
#             stack.append((moves + right_distance, idx+1, left, num_pos))
#         elif left_distance > right_distance:
#             stack.append((moves + right_distance, idx+1, left, num_pos))
#         else:
#             stack.append((moves + left_distance, idx+1, num_pos, right))
#     # print(min_moves)
#     return min_moves

# def clac_distance(num_pos, hand_pos):
#     if num_pos == hand_pos:
#         return 1
    
#     nrow, ncol = num_pos
#     hrow, hcol = hand_pos
    
#     trow = abs(nrow - hrow)
#     tcol = abs(ncol - hcol)
    
#     max_t = max(trow, tcol) 
#     min_t = min(trow, tcol)
#     return min_t * 3 + (max_t - min_t) * 2   

# def solution(numbers):
#     nums = {f"{i+1}":(i//3, i%3) for i in range(9)}
#     nums['0'] = (3,1)
    
#     left = (1,0)
#     right = (1,2)
#     moves = 0
    
#     for idx in range(len(numbers)):
#         num = numbers[idx]
#         num_pos = nums[num]
#         left_distance = clac_distance(num_pos, left)
#         right_distance = clac_distance(num_pos, right)
#         if left_distance == right_distance:
#             if idx + 1 < len(numbers):
#                 num_next = numbers[idx+1]
#                 num_pos_next = nums[num_next]
#                 left_distance_next = clac_distance(num_pos_next, left)
#                 right_distance_next = clac_distance(num_pos_next, right)
#                 if left_distance_next > right_distance_next:
#                     moves += left_distance
#                     left = num_pos
#                 else:
#                     moves += right_distance
#                     right = num_pos
#             else:
#                 moves += left_distance
#                 left = num_pos
#         elif left_distance > right_distance:
#             moves += right_distance
#             right = num_pos
#         else:
#             moves += left_distance
#             left = num_pos
#     # print(moves)
#     return moves

# def clac_distance(num_pos, hand_pos):
#     if num_pos == hand_pos:
#         return 1
    
#     nrow, ncol = num_pos
#     hrow, hcol = hand_pos
    
#     trow = abs(nrow - hrow)
#     tcol = abs(ncol - hcol)
    
#     max_t = max(trow, tcol) 
#     min_t = min(trow, tcol)
#     return min_t * 3 + (max_t - min_t) * 2
    # 0,0 -> 1,2   
    
def solution(numbers):
    nums = {f"{i+1}":(i//3, i%3) for i in range(9)}
    nums['0'] = (3,1)
    print(nums)
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
        stack.append((moves + left_distance, idx+1, num_pos, right))
        stack.append((moves + right_distance, idx+1, left, num_pos))
    print(min_moves)
    return min_moves

def clac_distance(num_pos, hand_pos):
    if num_pos == hand_pos:
        return 1
    
    nrow, ncol = num_pos
    hrow, hcol = hand_pos
    
    trow = abs(nrow - hrow)
    tcol = abs(ncol - hcol)
    
    max_t = max(trow, tcol) 
    min_t = min(trow, tcol)
    return min_t * 3 + (max_t - min_t) * 2  

solution("1756")
solution("5123")