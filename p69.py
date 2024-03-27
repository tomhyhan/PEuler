# too slow 
# def gcd(x,y):
#     return y if x % y == 0 else gcd(y, x % y)
import math


# try to make a list of prime numbers and try again
def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n, primes):
    i=0
    factors = set()
    while n > 1:
        factor = primes[i] 
        if n % factor == 0:
            factors.add(factor)
            n //= factor
        else:
            i += 1
            
    return factors
    
def solution():
    
    max_phi = 0
    max_n = 0
    
    primes = []
    for n in range(2, 1000000):
        if is_prime(n):
            primes.append(n)
    print(prime_factors(12, primes))

    # for n in range(2,100001):
    for n in range(2,1000001):
        phi = 1
        for factor in prime_factors(n, primes):
            phi *= factor / (factor - 1) 
        if phi > max_phi:
            max_phi = phi
            max_n = n
    print(max_phi, max_n)

def solution1():
    print(2 * 3 * 5 * 7 * 11 * 13 * 17)
    pass

# solution()
solution1()
