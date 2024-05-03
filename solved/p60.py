from itertools import permutations, combinations
from collections import defaultdict
import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n)) +1):
        if n % i == 0:
            return False
    return True

def concat_primes(p1, p2):
    pcat1 = int(str(p1) + str(p2))
    pcat2 = int(str(p2) + str(p1)) 

    if is_prime(pcat1) and is_prime(pcat2):
        return True
    
    return False 

def naive_solution():
    primes = []
    for i in range(2, 1000):
        if is_prime(i):
            primes.append(i)
    n_primes = len(primes)

    for i in range(n_primes):
        first = primes[i]
        for j in range(i+1, n_primes):
            second = primes[j]
            if concat_primes(first,second):
                for k in range(j+1, n_primes):
                    third = primes[k]
                    if concat_primes(first, third) and concat_primes(second, third):
                        for w in range(k+1, n_primes):
                            fourth = primes[w]
                            if concat_primes(first, fourth) and concat_primes(second, fourth) and concat_primes(third, fourth):
                                print(first, second, third, fourth)
                                return

def find_tuple_of(size: int) -> int:
    partners = defaultdict(list)
    primes = []
    for i in range(2, 1000):
        if is_prime(i):
            primes.append(i)

    prime_set = set(primes)

    for first_prime in primes:
        for second_prime in primes:
            if second_prime == first_prime:
                break
            if concat_primes(first_prime, second_prime):
                partners[first_prime].append(second_prime)

        if len(partners[first_prime]) >= size - 1:
            for subset in combinations(partners[first_prime], size - 1):
                for i, number in enumerate(subset):
                    for other_number in subset[:i]:
                        if other_number not in partners[number]:
                            break
                    else:
                        continue
                    break
                else:
                    return first_prime + sum(subset)
        # break
print(find_tuple_of(3))         
# naive_solution()