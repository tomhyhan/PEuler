def solution():
    cnt = 0
    for digit in range(1, 100):
        for base in range(1,100):
            bd = str(base ** digit)
            if len(bd) == digit:
                cnt += 1 
                print(base, digit, bd)
    print(cnt )
solution()