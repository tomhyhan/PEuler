from utils import time_checker
import numpy as np

def helper(row, col, memo):
    if row == 0 or col == 0:
        return 1
    elif (row,col) in memo:
        return memo[(row,col)]
        
    routes = helper(row-1,col,memo) + helper(row, col-1,memo)
    memo[(row,col)] = routes
    
    return routes

@time_checker
def solution():
    memo = {}
    print(helper(20,20, memo))

@time_checker
def solution2():
    size = 21
    # grid = [[1] * size for _ in range(size)]
    grid = np.ones((size,size))
    for row in range(1,size):
        for col in range(1,size):
            grid[row][col] = grid[row-1][col] + grid[row][col-1] 

    print(grid[20][20])
    
    # print(grid)
            
solution()
solution2()