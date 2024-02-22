import math 
from utils import time_checker

def combinator(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))

@time_checker
def solution():
    cnt = 0
    for n in range(1,101):
        for r in range(1,n+1):
            if combinator(n,r) > 1000000:
                cnt += 1
    print(cnt)

@time_checker
def solution1():
    DP = {}
    for n in range(101):
      DP[(n,0)] = 1  
      DP[(n,n)] = 1  
    cnt = 0
    for n in range(1,101):
        for r in range(1,n):
            DP[(n,r)] = DP[(n-1,r)] + DP[(n-1,r-1)]
            if DP[(n,r)] > 1000000:
                cnt += 1
    print(cnt)

solution()
solution1()