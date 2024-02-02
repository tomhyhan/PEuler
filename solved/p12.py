import math
from utils import time_checker

def num_divisor(num):
    divisors = 0
    
    if num == 1:
        return 1
        
    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0:
            divisors += 2
            
    if math.sqrt(num) ** 2 == num:
        divisors -= 1

    return divisors

@time_checker
def solution():
    num = 1
    trig = 1
    while num_divisor(trig) <= 500:
        trig = (num * (num + 1)) // 2
        num += 1
    print(trig)

@time_checker
def solution2():
    num = 1
    trig = None
    while True:
        trig = (num * (num + 1)) // 2
        if num % 2 == 0:
            divisors = num_divisor(num // 2) * num_divisor(num + 1)
        else:
            divisors = num_divisor(num) * num_divisor((num + 1) //2)
        if divisors > 500:
            trig = (num * (num + 1)) // 2
            break
        num += 1
    print(trig)

solution()
solution2()