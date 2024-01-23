import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution():
    primes = 0
    num = 2
    while primes < 10001:
        if is_prime(num):
            primes += 1
            print(num)
        num += 1
    pass    

solution()