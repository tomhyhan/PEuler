def solution():
    max_digit_sum = 0

    for a in range(1,100):
        for b in range(1,100):
            s = a ** b
            ss = sum(map(int, list(str(s))))
            max_digit_sum = max(max_digit_sum, ss)
    print(max_digit_sum)

solution()