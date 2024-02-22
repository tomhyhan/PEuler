import math

def is_prime(num):
    if num <= 0:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def get_primes_n(a,b):
    n = 0
    while is_prime(n*n + a*n + b):
        n += 1
    return n

def solution():
    max_primes = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            current = get_primes_n(a,b)
            if max_primes < current:
                max_primes = current
                print(a * b)
    print(max_primes)
solution()