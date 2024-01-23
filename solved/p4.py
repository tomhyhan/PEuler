import numpy as np

# 10 3
def gcd(x,y):
    return y if x % y == 0 else gcd(y, x%y)

def lcm(*args):
    value = args[0]
    for i in range(1, len(args)):
        value = value * args[i] // gcd(value, args[i])
    return value

def solution():
    arr = np.array([i for i in range(1, 21)], dtype=np.int64)
    print(lcm(*arr))

solution()