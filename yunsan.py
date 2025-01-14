def solution(arr):
    numbers = [int(arr[i]) for i in range(0, len(arr), 2)]
    ops = [arr[i] for i in range(1, len(arr), 2)]
    
    print(numbers, ops)
    # [1, 3, 5, 8] ['-', '+', '-']
    N = len(numbers)
    MAXD = [[float("-inf") if i!=j else numbers[i] for j in range(N)] for i in range(N)]
    MIND = [[float("inf") if i!=j else numbers[i] for j in range(N)] for i in range(N)]

    for brac in range(N):
        for i in range(N-brac):
            j = i + brac
            for k in range(i, j):
                if ops[k] == '+':
                    MAXD[i][j] = max(MAXD[i][j], MAXD[i][k] + MAXD[k+1][j])
                    MIND[i][j] = min(MIND[i][j], MIND[i][k] + MIND[k+1][j])
                elif ops[k] == '-':
                    MAXD[i][j] = max(MAXD[i][j], MAXD[i][k] - MIND[k+1][j])
                    MIND[i][j] = min(MIND[i][j], MIND[i][k] - MAXD[k+1][j])
    
    return MAXD[0][-1]

# (((1 - 3) + 5) - 8) = -5
# ((1 - (3 + 5)) - 8) = -15
# (1 - ((3 + 5) - 8)) = 1
# (1 - (3 + (5 - 8))) = 1
# ((1 - 3) + (5 - 8)) = -5

# 1 -3 +5 -8, (1-3)+5-8 | 1-(3+5)-8 | 1-3+(5-8), (-2+5)-8 | -2+(5-8) 
solution(["1", "-", "3", "+", "5", "-", "8"])
# solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"])
# solution(["5", "-", "3", "+", "1", "+", "2", "-", "4", '+', "5", "-", "3", "+", "1", "+", "2", "-", "4", '+', "5", "-", "3", "+", "1", "+", "2", "-", "4", '+', "5", "-", "3", "+", "1", "+", "2", "-", "4"])