import re

def find_110(s):
    stack = []
    
    n_110 = 0
    for i in range(len(s)):
        stack.append(s[i])

        if len(stack) > 2 and ''.join(stack[-3:])== "110":
            n_110 += 1
            stack.pop()
            stack.pop()
            stack.pop()
    
    return ''.join(stack), n_110

def solution(s):
    for i in range(len(s)):
        stack, n_110 = find_110(list(s[i]))
        stack = stack[::-1]
        idx_0 = stack.find('0')
        print("idx_0", idx_0, n_110, stack)
        if idx_0 != -1:
            s[i] = ''.join(stack[:idx_0] + "011" * n_110 + stack[idx_0:])[::-1]
        else:
            s[i] = ''.join(stack + "011" * n_110 )[::-1]
    return s

    print(s)
    #     pass
            # s[i] = s[i].replace("110", "") + "110" * cnt

# ["1101","100110110","0110110111"]
solution(["1110","100111100","0111111010"])
# 0111

# 0111011011011001
# 0101101101101101
# 1100110110110101
solution(["1100110110110101"])

# 1 110 0 0 11 110 0
# 1  0 0 110 110 11  0