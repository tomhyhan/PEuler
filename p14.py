from utils import time_checker
# 1000000

def helper(num, memo):
    if num == 1:
        return 1
    elif num in memo:
        return memo[num]
        
    steps = 0
    if num % 2 == 0:
        steps += helper(num / 2, memo) + 1
    else:
        steps += helper(3*num + 1, memo) + 1

    memo[num] = steps
    return steps

@time_checker
def solution():
    # 1000000
    memo = {}
    for n in range(1, 1000000):
        helper(n,memo)
    print(max(memo, key=memo.get))

solution()