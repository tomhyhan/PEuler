import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
    
def solution():
    primes = []
    for n in range(1000, 10000):
        if is_prime(n):
            primes.append(n)
    print(is_prime(2969))
    print(is_prime(2969+3330))
    print(is_prime(2969+3330*2))
    print(str(2969) + str(2969+3330) + str(2969+3330*2))
    for x in primes:
        if (x+3330) in primes and (x+3330*2) in primes and (set(str(x)) == set(str(x+3330))):
            print(x)

solution()