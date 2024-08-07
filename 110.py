import re

def solution(s):
    result = []
    for i in range(len(s)):
        a = list(s[i])
        helper(a, 0)
        # print(a)
        result.append(''.join(a))
    print(result)
    return result

def helper(a, l):
    joined = ''.join(a[l:])
    if not (find := re.search(r'111+0', joined)):
        return
    b, e = find.span()
    a[l+b+2], a[l+e-1] = a[l+e-1], a[l+b+2]
    helper(a, l+b+3)

# ["1101","100110110","0110110111"]
solution(["1110","100111100","0111111010"])

# 0110110110110101


# 0101101101101101
# 1100110110110101
solution(["0110111011101001"])
