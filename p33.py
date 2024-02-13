def gcd(x,y):
    return y if x % y == 0 else gcd(y, x%y)

def solution():
    nu = 1
    de = 1
    for d in range(11,100):
        for n in range(10, d):
            sn1 = int(str(n)[0])
            sn2 = int(str(n)[1])
            sd1 = int(str(d)[0])
            sd2 = int(str(d)[1])
            if d % 10 == 0:
                continue
            if n / d < 1 and sn2 == sd1 and n / d == sn1 / sd2:
                # print(n, d)
                # print(gcd(n,d))
                c = gcd(n,d)
                nu *= n // c
                de *= d // c
    print(nu, de)
solution()