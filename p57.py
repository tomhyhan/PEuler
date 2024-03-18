import sys

new_limit = 5000 
sys.setrecursionlimit(new_limit)

def con_root(cnt, limit):
    if cnt == limit:
        return 5, 2
    nu, de = con_root(cnt + 1, limit)
    new_de = nu
    new_nu = 2 * nu + de
    return new_nu, new_de  

def solution():
    pairs = []

    for i in range(1, 30):
        x, y = con_root(1, i)
        pairs.append((y,x))

    cnt = 0
    for i ,pair in enumerate(pairs):
        nu, de = pair
        if len(str(nu + de)) > len(str(de)):
            print(de, i)
            cnt += 1 
    print(cnt)
solution()