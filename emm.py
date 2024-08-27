def solution(matrix_sizes):
    
    memo = {}
    mm_small = helper(matrix_sizes, memo)
    print(memo)
    return mm_small

def helper(matrix_sizes, memo):
    key = tuple([tuple(m) for m in matrix_sizes])
    
    if len(matrix_sizes) == 2:
        return matrix_sizes[0][0] * matrix_sizes[0][1] *  matrix_sizes[1][1]
    elif key in memo:
        print("found~")
        return memo[key]
    
    mm_small = float('inf')
    for i in range(len(matrix_sizes) - 1):
        matmul_shape = [matrix_sizes[i][0], matrix_sizes[i+1][1]]
        new_matrix = matrix_sizes[:i] + [matmul_shape] + matrix_sizes[i+2:]
        mm_curr = matrix_sizes[i][0] * matrix_sizes[i][1] *  matrix_sizes[i+1][1] + helper(new_matrix, memo)
        # print(mm_curr) 
        mm_small = min(mm_small, mm_curr)
    
    memo[key] = mm_small
    return mm_small

solution([[5,3],[3,10],[10,6], [6,3],[3,10],[10,6]])