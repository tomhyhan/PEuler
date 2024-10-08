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

def solution(beginning, target):
    print((1 << 0) & 3)
    print((1 << 1) & 3)
    print((1 << 2) & 3)

solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]) 
# solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 1], [0, 0, 0], [0, 0, 0]])