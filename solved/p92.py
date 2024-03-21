def arrives_89(start_num, DP):
    if start_num == 1:
        return False
    elif start_num == 89:
        return True
    elif start_num in DP:
        return DP[start_num]

    next_num = sum([int(n) ** 2 for n in str(start_num)])

    result = arrives_89(next_num, DP)
    DP[start_num] = result
    return result

def solution():
    DP = {}
    cnt = 0
    for start_num in range(1,10000000):
        if arrives_89(start_num, DP):
            cnt += 1
            pass
    print(cnt)

solution()