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
    
import sys
sys.setrecursionlimit(int(1e6))

costs =     [[1, 7, 6, 7, 5, 4, 5, 3, 2, 3]
            ,[7, 1, 2, 4, 2, 3, 5, 4, 5, 6]
            ,[6, 2, 1, 2, 3, 2, 3, 5, 4, 5]
            ,[7, 4, 2, 1, 5, 3, 2, 6, 5, 4]
            ,[5, 2, 3, 5, 1, 2, 4, 2, 3, 5]
            ,[4, 3, 2, 3, 2, 1, 2, 3, 2, 3]
            ,[5, 5, 3, 2, 4, 2, 1, 5, 3, 2]
            ,[3, 4, 5, 6, 2, 3, 5, 1, 2, 4]
            ,[2, 5, 4, 5, 3, 2, 3, 2, 1, 2]
            ,[3, 6, 5, 4, 5, 3, 2, 4, 2, 1]]

def solution(numbers):
    nums = {i+1:(i//3, i%3) for i in range(9)}
    nums[0] = (3,1)

    poses = helper({(4, 6):0}, numbers, nums)
    # print(poses)
    return min(poses.values())

def helper(hand_poses, numbers, num_pos):
    if not numbers:
        return hand_poses
    
    current_num = int(numbers[0])
    
    new_poses = {}
    for (left, right), moves in hand_poses.items():
        
        left_moves = costs[left][current_num]
        # clac_distance(num_pos[left], num_pos[current_num])
        right_moves = costs[right][current_num]
        # clac_distance(num_pos[right], num_pos[current_num])
        t_left_moves = moves + left_moves
        t_right_moves = moves + right_moves
         
        left_key = (current_num, right)
        right_key = (left, current_num)
        
        if left_moves == 1:
            if left_key not in new_poses or t_left_moves < new_poses[left_key]:
                new_poses[left_key] = t_left_moves
        elif right_moves == 1:
            if right_key not in new_poses or t_right_moves < new_poses[right_key]:
                new_poses[right_key] = t_right_moves
        else:
            if left_key not in new_poses or t_left_moves < new_poses[left_key]:
                new_poses[left_key] = t_left_moves
            if right_key not in new_poses or new_poses and t_right_moves < new_poses[right_key]:
                new_poses[right_key] = t_right_moves
                
    return helper(new_poses, numbers[1:], num_pos)
        
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
# solution1("1756")
# solution("5123")