import math 

MOD = 1e9 + 7
MOD = 1000000007

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

    kbit = 0
    while math.pow(2, kbit) < k:
        kbit += 1

    matmuls = [[[val for val in row] for row in DP[len(D)]]]
    for i in range(1, kbit+1):
        matmuls.append(matmul(matmuls[i-1], matmuls[i-1]))

    mat = DP[0]
    while k > 0:
        if k >= math.pow(2, kbit):
            mat = matmul(mat, matmuls[kbit])
            k -= math.pow(2, kbit)
        kbit -= 1
    
    result = 0
    for row in range(NRC):
        for col in range(NRC):
            result = (result + mat[row][col]) % MOD
            
    return result    
    
    
def matmul(A, B):
    N = len(A)
    mat = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            for p in range(N):
                mat[x][y] += (A[x][p]  * B[p][y] ) % MOD
    return mat     

    
# solution([[3, 4, 6, 5, 3], 
#           [3, 5, 5, 3, 6], 
#           [5, 6, 4, 3, 6], 
#           [7, 4, 3, 5, 0]], [1, -2, -1, 0, 2], 2)
solution([[3, 6, 11, 12], [4, 8, 15, 10], [2, 7, 0, 16]],[1, -2, 5],3)
solution([[0, 0, 0], [1, 0, 0], [0, 0, 0], [0, 0, 1], [1, 0, 0]],[0, 0, 1, -1, 0, 0, 1, -1],10)