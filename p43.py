from collections import deque

PRIMES = [2,3,5,7,11,13,17]

def find_d(num, pi, pandigital, pandigitals):
    if pi == -1:
        if len(set(pandigital)) == 10:
            pandigitals.append([n for n in pandigital])
        return pandigital

    if num % PRIMES[pi] == 0:
        for i in range(0, 10):
            new_num = num // 10 + i * 100
            if i in pandigital:
                continue
            pandigital.appendleft(i)
            find_d(new_num, pi - 1, pandigital, pandigitals)
            pandigital.popleft()
            
    return False

def solution():
    sums = 0
    for num in range(102, 1000):
        pandigital = deque(map(int, list(str(num))))
        pandigitals = []
        find_d(num, 6, pandigital, pandigitals)
        if len(pandigitals) > 0:
            print("pandigitals", pandigitals)
            for pan in pandigitals:
                pint = ''.join(map(str, pan))
                sums += int(pint)
    print(sums)

solution()