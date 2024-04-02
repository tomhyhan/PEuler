from collections import defaultdict

def solution():
    cnts = defaultdict(list)
    for num in range(1000,10000):
        perm = tuple(sorted(str(num ** 3)))
        cnts[perm].append(num)
    for k, v in cnts.items():
        if len(v) >=5:
            print(''.join(k))
            print(v)
    print(5027 ** 3)
solution()