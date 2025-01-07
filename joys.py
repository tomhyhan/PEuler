# (13 - abs(ord(name[i]) - ord('N')))
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


# print(solution("BBBBAAAAB"))
solution("JAN")
# solution("JAZ")
# solution("JZA")
# solution("JEROEN")