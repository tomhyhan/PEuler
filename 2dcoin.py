# try 1
# import json
# import heapq
# from copy import deepcopy

# def solution(beginning, target):
#     seen = {}
#     queue = ([(0, clac_diff(beginning, target) ,beginning)])
    
#     while queue:
#         flips, _, board = heapq.heappop(queue)
#         key = json.dumps(board)
        
#         if key in seen and seen[key] < flips:
#             continue

#         if board == target:
#             return flips
        
#         seen[key] = flips
        
#         for row in range(len(board)):
#             new_board = deepcopy(board)
#             flip_row(new_board, row)
#             heapq.heappush(queue, (flips+1, clac_diff(new_board, target), new_board))

#         for col in range(len(board[0])):
#             new_board = deepcopy(board)
#             flip_col(new_board, col)
#             heapq.heappush(queue, (flips+1, clac_diff(new_board, target), new_board))
            
#     return -1

# def clac_diff(b1, b2):
#     diff = 0
#     for i in range(len(b1)):
#         for j in range(len(b1[0])):
#             if b1[i][j] != b2[i][j]:
#                 diff += 1
#     return diff

# def flip_row(board, row):
#     for col in range(len(board[0])):
#         board[row][col] = 0 if board[row][col] == 1 else 1
    
# def flip_col(board, col):
#     for row in range(len(board)):
#         board[row][col] = 0 if board[row][col] == 1 else 1

def solution(beginning, target):

    n_row = len(beginning) 
    n_col = len(beginning[0])
    
    board = [[0 for _ in range(n_col)] for _ in range(n_row)]
    
    for i in range(n_row):
        for j in range(n_col):
            if beginning[i][j] != target[i][j]:
                board[i][j] = 1

    for b in board:
        
        print(b)
        
    print(1024 * 1024)
# def flip_row(board, row):
#     for col in range(len(board[0])):
#         board[row][col] = 0 if board[row][col] == 1 else 1
    
solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]])

# solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 1], [0, 0, 0], [0, 0, 0]])