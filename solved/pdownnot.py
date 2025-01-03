def solution(prices):
    answer = [0 for _ in prices]
    stack = []
    for i in range(len(prices)):
        
        while stack and stack[-1][1] > prices[i]:
            j, _ = stack.pop()
            answer[j] = i-j
        stack.append((i, prices[i]))
    for i, p in stack:
        answer[i] = len(prices) - i -1
    print(answer)
    
# [4, 3, 1, 1, 0]
solution([1, 2, 3, 2, 3])