def base_dec(base, num):
    factor = 1
    dec = 0
    num = int(num)
    while num > 0:
        x, remain = divmod(num, 10)
        dec += remain * factor
        factor *= base
        num = x
    return dec    

def dec_base(base, dec):
    if dec == 0:
        return '0'
    base_num = ''
    
    while dec > 0:
        dec, remain = divmod(dec, base)
        base_num = str(remain) + base_num 
    return int(base_num)

def solution(expressions):
    # base 2 - 9 
    norm_exps = []
    X_exps = []
    
    OPS = {
        '+': lambda a,b: a+b,
        '-': lambda a,b: a-b
    }

    max_pos = set()
    for expression in expressions:
        f, op, s, _, r = expression.split(' ')
        if 'X' in expression:
            X_exps.append(expression)
            max_pos |= set(f) | set(s)
        else:
            norm_exps.append(expression)
            max_pos |= set(f) | set(s) | set(r)
    max_pos = int(max(max_pos))

    bases = set(range(max_pos + 1,10))
    for norm_exp in norm_exps:
        f, op, s, _, r = norm_exp.split(' ')
        remove_base = set()
        for base in bases:
            if base_dec(base, r) != OPS[op](base_dec(base, f), base_dec(base, s)):
                remove_base.add(base)
        bases -= remove_base
    
    result = []
    for x_exp in X_exps:
        f, op, s, _, _ = x_exp.split(' ')
        x_cand = set()
        for base in bases:
            evaluate = OPS[op](base_dec(base, f), base_dec(base, s))
            x_cand.add(dec_base(base, evaluate))

        if len(x_cand) > 1:
            result.append(f"{f} {op} {s} = ?")
        else:
            r = x_cand.pop()
            result.append(f"{f} {op} {s} = {r}")
    return result      
    
# ["13 - 6 = 5"]
# solution(["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"])
# ["1 + 5 = ?", "1 + 2 = 3"]
# solution(["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"])
# ["10 - 2 = 4", "3 + 3 = 10", "33 + 33 = 110"]
# solution(["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"])
# ["2 + 2 = 4", "7 + 4 = ?", "5 - 5 = 0"]
# solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"])

# prev solution
# def solution(expressions):
#     nums = "23456789"
    
#     joined_exp = ''.join(expressions)
#     max_num = 0
#     for num in nums:
#         if num in joined_exp:
#             max_num = max(max_num, int(num))
    
#     p_bases = set([int(num) for num in nums if int(num) > max_num])
    
#     hints = []
#     results = []
    
#     for expression in expressions:
#         if 'X' in expression:
#             results.append(expression)
#         else:
#             hints.append(expression)

#     for hint in hints:
#         f, o, s, _, r = hint.split(' ')
#         equation = lambda x, y: x+y if o =='+' else x-y
#         not_base = set()
#         for base in p_bases:
#             if equation(base_to_decimal(f, base), base_to_decimal(s, base)) != base_to_decimal(r, base):
#                 not_base.add(base)
#         p_bases -= not_base
        
#     solutions = []
#     for result in results:
#         f, o, s, _, _ = result.split(' ')
#         p_solutions = set()
#         equation = lambda x, y: x+y if o =='+' else x-y
#         for base in p_bases:
#             r = equation(base_to_decimal(f, base), base_to_decimal(s, base))
#             p_solutions.add(decimal_to_base(r, base))

#         if len(p_solutions) > 1:
#             solutions.append(f"{f} {o} {s} = ?")
#         else:
#             solutions.append(f"{f} {o} {s} = {p_solutions.pop()}")
            
#     return solutions

# def base_to_decimal(snum, base):
#     num = int(snum)
#     dnum = 0
#     pos = 0
#     while num != 0 :
#         num, remainder = divmod(num, 10)
#         dnum += remainder * base ** pos
#         pos += 1
#     return dnum

# def decimal_to_base(num, base):
#     to_base = ''
#     while num > 0:
#         num, remainder = divmod(num, base)
#         to_base = str(remainder) + to_base
#     return to_base if to_base else 0