import numpy as np
from helper import time_checker

def is_prime(num):
    for n in range(2,int(num**(1/2))+1):
        if num % n == 0:
            return False
    return True

@time_checker
def solution():
    total = 0
    for num in range(2, 2000000):
        if is_prime(num):
            total += num
    print(total)

@time_checker
def solution1():
    # dp = np.zeros(2000000)
    dp = [0] * 2000000
    total = 2
    num = 3
    while num < 2000000:
        if dp[num] == 0:
            total += num
            notp = num
            while notp < 2000000:
                dp[notp] = 1
                notp += num
        num += 2
    print(total)

# solution()
solution1()