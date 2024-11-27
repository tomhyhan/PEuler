from itertools import permutations

def is_prime(num):
    if num in [0,1]:
        return False
    
    for d in range(2, int(num**0.5) + 1):
        if num % d == 0:
            return False

    return True

def solution(numbers):
    ps = set()
    for i in range(1,8):
        for perm in permutations(numbers, i):
            c = int(''.join([str(p) for p in perm]))
            if is_prime(c):
                ps.add(c)
    return len(ps)

solution("011")