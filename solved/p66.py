import math
from p65 import converge
from p64 import cont_faction

def solution():
    max_d = 0
    num = 0
    for i in range(2, 1000):
        if math.sqrt(i).is_integer():
            continue
        continue_fraction = cont_faction(i)
        n_cf = len(continue_fraction[1:])
        if n_cf % 2 == 1:
            continue_fraction += continue_fraction[1:]
        # print(continue_fraction)
        n,d = converge(continue_fraction[:-1])
        if max_d < d:
            max_d = d
            num = i 
    print(max_d, num)
solution()