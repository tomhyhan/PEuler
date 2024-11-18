from collections import defaultdict
import copy 
from functools import reduce

def solution(clothes):
    memo = defaultdict(int)
    for _, cate in clothes:
        memo[cate] += 1
    combs = list(memo.values())

    powerset = [[]]
    for num in combs:
        n_powerset = len(powerset)
        for i in range(n_powerset):
            temp = copy.deepcopy(powerset[i])
            temp.append(num)
            powerset.append(temp)
            
    total = 0
    for pset in powerset:
        if pset:
            total += reduce(lambda x, y: x * y, pset)
    return total

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
        
    