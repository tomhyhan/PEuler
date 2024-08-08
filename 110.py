import re

def find_and_replace(s):
    stack = ""
    i11 = -1
    i0 = -1
    i1 = -1
    cnt = 0
    
    len_s = len(s)
    
    s = s[::-1]
    i = 0
    print(s)
    while i < len_s:
        if s[i:i+3] == "011":
            i += 2
            cnt += 1
            print(i, s[i:i+3])
        elif s[i:i+2] == "11":
            stack = s[i:i+2] + stack
            i += 1
            i11 = len_s-i-1 
        elif s[i] == '0':
            stack = s[i] + stack
            i0 = len_s-i-1  if i0 == -1 else i0
        elif s[i] == '1':
            stack = s[i] + stack
            i1 = len_s-i-1 
        else:
            raise Exception("wrong")
        i += 1
    return stack, cnt, i11, i0, i1
             

def solution(s):
    for i in range(len(s)):
        a, cnt, i11, i0, i1 = find_and_replace(s[i])
        print(a, cnt, i11, i0, i1)
        while True:
            if i11 != -1:
                s[i] = a[:i11] + "110" * cnt + a[i11:]
            else:
                if i0 != -1:
                    s[i] = a[:i0+1] + "110" * cnt + a[i0+1:]
                else:
                    s[i] = a[:i1] + "110" * cnt + a[i1:]
            a, curr_cnt, i11, i0, i1 = find_and_replace(s[i])
            if curr_cnt > cnt:
                cnt = curr_cnt
            else:
                break 
    print(s)
            
    return s
            # s[i] = s[i].replace("110", "") + "110" * cnt

# ["1101","100110110","0110110111"]
# solution(["1110","100111100","0111111010"])
# 0101101101101101

# 0111011011011001
# 0101101101101101
# 1100110110110101
# solution(["1100110110110101"])
solution(["0111111010"])

# 1 110 0 0 11 110 0
# 1  0 0 110 110 11  0