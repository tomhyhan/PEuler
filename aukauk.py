def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    p = 2
    
    while p  <= limit:
        if primes[p] is True:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1

    prime_numbers = {p for p in range(2, limit + 1) if primes[p]}
    return prime_numbers

import math 

def sieve_of_eratosthenes(limit):
    cmmn_cnts = [0] * (limit + 1)
    p = 2
    
    while p <= limit // 2 + 1:
        for i in range(2*p, limit + 1, p):
            cmmn_cnts[i] += 1
        p += 1

    return cmmn_cnts

def solution(e, starts):
    cmmn_cnts = sieve_of_eratosthenes(e)
    answer = []
    for num in starts:
        numbers = cmmn_cnts[num:e+1]
        max_value = max(numbers)
        max_index = numbers.index(max_value)
        answer.append(num + max_index)
    # print(answer)
    return answer

solution(8, [1,3,7])
# solution(12, [1,3,7])