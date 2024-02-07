import math 

def solution():
    total = 0
    for num in range(3, 2177280):
        sn = sum(map(lambda x: math.factorial(int(x)), list(str(num))))
        if sn == num:
            print(num)
            total += num
    print(total)
solution()