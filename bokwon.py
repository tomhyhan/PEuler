def solution(expressions):
    nums = "23456789"
    
    joined_exp = ''.join(expressions)
    max_num = 0
    for num in nums:
        if num in joined_exp:
            max_num = max(max_num, int(num))
    
    p_bases = set([int(num) for num in nums if int(num) > max_num])
    
    hints = []
    results = []
    
    for expression in expressions:
        if 'X' in expression:
            results.append(expression)
        else:
            hints.append(expression)

    for hint in hints:
        f, o, s, _, r = hint.split(' ')
        equation = lambda x, y: x+y if o =='+' else x-y
        not_base = set()
        for base in p_bases:
            if equation(base_to_decimal(f, base), base_to_decimal(s, base)) != base_to_decimal(r, base):
                not_base.add(base)
        p_bases -= not_base
        
    solutions = []
    for result in results:
        f, o, s, _, _ = result.split(' ')
        p_solutions = set()
        equation = lambda x, y: x+y if o =='+' else x-y
        for base in p_bases:
            r = equation(base_to_decimal(f, base), base_to_decimal(s, base))
            p_solutions.add(decimal_to_base(r, base))

        if len(p_solutions) > 1:
            solutions.append(f"{f} {o} {s} = ?")
        else:
            solutions.append(f"{f} {o} {s} = {p_solutions.pop()}")
            
    return solutions

def base_to_decimal(snum, base):
    num = int(snum)
    dnum = 0
    pos = 0
    while num != 0 :
        num, remainder = divmod(num, 10)
        dnum += remainder * base ** pos
        pos += 1
    return dnum

def decimal_to_base(num, base):
    to_base = ''
    while num > 0:
        num, remainder = divmod(num, base)
        to_base = str(remainder) + to_base
    return to_base if to_base else 0

# solution(["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"])
# solution(["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"])
# solution(["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"])
solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"])