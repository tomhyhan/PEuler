import math 

def solution():
    fn = 3
    fd = 7
    l = 1000000

    fractions = []
    for d in range(3, l+1):
        n = find_n(d, fn, fd)
        if n * fd < fn * d:
            fractions.append([n / d, (n,d)])
    print(max(fractions))
    print(math.gcd(428570, 999997))

    
def find_n(d, fn, fd):
    left = 0
    right = d * fn // fd
    while left + 1< right:
        mid = (left + right) // 2
        if mid * fd < fn * d:
            left = mid
        else:
            right = mid
    return right

def solution1():
    # using Farey sequence
    x = (1000000 - 5) // 7 
    print(2 + 3 * x)
    print(5 + 7 * x)
    pass

# solution()
solution1()