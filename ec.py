def solution(grid, D, k):
    NR = len(grid)
    NC = len(grid[0])
    NRC = NR * NC

    DP =  [ [[0 for _ in range(NRC) ] for _ in range(NRC)] for _ in range(len(D) + 1)]

    for i in range(NRC):
        DP[0][i][i] = 1
    
    for i in range(1, len(D) + 1):
        for row in range(NR):
            for col in range(NC):
                for dir in [[0,1],[0,-1],[1,0],[-1,0]]:
                    nrow = row + dir[0]
                    ncol = col + dir[1]
                    
                    if 0 <= nrow < NR and 0 <= ncol < NC and grid[nrow][ncol] - grid[row][col] == D[i-1]:
                        for j in range(NRC):
                            DP[i][j][nrow*NC+ncol] += DP[i-1][j][row*NC+col] 
    
    print(DP[len(D)][6][3])
    
    
    

    
solution([[3, 4, 6, 5, 3], 
          [3, 5, 5, 3, 6], 
          [5, 6, 4, 3, 6], 
          [7, 4, 3, 5, 0]], [1, -2, -1, 0, 2], 2)

# solution([[0, 0, 0], 
#           [1, 0, 0], 
#           [0, 0, 0], 
#           [0, 0, 1], 
#           [1, 0, 0]], 
#             [0, 0, 1, -1, 0, 0, 1, -1], 
#             10)