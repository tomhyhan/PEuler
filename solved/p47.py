import math
from collections import deque

def get_prime_factors(num, primes):
    idx = 0
    factors = set()
    while idx < len(primes) and num >= primes[idx]:
        if num % primes[idx] == 0:
            num = num // primes[idx]
            factors.add(primes[idx])
            continue
        idx += 1
    
    return factors if num == 1 else []

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def get_primes():
    return [n for n in range(2, 1000) if is_prime(n)]

def solution():
    primes = get_primes()
    cons_nums = deque([False,False,False,False])
    c = 4
    for n in range(10, 1000000):
        if all(n for n in cons_nums):
            print(n-c)
            break
        is_distinct = len(get_prime_factors(n, primes)) == c
        cons_nums.popleft()
        cons_nums.append(is_distinct)


solution()
