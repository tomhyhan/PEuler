def helper(i, e_const, l):
    if i == l:
        denom = e_const[i]
        numer = e_const[i-1] * denom + 1
        return denom, numer
    numer, denom = helper(i+1, e_const, l)
    if i == 0:
        return numer, denom
    # print(numer, denom)
    new_numer = e_const[i-1] * denom + numer
    # print("new_numer", new_numer, denom)
    return denom, new_numer

def converge(continue_fraction):
    n, d = helper(0, continue_fraction, len(continue_fraction) - 1)
    return n, d

def solution():
    e = [3,1,1,1,1,6,1,1,1,1]
    # f = 2
    # for i in range(2, 150):
    #     if i % 3 == 0:
    #         k = f
    #         f += 2
    #     else:
    #         k = 1
    #     e.append(k)
    # print(e)
    n, d = helper(0, e, len(e) - 1)

    print(n, d)
    # n, d = helper(0, e, 100 - 2)
    # n, d = helper(0, e, 100 - 2)
    # print(d *2 + n, d)
    # print(sum(map(int, str(d *2 + n))))
# solution()
