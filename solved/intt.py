from copy import deepcopy

def solution(triangle):
    s = deepcopy(triangle)
    for i in range(0, len(triangle)-1):
        for j in range(len(triangle[i])):
            s[i+1][j] = max(s[i+1][j], triangle[i+1][j]+ s[i][j])
            s[i+1][j+1] = max(s[i+1][j+1], triangle[i+1][j+1]+ s[i][j])
    return max(s[-1])

# 30
# solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
solution([[1], [2,3], [4,5,6]])