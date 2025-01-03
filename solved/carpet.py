def solution(brown, yellow):
    divisors = []
    
    for i in range(1, int(yellow**0.5) + 1) :
        if yellow % i == 0:
            divisors.append((i, yellow // i))
    for row, col in divisors:
        if 2 * row + 2 * col + 4 == brown:
            return [col+2, row+2]

print(solution(24, 24))