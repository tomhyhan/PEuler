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
            print(i, j, k)
            print(nums)
            for x in nums[j]:
                for y in nums[k]:
                    for operand in operands:
                        if operand == "//" and y == 0:
                            continue
                        result = operands[operand](x,y)
                        if result == number:
                            return i
                        nums[i].add(result)
            print(nums) 

    return -1 

solution(5, 12)