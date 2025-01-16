
def helper(i, curr_sum, number, target):
    if i == len(number):
        return 1 if curr_sum == target else 0
    
    num = number[i]
    matches = 0
    matches += helper(i+1, curr_sum+num, number, target)
    matches += helper(i+1, curr_sum-num, number, target)

    return matches

def solution(numbers, target):
    
    result = helper(0, 0, numbers, target)
    return result

solution([1, 1, 1, 1, 1], 3)
solution([4, 1, 2, 1], 4)