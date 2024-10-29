def solution(N, number):

    operands = {
        "-" : lambda a, b: a - b, 
        "+" : lambda a, b: a + b, 
        "*" : lambda a, b: a * b, 
        "//" : lambda a, b: a // b
    }
    nums = [set() for _ in range(9)]
    
    for i in range(1, 9):
        nn = int(str(N) * i)
        if number == nn:
            return i
        nums[i].add(nn)
    
    for i in range(1, 9):
        for j in range(1, i):
            k = i - j
            for x in nums[j]:
                for y in nums[k]:
                    for operand in operands:
                        if operand == "//" and y == 0:
                            continue
                        result = operands[operand](x,y)
                        if result == number:
                            return i
                        nums[i].add(result)

    return -1 
    
# 5 55 555 5555
# 1 - 5
# 2 - 55 5+5 5-5 5*5 5//5
# 3 - 5+5+5 5+5-5 5+5*5 5+5//5
#   - 55+5 55-5 55*5 55//5
#   - 5+55 5-55 5*55 5//55
print(solution(5, 12))
print(solution(2,11))