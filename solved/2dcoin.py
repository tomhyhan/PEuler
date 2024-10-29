# try 1
from itertools import product

def solution(beginning, target):
    
    n_row = len(beginning)
    n_col = len(beginning[0])
    
    for row_comb in sorted(product([0,1], repeat=n_row), key=lambda x: x.count(1)):
        row_begin = [[col for col in row] for row in beginning]
        flips = 0
        for row, do_flip in enumerate(row_comb):
            if not do_flip:
                continue
            row_begin[row] = [0 if coin == 1 else 1 for coin in row_begin[row]]
            flips += 1

        for col_comb in sorted(product([0,1], repeat=n_col), key=lambda x: x.count(1)):
            col_begin = [[col for col in row] for row in row_begin]
            col_flips = 0
            for col, do_flip in enumerate(col_comb):
                if not do_flip:
                    continue
                for row in range(n_row):
                    col_begin[row][col] = 0 if col_begin[row][col] == 1 else 1
                col_flips += 1
                
            if col_begin == target:
                total_flips = flips + col_flips
                return total_flips
    return -1 

# idea 1: flip rows -> flip cols in line by line -> check if fliped == target
# idea 2: start with board by comparing begin and target -> flip the rows -> check if only 0 or 1 is in col line, and if 1 is in col line add 1 to count
def solution(beginning, target):
    
    n_rows = len(beginning)
    n_cols = len(target)
    low_flips = float('inf')
    
    for bits in range(2**n_rows):
        row_begin = [[col for col in row] for row in beginning] 
        flips = 0
        for row in range(n_rows):
            if (1 << row) & bits:
                row_begin[row] = [1-cur for cur in row_begin[row]] 
                flips += 1
                
        for col in range(n_cols):
            curr_col = []
            target_col = []

            for row in range(n_rows):
                curr_col.append(row_begin[row][col])
                target_col.append(target[row][col])
                
            if curr_col != target_col:
                for row in range(n_rows):
                    row_begin[row][col] = 1-row_begin[row][col]
                flips += 1
                
        if row_begin == target:
            low_flips = min(low_flips, flips)
            
    return -1 if low_flips == float('inf') else low_flips       
        
# very cool solution
# def solution(beginning, target):
#     answer = 0
#     table = [[beginning[i][j] ^ target[i][j] for j in range(len(beginning[i]))] for i in range(len(beginning))]
#     cnt = 0
#     m = len(table)
#     n = len(table[0])
#     print(table)
#     for i in range(1, m):
#         if (table[i] != table[0]):
#             cnt+=1
#             if (list(map(lambda x: x ^ 1, table[i])) != table[0]):
#                 return -1

#     answer = min((cnt) + sum(table[0]), (m - cnt) + (n - sum(table[0])))

#     return answer

solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]) 
# solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 1], [0, 0, 0], [0, 0, 0]])