def solution(mats, park):
    mats.sort(reverse=True)
    for mat in mats:
        match_block = [['-1' for _ in range(mat)] for _ in range(mat)]
        for row in range(len(park) - mat + 1):
            for col in range(len(park[0]) - mat + 1):
                curr_block = [[park[row+i][col+j] for j in range(mat)] for i in range(mat)]
                if curr_block == match_block:
                    return mat
    return -1
    

solution([5,3,2], [["A", "A", "-1", "B", "B", "B", "B", "-1"], ["A", "A", "-1", "B", "B", "B", "B", "-1"], ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]])