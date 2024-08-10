from collections import Counter

def solution(a):
    stack = []
    
    for i in range(len(a)):
        stack.append(a[i])
        
        if len(stack) > 3 and a[i-2] == a[i-1] == a[i]:
            if i == 2 or i == len(a) - 1:
                stack.pop()
            stack.pop()

    if len(stack) > 2 and stack[0] == stack[1]:
        stack = stack[1:]
    
    if len(stack) > 2 and stack[-2] == stack[-1]:
        stack = stack[:-1]

    a_cnt = Counter(a)
    a_max = max(a_cnt.values())
    print(a_cnt)   
    print(a_max)

# [5,2,3,3,5,3] -> wrong
    
# solution([0,3,3,0,7,2,0,2,2,0,0])
solution([0,3,3,0,7,2,0,2,2,0])
solution([5,2,3,3,5,3])
solution([0])