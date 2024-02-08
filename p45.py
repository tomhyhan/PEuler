import math

def is_t(val):
    n = (math.sqrt(1 + 8 * val) - 1) / 2
    return int(n) == n

def is_p(val):
    n = (math.sqrt(1 + 24 * val) + 1) / 6
    return int(n) == n

def solution():
    for n in range(144, 1000000):
        h = n * (2*n - 1)
        if is_t(h) and is_p(h):
            print(n)
            print(h)
            break

solution()