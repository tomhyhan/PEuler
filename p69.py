# too slow 
# def gcd(x,y):
#     return y if x % y == 0 else gcd(y, x % y)
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    sieve = set([i for i in range(2, n)])

    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime(i):
            print("prime", i)
            j = 1
            while i * j < n:
                if i * j in sieve:
                    sieve.remove(i * j)
                j += 1

    return sieve 
    
def solution():
    
    max_phi = 0
    max_n = 0
    print(prime_factors(10))
    # for n in range(2,1000001):
    #     prime_factors(n)
    # print("asdf")
    # for n in range(2,100001):
    #     phi = 1
    #     for factor in prime_factors(n):
    #         phi *= factor / (factor - 1) 
    #     if phi > max_phi:
    #         max_phi = phi
    #         max_n = n
    # print(max_phi, max_n)
    pass

solution()
