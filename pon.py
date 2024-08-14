def solution(N, number):

    operands = ["-", "+", "*", "/"]
    def helper(evaluation, isNum, p_open, n_used):
        if not isNum:
            evaluation2 = evaluation + ')'
            try:
                if eval(evaluation) == number:
                    print(evaluation)
                print(eval(evaluation))
            except Exception:
                pass
            
        if n_used == 0:
            return
        # print(evaluation)
        if isNum:
            for i in range(1, n_used + 1):
                num = str(N) * i 
                if n_used - i != 0:
                    helper(evaluation + f"({num}", False, p_open+1, n_used - i)
                elif n_used - i != 0 and p_open > 0:
                    helper(evaluation + f"{num})", False, p_open-1, n_used - i)
                
                helper(evaluation + num, False, p_open, n_used - i)
        else:
            for op in operands:
                helper(evaluation + op, True, p_open, n_used)
    helper("", True, 0, 8)
    

# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5
solution(5, 12)