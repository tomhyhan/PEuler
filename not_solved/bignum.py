def solution(number, k):
    stack = []
    delete = 0
    
    i = 0
    while i < len(number) and delete < k:
        curr_num = number[i]
        while stack and delete < k and curr_num > stack[-1]:
            stack.pop()
            delete += 1
        stack.append(curr_num)
        i += 1

    return (''.join(stack) + number[i:])[:len(number)-k]
    
# 9841

# # "94"
# solution("1924", 2)
# # # "3234"
# solution("1231234", 3)
# # # "775841"
# solution("4177252841", 4)
# # "984"
# solution("179252841", 6)
# solution("190000002", 3)
