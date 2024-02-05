from itertools import permutations
import math
def solution():
    num = 10
    for i, perm in enumerate(permutations(list(range(num)), num)):
        if i == 1000000-1:
            print(''.join(map(str, perm)))

def solution1():
    digit = ""
    m = 1000000 - 1
    seen = set()
    for i in reversed(range(1,11)):
        di = 0
        current_digits = [n for n in list(range(10)) if n not in seen]
        perm_n = math.factorial(i) / i
        a = perm_n
        while a <= m : 
            a += perm_n
            di += 1
        digit += str(current_digits[di])
        seen.add(current_digits[di])
        m = m - a + perm_n

    print(digit)
    # print(m - 2 * a )
    # print(math.factorial(10) % 1000000)
    # pass

solution()
solution1()