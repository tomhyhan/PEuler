def solution(expressions):
    nums = "123456789"
    p_bases = set([int(num) for num in nums])
    
    joined_exp = ''.join(expressions)
    for num in nums:
        if num in joined_exp:
            p_bases.remove(int(num))
    
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
            try:
                if equation(int(f, base), int(s, base)) != int(r, base):
                    not_base.add(base)
            except:
                not_base.add(base)
        p_bases -= not_base
        
    print("p_bases", p_bases)            
    print(int("16", 6))
    solutions = []
    for result in results:
        f, o, s, _, _ = result.split(' ')
        p_solutions = set()
        equation = lambda x, y: x+y if o =='+' else x-y
        for base in p_bases:
            r = equation(int(f, base), int(s, base))
            print("r", r)
            p_solutions.add(int(str(r), base))

        if len(p_solutions) > 1:
            solutions.append(f"{f} {o} {s} = ?")
        else:
            solutions.append(f"{f} {o} {s} = {p_solutions.pop()}")
            
    print(solutions)

def base_to_decimal(num, base):
    dnum = 0
    pos = 0
    while num != 0 :
        num, remainder = divmod(num, 10)
        dnum += remainder * base ** pos
        pos += 1
    return dnum

def decimal_to_base(num, base):
    
    pass

print(base_to_decimal(14, 6))
# solution(["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"])
# solution(["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"])