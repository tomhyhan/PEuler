from itertools import combinations
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution():
    primes = []
    for i in range(2,18000):
        if is_prime(i):
            primes.append(i)
    
    for slide in range(len(primes), 1, -1):
        current_sum = sum(primes[:slide])
        left = len(primes) - slide
        if current_sum < 10**6 and is_prime(current_sum):
            print(current_sum)
            return
        for i in range(left):
            current_sum -= primes[i] 
            current_sum += primes[i + slide] 
            if current_sum < 10**6 and is_prime(current_sum):
                print(current_sum)
                print(slide)
                return  

def solution2():
    primes = []
    for i in range(2,19):
        if is_prime(i):
            primes.append(i)
    
    p_len = len(primes)
    for i in range(1,5):
        for j in range(1, i + 1):
            print(primes[i:p_len-j])
            current_sum = sum(primes[i:p_len-j])
            if current_sum < 10**6 and is_prime(current_sum):
                print(current_sum)
                return 
            
    pass

solution()
solution2()