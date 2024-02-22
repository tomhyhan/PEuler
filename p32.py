def has_same_digit(snum):
    if '0' in snum:
        return True
    return len(set(snum)) != len(snum)

def solution():
    pandigital = set()
    for a in range(100,1001):
        for b in range(10,101):
            mutiplier = str(a) + str(b)
            if has_same_digit(str(a) + str(b)):
                continue
            multiple = str(a * b)
            if has_same_digit(mutiplier + multiple):
                continue
            # print(a,b,multiple)
            pandigital.add(multiple)
            
    for a in range(1000,10000):
        for b in range(1,10):
            mutiplier = str(a) + str(b)
            if has_same_digit(str(a) + str(b)):
                continue
            multiple = str(a * b)
            if has_same_digit(mutiplier + multiple):
                continue
            print(a,b,multiple)
            pandigital.add(multiple)

    print(sum(map(int, pandigital)))

solution()