import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution():
    n = 28433
    for _ in range(7830457):
        n = ((n * 2) % 10**10) 
    print(n + 1)
    print((28433 * 2**7830457 + 1) % 10**10) 
    # print(str(2 ** 6992593 - 1)[-10:])
    # print(2 ** 17 - 1)


solution()