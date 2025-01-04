# (13 - abs(ord(name[i]) - ord('N')))

def ways(i, moves, go_front, name):
    
    if name[i] != 'A':
        ways(i + 1, moves + 1, go_front, name)
    pass

def solution(name):
    moves = 0
    min_move = len(name) - 1
    
    for i in range(len(name)):
        moves += (13 - abs(ord(name[i]) - ord('N')))
        
        next = i + 1
        cnt = 0
        while next < len(name) and name[next] == 'A':
            cnt += 1
            next += 1
            
        min_move = min(min_move, i + len(name) - 1- cnt, i + 2 * (len(name) - next))
    moves += min_move
    return moves

# 0 8 16
# 0 9 1

# 1 9 15
# 2 9 2

# 2 10 14
# 4 9 3

# 3 7 5
# 6 9 8

# 4 9 6
# 8 9 8

# 5 11 7
# 10 9 8

# 6 13 8
# 12 9 8

# 7 15 9
# 14 9 8

# 8 16 8
# 16 9 9

# 10
# print(solution("BBBBAAAAB"))
solution("JAN")
# solution("JAZ")
# solution("JZA")
# solution("JEROEN")