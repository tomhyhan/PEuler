def is_palin(snum):
    left = 0
    right = len(snum) - 1
    while left < right:
        if snum[left] != snum[right]:
            return False
        left += 1
        right -= 1
    return True

def is_lychrel(num):
    cnt = 50
    while cnt > 0 :
        rs = int(''.join(reversed(str(num))))
        num += rs
        if is_palin(str(num)):
            return False
        cnt -= 1
    return True

def solution():
    cnt = 0
    for n in range(1, 10000):
        if is_lychrel(n):
            cnt += 1
    print(cnt)
    print(is_lychrel(4994))
solution()