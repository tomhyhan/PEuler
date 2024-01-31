import sys
import math
from decimal import Decimal
from utils import time_checker

sys.setrecursionlimit(9999)

def solution():
    # 1 1 2 3 
    a,b,i = 1,1,2
    while len(str(b)) < 1000:
        a, b = b, a + b 
        i += 1
    print(b)
    print(i)

def helper(idx, memo):
    if idx < 2:
        return idx
    elif idx in memo:
        return memo[idx]

    memo[idx] = helper(idx - 1, memo) + helper(idx - 2,memo) 
    return memo[idx]

@time_checker
def solution2():
    # 0 1 1 2 3 5 8 
    memo = {}
    num = helper(1000, memo)

def golden_ratio_conjugate():
    return (1-math.sqrt(5)) / 2

def golden_ratio():
    return (1+math.sqrt(5)) / 2

# ((golden_ratio() ** idx) - (golden_ratio_conjugate() ** idx))/math.sqrt(5)
# round((golden_ratio() ** idx) / math.sqrt(5))
def solution3():
    # 0 1 1 2 3 5 8 13 21
    """
        (golden_ratio() ** idx) / math.sqrt(5) > 10 ** 999 
        log((golden_ratio() ** idx)) - log(math.sqrt(5)) > log(10 ** 999)
        idx * log(golden_ratio()) > 999 + log(5) / 2
        idx  > (999 + log(5) / 2) / log(golden_ratio())
    """
    num_digit = 999
    print((num_digit * math.log(10) + math.log(5) / 2)  / math.log(golden_ratio()))

def solution4():
    print(Decimal(golden_ratio()) ** 4780)
    print(Decimal(golden_ratio()) ** 4781)

solution()
solution2()
solution3()
solution4()