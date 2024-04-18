import math
import itertools
import collections
        
def q_formula(a,b,c):
    return ((-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)).is_integer()

def solution():
    polygonal = [
            lambda x: [1, 1, -2*x], 
            lambda x: [1, 0, -x], 
            lambda x: [3, -1, -2*x],
            lambda x: [2, -1, -x],
            lambda x: [5, -3, -2*x],
            lambda x: [3, -2, -x],
        ]

    used = set()
    result = []
    for n in range(10, 100):
        f = str(n)
        helper(f, used, result, polygonal, f)
    print(sum([8128, 2882, 8256, 5625, 2512, 1281]))
    
def helper(f, used, result, polygonal, start):
    if len(used) == len(polygonal):
        if f == start:
            print(result)
        return
    
    for n in range(10, 100):
        s = str(n)
        num = int(f + s)
        for i in range(len(polygonal)):
            if i in used:
                continue
            if q_formula(*polygonal[i](num)):
                result.append(num)
                used.add(i)
                helper(s, used, result, polygonal, start)
                result.pop()
                used.remove(i)

solution()        
