def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    p = 2
    
    while p * p <= limit:
        if primes[p] is True:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1

    prime_numbers = {p for p in range(2, limit + 1) if primes[p]}
    return prime_numbers

def solution(e, starts):
    primes = sieve_of_eratosthenes(e)
    answer = []
    cnts = [0 for i in range(e + 1)]

    # primes = 
    
    for i in range(2,e+1):
        if i in primes:
            continue
        cnts[i] = cnt_common_div(i)
        
        #     passis_prime(i):
        #     cnts[i] = 1
        # else:
    
    # print(cnts)
    # for num in starts:
    #     print(sorted(cnts[num:e+1], ))
    #     pass        


# solution(8, [1,3,7])
solution(5000000, [1,3,7])