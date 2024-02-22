def is_pandigital(s):
    if '0' in s or len(s) != 9:
        return False
    return len(set(s)) == len(s)

def solution():
    max_p = 0
    for p in range(1,10000):
        for N in range(2,10):
            s = ""
            for n in range(1, N+1):
                s += str(p * n)
            if is_pandigital(s):
                max_p = max(max_p, p)
                print(p)
                print(s)
    print("max_p", max_p)
solution()