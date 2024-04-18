import math
from itertools import permutations, product

def is_prime(num):
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution():
    primes = []
    
    for i in range(10, 1000000):
        if is_prime(i):
            primes.append(i)

    for prime in primes:
        p_li = list(str(prime)) 
        p_len = len(p_li)
        for replace in product(*[(True, False) for _ in range(p_len - 1)]):
            p_family = set()
            for i in range(10):
                if i==0 and replace[0]:
                    continue
                new_p = [str(i) if replace[pi] else p_li[pi] for pi in range(len(p_li) - 1)] + [p_li[-1]]
                int_p = int(''.join(new_p))
                if is_prime(int_p):
                    p_family.add(int_p)
            if len(p_family) == 8:
                print(p_family)
                return 
solution()