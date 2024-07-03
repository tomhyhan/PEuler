def solution(A, B):
    A = sorted(A)
    B = sorted(B)
    
    b_wins = 0
    while A and B:
        if A[-1] < B[-1]:
            B.pop()
            b_wins += 1
        A.pop()

    return b_wins

solution([5,1,3,7], [2,2,6,8])
solution([2,2,2,2], [1,1,1,1])