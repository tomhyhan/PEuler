def solution(triangle):
    for i in reversed(range(len(triangle) - 1)):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])         

    return triangle[0][0]

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])