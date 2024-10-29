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
    memo = {}
    current_max = -1
    current_index = -1
    right_bound = e+1
    for num in sorted(starts, reverse=True):
        nums = cmmn_cnts[num:right_bound]
        max_value = max(nums)
        max_index = nums.index(max_value) + num
        
        if max_value >= current_max:
            current_max = max_value
            current_index = max_index
        
        right_bound = num
        memo[num] = current_index
    # print(memo)
    return [memo[start] for start in starts]

solution(8, [1,3,7])
# solution(12, [1,3,7])