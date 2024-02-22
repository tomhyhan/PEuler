from itertools import permutations
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution():
    for i in range(8,0,-1):
        print(i)
        li = list(reversed([i for i in range(1,i)]))
        for perm in permutations(li, i-1):
            num = int(''.join(map(str, perm)))
            if is_prime(num):
                print(num)
                return

solution()