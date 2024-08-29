# try 1 
# def solution(matrix_sizes):
    
#     memo = {}
#     mm_small = helper(matrix_sizes, memo)
#     print(memo)
#     return mm_small

# def helper(matrix_sizes, memo):
#     key = tuple([tuple(m) for m in matrix_sizes])
    
#     if len(matrix_sizes) == 2:
#         return matrix_sizes[0][0] * matrix_sizes[0][1] *  matrix_sizes[1][1]
#     elif key in memo:
#         print("found~")
#         return memo[key]
    
#     mm_small = float('inf')
#     for i in range(len(matrix_sizes) - 1):
#         matmul_shape = [matrix_sizes[i][0], matrix_sizes[i+1][1]]
#         new_matrix = matrix_sizes[:i] + [matmul_shape] + matrix_sizes[i+2:]
#         mm_curr = matrix_sizes[i][0] * matrix_sizes[i][1] *  matrix_sizes[i+1][1] + helper(new_matrix, memo)
#         # print(mm_curr) 
#         mm_small = min(mm_small, mm_curr)
    
#     memo[key] = mm_small
#     return mm_small

# try 2
# def solution(matrix_sizes):
#     memo = {}
#     _, val = find_mm(matrix_sizes, memo)
#     print(val)

# def find_mm(matrix_sizes, memo):
#     key = tuple(tuple(m) for m in matrix_sizes)
#     if len(matrix_sizes) == 1:
#         return matrix_sizes[0], 0
#     elif key in memo:
#         return memo[key]
    
#     smallest_mm_val = float('inf')
#     smallest_mm = None
#     for i in range(1, len(matrix_sizes)):
#         left_m = matrix_sizes[:i]
#         right_m = matrix_sizes[i:]
#         curr_mm, curr_mm_val = merge(find_mm(left_m, memo), find_mm(right_m, memo))
#         if curr_mm_val < smallest_mm_val:
#             smallest_mm_val = curr_mm_val
#             smallest_mm = curr_mm
#     memo[key] = (smallest_mm, smallest_mm_val) 
#     return (smallest_mm, smallest_mm_val)

# def merge(left, right):
#     left_m, left_val = left
#     right_m, right_val = right
#     return [left_m[0], right_m[1]], left_m[0] * left_m[1] * right_m[1] + left_val + right_val

def solution(matrix_sizes):
    N = len(matrix_sizes)
    DP = [[float("inf") for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N-i):
            a = j
            b = j + i
            if a == b:
                DP[a][b] = 0
                continue
            for k in range(a,b):
                DP[a][b] = min(DP[a][b], DP[a][k] + DP[k+1][b] + (matrix_sizes[a][0] * matrix_sizes[k][1] * matrix_sizes[b][1]))
    return DP[0][-1]

solution([[5,3],[3,10],[10,6],[6,4]])
# 0    0,1  0,2
# 1,0   0   1,2
# 2,0  2,1   0