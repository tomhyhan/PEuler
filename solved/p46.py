import math
 
def is_prime(num):
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    return True

def is_gb(odd):
    for p in range(0,odd):
        if not is_prime(p):
            continue
        for n in range(0,1000):
            if odd == p + 2 * (n**2):
                return True    
    return False

def solution():
    for n in range(3,100000, 2):
        if is_prime(n):
            continue
        if not is_gb(n):
            print(n)
            break

solution()