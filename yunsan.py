def helper(tokens):
    if len(tokens) == 1:
        return tokens[0]
    
    max_sum = float('-inf')
    
    for i in range(1, len(tokens)):
        left = helper(tokens[:i])
        right = helper(tokens[i:])
        current = left + right
        max_sum = max(max_sum, current)
    
    return max_sum

def solution(arr):
    # Parse numbers and operators
    numbers = [int(arr[i]) for i in range(0, len(arr), 2)]
    operators = [arr[i] for i in range(1, len(arr), 2)]
    
    # Create tokens with proper signs
    tokens = [numbers[0]]
    for i in range(len(operators)):
        if operators[i] == '+':
            tokens.append(numbers[i + 1])
        else:  # '-'
            tokens.append(-numbers[i + 1])
    print(helper(tokens))
    return 
# (((1 - 3) + 5) - 8) = -5
# ((1 - (3 + 5)) - 8) = -15
# (1 - ((3 + 5) - 8)) = 1
# (1 - (3 + (5 - 8))) = 1
# ((1 - 3) + (5 - 8)) = -5

# 1 -3 +5 -8, (1-3)+5-8 | 1-(3+5)-8 | 1-3+(5-8), (-2+5)-8 | -2+(5-8) 
solution(["1", "-", "3", "+", "5", "-", "8"])
solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"])
# solution(["5", "-", "3", "+", "1", "+", "2", "-", "4", '+', "5", "-", "3", "+", "1", "+", "2", "-", "4", '+', "5", "-", "3", "+", "1", "+", "2", "-", "4", '+', "5", "-", "3", "+", "1", "+", "2", "-", "4"])