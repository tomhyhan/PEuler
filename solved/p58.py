
import math 

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution():
    corner = 1
    primes = 0
    d_nums = 1
    for layer in range(1,100000):
        step = 2 * layer
        d_nums += 4 
        for _ in range(4):
            corner += step
            if is_prime(corner):
                primes += 1
        ratio = primes / d_nums
        if ratio < 0.10:
            print(ratio)
            print(2 * layer + 1)
            break
    pass

solution()