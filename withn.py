def solution(N, number):
    OPS = {
        '+': lambda a,b: a+b,
        '/': lambda a,b: a//b,
        '-': lambda a,b: a-b,
        '*': lambda a,b: a*b,
    }
    L = 8
    DP = [set([int(str(N) * i)]) if i != 0 else set() for i in range(L+1)]

    for i in range(1,L):
        j = L - i + 1
        for k in range(1,j):
            for inum in DP[i]:
                for knum in DP[k]:
                    for op in OPS:
                        if knum == 0:
                            DP[i+k].add(0)
                            continue
                        DP[i+k].add(OPS[op](inum,knum))

    for i in range(1,L+1):
        if number in DP[i]:
            return i
    return -1
# [(5), (55, 5+5, 5/5), (555, 5+55, 5/55, ..., 55+5, 55/5, 5+5+5, 5+5/5, 5/5+5, 5/5/5), (5555)] 15
# 12 = 5 + 5 + (5 / 5) + (5 / 5)
solution(5,12)