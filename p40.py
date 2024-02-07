from utils import time_checker

@time_checker
def solution():
    s = "123456789"
    for i in range(10, 1000000):
        s += str(i)
    s = list(map(int, s))
    print(s[1-1]* s[10-1] * s[100-1] * s[1000-1] * s[10000-1] * s[100000-1] * s[1000000-1])

@time_checker
def solution2():
    mul_f = 9 
    result = 1

    for d in range(7):
        d = (10 ** d) - 1
        current_i = 0
        i = 0
        while True:
            expand = (10 ** (i-1)) * mul_f * i
            if expand + current_i > d:
                break 
            current_i += expand
            i += 1
        k = 10 ** (i-1)
        nth = int(d - current_i)
        step, remain = divmod(nth, i)
        result *= int(str(k + step)[remain])
    print(result)
    
solution()
solution2()