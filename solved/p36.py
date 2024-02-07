from utils import time_checker

def is_palin(num):
    left = 0
    right = len(num) - 1
    while left < right:
        if num[left] != num[right]:
            return False
        left += 1
        right -= 1
    return True

@time_checker
def solution():
    total = 0
    for num in range(1, 1000000):
        snum = str(num)
        sbnum = bin(num)[2:]
        if is_palin(snum) and is_palin(sbnum):
            total += num
    print(total)

@time_checker
def solution2():
    total = 0
    a = ['1','3','5','7','9']
    s_nums = [str(i) for i in range(10)]
    aa = [an + an for an in a]
    aba = [an + bn + an for an in a for bn in s_nums]
    abba = [an + bn + bn + an for an in a for bn in s_nums]
    abcba = [an + bn + cn + bn + an for an in a for bn in s_nums for cn in s_nums]
    abccba = [an + bn + cn + cn + bn + an for an in a for bn in s_nums for cn in s_nums]
    possibles = a + aa+ aba + abba + abcba + abccba
    for num in possibles:
        snum = str(num)
        sbnum = bin(int(num))[2:]
        if is_palin(snum) and is_palin(sbnum):
            total += int(num)
    print(total)

solution()
solution2()