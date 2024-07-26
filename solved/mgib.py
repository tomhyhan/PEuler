def solution(n, s):

    answer = []
    
    remainder = s
    while n > 0:
        num = remainder // n
        remainder -= num
        if num == 0:
            return [-1]
        n -= 1
        answer.append(num)
    print(10%5)
    return answer
        
solution(2, 9)
solution(5, 10)
solution(2, 1)