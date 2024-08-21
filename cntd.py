from collections import deque

def solution(target):
    bulls, left = divmod(target, 50)
    answer = [bulls, bulls]

    if left <= 20:
        answer[0] +=1
        answer[1] +=1
    else:
        if (left % 2 == 0 and left <= 40) or (left % 3 == 0):
            answer[0] += 1
        else:
            answer[0] +=2
            answer[1] +=2
    print(answer)
    return answer
            
            
solution(21)
solution(58)
solution(23)